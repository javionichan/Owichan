🛡️ Owichan - Auditoría de Seguridad Wi-Fi 📡
📝 Descripción
Owichan es un proyecto en Python diseñado para auditar redes Wi-Fi y detectar vulnerabilidades de seguridad comunes, como:

-🔓 Redes abiertas

-🔐 Cifrado WEP

-📶 WPS activo

-⚠️ Entre otras...

Este script utiliza herramientas como Scapy, Aircrack-ng y Wireshark/Tshark para analizar redes inalámbricas y generar reportes detallados.

-⚠️ Nota: Este proyecto es únicamente para fines educativos y auditorías autorizadas. El uso indebido puede violar leyes locales.

🚨 Vulnerabilidades Detectadas
El script identifica las siguientes vulnerabilidades:

-🔓 Redes Wi-Fi abiertas (sin cifrado)

-🔐 Uso de cifrado WEP (obsoleto y vulnerable)

-📶 WPS activo (vulnerable a ataques de fuerza bruta)

-🧩 Otras vulnerabilidades (como contraseñas débiles o autenticación insegura) pueden implementarse con módulos adicionales.

🧰 Tecnologías Utilizadas
-🐍 Python / Scapy: Captura y análisis de paquetes

-🛠️ Aircrack-ng: Pruebas de penetración (e.g., WPS)

-🔍 Wireshark / Tshark: Análisis de tráfico (opcional)

-💻 Bash: Comandos del sistema

📦 Requisitos
🐧 Sistema operativo Linux (Recomendado: Kali Linux o Ubuntu)

📡 Adaptador Wi-Fi en modo monitor (e.g., chipset Atheros, Ralink)

🔧 Dependencias:
sudo apt-get install aircrack-ng wireshark tshark python3-scapy
pip install scapy
-🔐 Permisos de root para ejecutar el script

⚙️ Instalación
Clona o descarga este repositorio:

git clone <URL_DEL_REPOSITORIO>
cd owichan
Asegúrate de tener las dependencias instaladas (ver Requisitos)

Dale permisos de ejecución al script:
chmod +x wifi_audit.py

▶️ Uso
Ejecuta el script con permisos de root:
sudo python3 wifi_audit.py
📥 Ingresa el nombre de la interfaz Wi-Fi (e.g., wlan0)
⏱️ El script escaneará redes durante 30 segundos
📄 Generará un reporte en consola y un archivo de log (wifi_audit.log)

📊 Ejemplo de Salida
==================================================
🛡️ REPORTE DE AUDITORÍA DE SEGURIDAD WI-FI 🛡️
==================================================
📅 Fecha: 2025-05-14 19:27:00  
📶 Interfaz utilizada: wlan0  

🔍 Vulnerabilidades detectadas:
📡 Red: Guest-WiFi (BSSID: 00:11:22:33:44:55)
  - 🔓 Red abierta detectada (sin cifrado)  
    ⚠️ Riesgo: Acceso no autorizado y MITM

📡 Red: OldRouter (BSSID: 00:66:77:88:99:AA)
  - 🔐 Cifrado WEP detectado  
  - ⚠️ Riesgo: Cifrado obsoleto, vulnerable a cracking
  - 📶 WPS activo detectado  
  - ⚠️ Riesgo: Vulnerable a ataques de fuerza bruta


