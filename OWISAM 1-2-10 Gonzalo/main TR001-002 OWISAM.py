#!/usr/bin/env python3
import subprocess
import os
import time
import argparse
import sys

class WiFiOpenWEP:
    def __init__(self, interface):
        self.interface = interface
        self.output_dir = "wifiopenwep_output"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, text=True, capture_output=True)
            if result.stderr and "error" in result.stderr.lower():
                print(f"Error: {result.stderr}")
                return False
            return True
        except Exception as e:
            print(f"Error ejecutando comando: {e}")
            return False

    def check_root(self):
        if os.geteuid() != 0:
            print("Este script debe ejecutarse como root (usa sudo).")
            sys.exit(1)

    def setup_monitor_mode(self):
        print(f"Configurando {self.interface} en modo monitor...")
        if not self.run_command(f"ip link set {self.interface} down"):
            print("Error al desactivar la interfaz.")
            sys.exit(1)
        if not self.run_command(f"iwconfig {self.interface} mode monitor"):
            print("Error al configurar modo monitor.")
            sys.exit(1)
        if not self.run_command(f"ip link set {self.interface} up"):
            print("Error al reactivar la interfaz.")
            sys.exit(1)
        print(f"{self.interface} en modo monitor.")

    def scan_networks(self, duration=15):
        print(f"Escaneando redes durante {duration} segundos...")
        scan_file = os.path.join(self.output_dir, "openwep_scan")
        for f in os.listdir(self.output_dir):
            if f.startswith("openwep_scan") and f.endswith(".csv"):
                os.remove(os.path.join(self.output_dir, f))
        cmd = f"airodump-ng --output-format csv -w {scan_file} {self.interface} > /dev/null 2>&1"
        process = subprocess.Popen(cmd, shell=True)
        time.sleep(duration)
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            print("Proceso de airodump-ng forzado a terminar.")
        if not self.run_command(f"ip link show {self.interface} | grep UP"):
            print("Error: La interfaz se desactivó durante el escaneo.")
            sys.exit(1)
        csv_file = f"{scan_file}-01.csv"
        if not os.path.exists(csv_file):
            print("Error: No se generó el archivo de escaneo. Verifica la interfaz.")
            return None
        print("Archivo CSV generado correctamente.")
        return csv_file

    def process_csv(self, csv_file):
        print("Procesando CSV...")
        networks = []
        seen_bssids = set()
        try:
            with open(csv_file, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if not line.strip() or "BSSID" in line or "Station" in line:
                        continue
                    parts = line.split(",")
                    if len(parts) >= 14:
                        bssid = parts[0].strip()
                        if bssid in seen_bssids:
                            continue
                        seen_bssids.add(bssid)
                        essid = parts[13].strip() or "<Oculto>"
                        channel = parts[3].strip()
                        encryption = parts[5].strip()
                        if encryption in ["OPN", "WEP"]:
                            networks.append({
                                "bssid": bssid,
                                "essid": essid,
                                "channel": channel,
                                "encryption": encryption
                            })
        except Exception as e:
            print(f"Error procesando CSV: {e}")
            return []
        if not networks:
            print("No se encontraron redes abiertas o WEP.")
        else:
            print(f"Se encontraron {len(networks)} redes vulnerables.")
        return networks

    def generate_report(self, networks):
        print("\n=== WiFiOpenWEP Report ===")
        print(f"Fecha: {time.ctime()}")
        print(f"\nRedes vulnerables detectadas ({len(networks)}):")
        if not networks:
            print("  Ninguna red abierta o WEP encontrada.")
        for net in networks:
            print(f"ESSID: {net['essid']}")
            print(f"BSSID: {net['bssid']}")
            print(f"Canal: {net['channel']}")
            print(f"Encripción: {net['encryption']}")
            print()

    def cleanup(self):
        print("Restaurando interfaz...")
        self.run_command(f"ip link set {self.interface} down")
        self.run_command(f"iwconfig {self.interface} mode managed")
        self.run_command(f"ip link set {self.interface} up")
        self.run_command("systemctl start NetworkManager")

def main():
    parser = argparse.ArgumentParser(description="WiFiOpenWEP: Detecta redes Wi-Fi abiertas o WEP")
    parser.add_argument("-i", "--interface", required=True, help="Interfaz Wi-Fi (ej. wlan0)")
    parser.add_argument("-t", "--time", type=int, default=15, help="Tiempo de escaneo en segundos (default: 15)")
    args = parser.parse_args()

    probe = WiFiOpenWEP(args.interface)
    probe.check_root()
    try:
        probe.setup_monitor_mode()
        csv_file = probe.scan_networks(args.time)
        if csv_file:
            networks = probe.process_csv(csv_file)
            probe.generate_report(networks)
    finally:
        probe.cleanup()

if __name__ == "__main__":
    main()
