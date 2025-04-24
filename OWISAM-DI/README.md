# Owichan
 Open Wireless Security Assessment Methodology

# 🛡️ Owichan - Herramientas OWISAM para Auditoría Wi-Fi

Owichan es un conjunto de herramientas diseñadas para evaluar la seguridad de redes inalámbricas, basadas en la metodología **OWISAM** (Open Wireless Security Assessment Methodology). Este proyecto busca facilitar auditorías Wi-Fi mediante la automatización de controles y pruebas de seguridad, ayudando a identificar vulnerabilidades en infraestructuras inalámbricas.

# OWISAM-DI (Descubrimiento de dispositivos)

# Descripción
📌 Objetivo: Identificar dispositivos Wi-Fi en el entorno.
📌 Función: Capturar paquetes Beacon y Probe Request para detectar APs y clientes
conectados.
📌 Salida esperada: Lista de SSID, BSSID y clientes conectados.

# Requisitos

  1. SO: Linux (distribuciones basadas en Debian/Kali).
  2. Python ≥ 3.8
  3. Privilegios: root o sudo.
  4. Tarjeta Wi-Fi compatible con modo monitor.
     
# Instalación

  1. Clonar el repositorio:

   git clone https://github.com/CarlosBasulto/Owichan.git
     
  2. Crear entorno virtual (Opcional):
   
   python3 -m venv venv
   source venv/bin/activate
    
  3. Instalar dependencias:

   pip3 install scapy

# Uso

  1. Ponemos la interfaz modo monitor.
     
   sudo ip link set wlan0 down
   sudo iw dev wlan0 set type monitor
   sudo ip link set wlan0 up
   iwconfig  

  2. Ejecutar OWISAM-DI:

      sudo python3 owisam_di.py \
   --interface wlan0 \
   --output resultados.json \
   --wait-time 10

  3. Ver ayuda:

     python3 owisam_di.py -h
