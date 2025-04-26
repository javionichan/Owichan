import socket
import dns.resolver
import requests
import subprocess
from scapy.all import *
from datetime import datetime
import threading

# ---------- CONFIGURACIÓN ----------
INTERFACE = "wlan0"  # Interfaz en modo monitor para sniffing
AUTHORIZED_BSSIDS = {
       "2c:96:82:88:55:d8" # Añade aquí añades tu BSSIDS , este es uno de ejemplo
}
sitios_web = ["www.google.es/index.html", "nmap.org/index.html", "www.eusa.es/index.html"]

# Guardar redes detectadas para no repetir
redes_detectadas = set()

# ---------- FUNCIONES PARA DOMINIOS ----------
def obtener_ip_legitima(dominio):   #Resuelve el dominio con DNS, para saber la IP oficial.
    try:
        dominio_base = dominio.split("/")[0]
        respuesta = dns.resolver.resolve(dominio_base, 'A')
        for ip in respuesta:
            return ip.to_text()
    except dns.exception.DNSException as e:
        print(f"⚠ Error al resolver {dominio}: {e}")
        return None

def obtener_ip_conectada(dominio):  #Resuelve el dominio usando socket, para ver a qué IP está conectado realmente tu PC.
    try:
        dominio_base = dominio.split("/")[0]
        ip = socket.gethostbyname(dominio_base)
        return ip
    except socket.gaierror:
        print(f"⚠ Error al obtener IP para {dominio}")
        return None

def comprobar_pagina(dominio):  #Verifica si una página está online
    try:
        response = requests.get(f"http://{dominio}", timeout=5)
        if response.status_code == 200:
            print(f"✅ La página {dominio} está accesible.")
        else:
            print(f"❌ La página {dominio} no está accesible (Código: {response.status_code}).")
    except requests.RequestException as e:
        print(f"⚠ Error al acceder a {dominio}: {e}")

def auditar_conexion(dominio):  #Junta todo eso, compara las IPs (para detectar si hay ataque tipo DNS spoofing).
    print(f"\n🔍 Comprobando {dominio}...")
    ip_legitima = obtener_ip_legitima(dominio)
    ip_conectada = obtener_ip_conectada(dominio)

    if ip_legitima and ip_conectada:
        if ip_legitima != ip_conectada:
            print(f"⚠ ¡ALERTA! IP legítima de {dominio} no coincide con la IP conectada ({ip_conectada}).")
        else:
            print(f"✅ {dominio} es seguro.")
            comprobar_pagina(dominio)
    else:
        print(f"⚠ No se pudo verificar la IP para {dominio}.")

def validar_urls(diccionario_urls):  #Audita un conjunto de dominios predefinidos.
    for url in diccionario_urls:
        auditar_conexion(url)

# ---------- FUNCIONES WI-FI (SNIFFING & ESCANEO) ----------
def escanear_redes_wifi():  #Usa nmcli para listar las redes Wi-Fi que detecta tu placa.
    try:
        result = subprocess.run(['nmcli', '-t', 'dev', 'wifi'], capture_output=True, text=True)
        print("\n🌐 Redes Wi-Fi disponibles:")
        print(result.stdout)
    except Exception as e:
        print(f"⚠ Error al escanear redes Wi-Fi: {e}")

def detectar_ap_no_autorizado(pkt):  #Escucha paquetes Wi-Fi. Si detecta una red que no está en tu lista blanca, avisa.
    if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
        bssid = pkt[Dot11].addr3
        ssid = pkt[Dot11Elt].info.decode(errors='ignore')
        if bssid not in AUTHORIZED_BSSIDS:
            if bssid not in redes_detectadas:
                print(f"[{datetime.now()}] ⚠ Red NO autorizada detectada: SSID='{ssid}' BSSID={bssid}")
                redes_detectadas.add(bssid)

def detectar_cliente_red_insegura(pkt):  # Escucha si algún cliente intenta conectarse a una red insegura.
    if pkt.haslayer(Dot11) and pkt.type == 0 and pkt.subtype == 0:
        client_mac = pkt[Dot11].addr1
        bssid = pkt[Dot11].addr2
        print(f"[{datetime.now()}] 🚨 Cliente {client_mac} intentando conectarse a red BSSID={bssid}")

def packet_handler(pkt):   # Maneja cada paquete recibido para analizarlo
    detectar_ap_no_autorizado(pkt)
    detectar_cliente_red_insegura(pkt)

def iniciar_sniffing(): # Inicia el proceso de sniffing
    print("🕵♂ Iniciando monitoreo Wi-Fi (sniffing)... Pulsa Ctrl+C para detener.")
    sniff(iface=INTERFACE, prn=packet_handler, store=0)

# ---------- MENÚ INTERACTIVO ----------
def menu():
    while True:
        print("\n-------- Menú --------")
        print("1. Escanear redes Wi-Fi disponibles")  #Escanea las redes
        print("2. Comprobar seguridad de un dominio") #Auditar un dominio.
        print("3. Validar varios dominios") #Auditar varios dominios.
        print("4. Monitorear Wi-Fi (Redes no autorizadas y conexiones inseguras)") #Monitorear redes en vivo
        print("5. Salir") #Salir

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            escanear_redes_wifi()
        elif opcion == '2':
            dominio = input("Introduce el dominio (ej. www.google.es): ")
            auditar_conexion(dominio)
        elif opcion == '3':
            validar_urls(sitios_web)
        elif opcion == '4':
            try:
                sniff_thread = threading.Thread(target=iniciar_sniffing)
                sniff_thread.start()
            except KeyboardInterrupt:
                print("\n🛑 Sniffing detenido.")
        elif opcion == '5':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠ Opción inválida.")

# ---------- EJECUCIÓN PRINCIPAL ----------
if __name__ == "__main__":
    menu()
