import subprocess
import time
import argparse
import os
import signal

def activar_monitor(interfaz):
    print(f"Activando modo monitor en {interfaz}...")
    subprocess.run(["ip", "link", "set", interfaz, "down"])
    subprocess.run(["iw", interfaz, "set", "monitor", "none"])
    subprocess.run(["ip", "link", "set", interfaz, "up"])

def restaurar_interfaz(interfaz):
    print(f"\n Restaurando {interfaz} a modo managed...")
    subprocess.run(["ip", "link", "set", interfaz, "down"])
    subprocess.run(["iw", interfaz, "set", "type", "managed"])
    subprocess.run(["ip", "link", "set", interfaz, "up"])

def escanear_redes(interfaz):
    archivo_base = "/tmp/redes_scan"
    for f in os.listdir('/tmp'):
        if f.startswith("redes_scan"):
            os.remove(os.path.join('/tmp', f))

    comando = [
        "airodump-ng",
        "--output-format", "csv",
        "-w", archivo_base,
        interfaz
    ]

    proceso = subprocess.Popen(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)
    proceso.send_signal(signal.SIGINT)
    time.sleep(1)

    archivo_csv = archivo_base + "-01.csv"
    if not os.path.exists(archivo_csv):
        print("No se generó el archivo CSV.")
        return {}

    return procesar_csv(archivo_csv)

def procesar_csv(ruta):
    redes = {}
    with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
        lineas = f.readlines()

    for linea in lineas:
        if "Station MAC" in linea:
            break
        partes = linea.strip().split(",")
        if len(partes) >= 14 and "BSSID" not in partes[0]:
            ssid = partes[13].strip() or "OCULTA"
            try:
                signal = int(partes[8].strip())
                redes[ssid] = signal
            except:
                continue
    return redes

def imprimir_grafico(datos):
    os.system('clear')
    print("Intensidad de señal Wi-Fi:\n")
    for ssid, signal in sorted(datos.items(), key=lambda x: x[1], reverse=True):
        barras = '█' * max(0, int((100 + signal) / 2))
        print(f"{ssid:<30} | {signal:>4} dBm | {barras}")
    print("\nPulsa Ctrl+C para salir.")

def main():
    parser = argparse.ArgumentParser(description="Monitor Wi-Fi en terminal.")
    parser.add_argument("-i", "--interface", required=True, help="Interfaz de red (ej: wlan0)")
    args = parser.parse_args()
    interfaz = args.interface

    try:
        activar_monitor(interfaz)
        while True:
            redes = escanear_redes(interfaz)
            if redes:
                imprimir_grafico(redes)
            else:
                print("No se detectaron redes.")
            time.sleep(3)
    except KeyboardInterrupt:
        pass
    finally:
        restaurar_interfaz(interfaz)
        print("Saliste del script.")

if __name__ == "__main__":
    main()
