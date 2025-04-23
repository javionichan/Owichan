# Herramienta OWISAM-TR-004: Auditoría de Claves WEP/WPA/WPA2 Basada en Diccionario

Esta herramienta permite realizar auditorías de redes Wi-Fi para identificar debilidades en claves WEP, WPA y WPA2, mediante el uso de ataques de diccionario. Está diseñada para capturar handshakes y evaluar la fortaleza de las contraseñas, proporcionando resultados claros y recomendaciones para fortalecer la seguridad.

## **Características**

- Detección de redes Wi-Fi disponibles.
- Captura de paquetes y handshakes WPA/WPA2.
- Descifrado de claves utilizando un diccionario predefinido.
- Generación de reportes con resultados y recomendaciones de seguridad.

---

## **Plan de Desarrollo**

### **1. Objetivos**
- Detectar redes Wi-Fi disponibles y listar información básica (SSID, BSSID, cifrado).
- Capturar handshakes necesarios para el descifrado de claves WPA/WPA2.
- Intentar descifrar las claves usando un diccionario predefinido.
- Proveer recomendaciones de seguridad para las redes auditadas.

---

### **2. Herramientas Necesarias**

#### **Lenguaje**
- Python (por su amplia disponibilidad de librerías como `scapy` y `pyshark`).

#### **Librerías y Utilidades**
- `aircrack-ng` o `hashcat`: Para el descifrado de claves.
- `scapy` o `pyshark`: Para la captura y análisis de tráfico de red.

#### **Entorno**
- Adaptador Wi-Fi compatible con modo monitor.

---

