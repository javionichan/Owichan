#!/usr/bin/env python3

import os
import subprocess
import time
import scapy.all as scapy
import re
from datetime import datetime
import logging

# Configuración de logging para registrar eventos
logging.basicConfig(filename='wifi_audit.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Colores para la salida en consola
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

class WiFiAuditor:
    def __init__(self, interface):
        self.interface = interface
        self.vulnerabilities = []
        self.networks = []

    def set_monitor_mode(self):
        """Configura la interfaz Wi-Fi en modo monitor."""
        try:
            subprocess.run(['sudo', 'ifconfig', self.interface, 'down'], check=True)
            subprocess.run(['sudo', 'iwconfig', self.interface, 'mode', 'monitor'], check=True)
            subprocess.run(['sudo', 'ifconfig', self.interface, 'up'], check=True)
            logging.info(f"Interfaz {self.interface} configurada en modo monitor.")
            print(f"{GREEN}[+] Interfaz {self.interface} en modo monitor.{RESET}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error al configurar modo monitor: {e}")
            print(f"{RED}[-] Error al configurar modo monitor: {e}{RESET}")
            exit(1)

    def scan_networks(self, duration=30):
        """Escanea redes Wi-Fi utilizando Scapy."""
        print(f"{YELLOW}[*] Escaneando redes Wi-Fi durante {duration} segundos...{RESET}")
        self.networks = []

        def packet_handler(packet):
            if packet.haslayer(scapy.Dot11Beacon):
                bssid = packet[scapy.Dot11].addr2
                ssid = packet[scapy.Dot11Elt].info.decode('utf-8', errors='ignore')
                if ssid == '':
                    ssid = '<HIDDEN>'
                
                # Extraer información de cifrado
                encryption = self.get_encryption(packet)
                wps = self.check_wps(packet)

                if {'bssid': bssid, 'ssid': ssid} not in self.networks:
                    self.networks.append({
                        'bssid': bssid,
                        'ssid': ssid,
                        'encryption': encryption,
                        'wps': wps
                    })

        scapy.sniff(iface=self.interface, prn=packet_handler, timeout=duration)
        self.analyze_vulnerabilities()

    def get_encryption(self, packet):
        """Determina el tipo de cifrado de la red."""
        try:
            if packet.haslayer(scapy.Dot11Beacon):
                cap = packet.sprintf("%Dot11Beacon.cap%")
                if 'privacy' not in cap:
                    return 'OPEN'
                else:
                    # Analizar RSN (WPA/WPA2) o WEP
                    for elt in packet[scapy.Dot11Elt]:
                        if elt.ID == 48:  # RSN
                            return 'WPA/WPA2'
                        elif elt.ID == 221 and 'WEP' in str(elt.info):
                            return 'WEP'
                    return 'WEP'
        except Exception as e:
            logging.error(f"Error al determinar cifrado: {e}")
        return 'UNKNOWN'

    def check_wps(self, packet):
        """Verifica si la red tiene WPS activo."""
        try:
            for elt in packet[scapy.Dot11Elt]:
                if elt.ID == 221 and b'00:50:f2:04' in elt.info:  # Vendor-specific WPS
                    return True
        except Exception as e:
            logging.error(f"Error al verificar WPS: {e}")
        return False

    def analyze_vulnerabilities(self):
        """Analiza las redes detectadas para identificar vulnerabilidades."""
        self.vulnerabilities = []
        for network in self.networks:
            issues = []
            
            # 1. Red Wi-Fi abierta
            if network['encryption'] == 'OPEN':
                issues.append("Red abierta detectada (sin cifrado). Riesgo: Acceso no autorizado y MITM.")
            
            # 2. Uso de cifrado WEP
            if network['encryption'] == 'WEP':
                issues.append("Cifrado WEP detectado. Riesgo: Cifrado obsoleto, vulnerable a cracking.")
            
            # 3. WPS activo
            if network['wps']:
                issues.append("WPS activo detectado. Riesgo: Vulnerable a ataques de fuerza bruta.")
            
            # 4. Contraseñas débiles (simulación con Aircrack-ng, requiere captura previa)
            # Nota: Esto requiere un handshake capturado y un diccionario, no implementado aquí.
            
            if issues:
                self.vulnerabilities.append({
                    'ssid': network['ssid'],
                    'bssid': network['bssid'],
                    'issues': issues
                })

    def run_aircrack_wps_test(self, bssid, timeout=300):
        """Ejecuta una prueba de fuerza bruta en WPS usando Aircrack-ng (ejemplo)."""
        print(f"{YELLOW}[*] Probando vulnerabilidad WPS en {bssid}...{RESET}")
        try:
            cmd = ['sudo', 'reaver', '-i', self.interface, '-b', bssid, '-vv']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            if "WPS pin" in result.stdout:
                logging.info(f"WPS vulnerable detectado en {bssid}")
                print(f"{RED}[!] WPS vulnerable en {bssid}{RESET}")
                return True
        except subprocess.CalledProcessError as e:
            logging.error(f"Error en prueba WPS: {e}")
        return False

    def generate_report(self):
        """Genera un reporte con los resultados."""
        print("\n" + "="*50)
        print("REPORTE DE AUDITORÍA DE SEGURIDAD WI-FI")
        print("="*50)
        print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Interfaz utilizada: {self.interface}")
        print("\nVulnerabilidades detectadas:")
        
        if not self.vulnerabilities:
            print(f"{GREEN}[+] No se detectaron vulnerabilidades críticas.{RESET}")
        else:
            for vuln in self.vulnerabilities:
                print(f"\nRed: {vuln['ssid']} (BSSID: {vuln['bssid']})")
                for issue in vuln['issues']:
                    print(f"  - {RED}{issue}{RESET}")

        logging.info("Reporte generado correctamente.")

def main():
    interface = input("Ingrese la interfaz Wi-Fi (e.g., wlan0): ")
    auditor = WiFiAuditor(interface)
    
    # Configurar modo monitor
    auditor.set_monitor_mode()
    
    # Escanear redes
    auditor.scan_networks(duration=30)
    
    # Generar reporte
    auditor.generate_report()

if __name__ == "__main__":
    if os.geteuid() != 0:
        print(f"{RED}[-] Este script requiere permisos de root. Ejecute con sudo.{RESET}")
        exit(1)
    main()
