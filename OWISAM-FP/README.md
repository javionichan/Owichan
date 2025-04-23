# OWISAM-FP

Herramienta OWISAM-FP para fingerprinting Wi-Fi desarrollada en Python como parte del módulo Hacking Ético del GS de Ciberseguridad.

OWISAM-FP es una herramienta desarrollada en Python para la detección de redes Wi-Fi y la recopilación de información básica sobre ellas. Permite identificar redes inalámbricas cercanas, mostrando datos como:

- Nombre de la red (SSID)
- Dirección del punto de acceso (BSSID)
- Canal utilizado
- Tipo de cifrado (Abierta, WPA/WPA2/WPA3)
- Potencia de señal (RSSI)

Al finalizar el escaneo, la herramienta genera automáticamente dos archivos con los resultados:

- **CSV:** para visualización rápida en tablas
- **JSON:** para procesamiento automatizado y análisis estructurado

Esta herramienta forma parte de la metodología **OWISAM (Open Wireless Security Assessment Methodology)** y cumple con el control **OWISAM-M-FP (Fingerprinting)**.

## ✅ Pasos completos para usar la herramienta sin errores

```bash
# 1. Crear entorno virtual y activarlo
python3 -m venv env
source env/bin/activate

# 2. Instalar dependencias
pip install scapy
sudo apt install net-tools -y  # para usar iwconfig

# 3. Preparar interfaz Wi-Fi en modo monitor (ejemplo con wlan0)
sudo airmon-ng check kill
sudo ip link set wlan0 down
sudo iw wlan0 set monitor control
sudo ip link set wlan0 up
iwconfig   # debe decir Mode:Monitor

# 4. Ejecutar la herramienta
sudo python3 fingerprinting.py -i wlan0 -t 120
