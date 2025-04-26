# Herramienta OWISAM-TR-001-007-009: WiGuard Auditoría de Seguridad Wi-Fi y DNS

WiGuard es una herramienta desarrollada en Python para sistemas Kali Linux, diseñada con el objetivo de detectar redes Wi-Fi no autorizadas y clientes que intentan conectarse a redes inseguras, así como verificar la integridad de las conexiones DNS y prevenir ataques de tipo DNS Spoofing.

Esta utilidad integra análisis de red inalámbrica en tiempo real con auditorías de dominios, proporcionando un entorno robusto para la validación de seguridad en entornos corporativos o educativos.

## **Características**

- Detección de redes Wi-Fi disponibles desde terminal.

- Monitoreo pasivo de redes Wi-Fi para identificar:

- Redes no autorizadas (OWISAM-TR-007)

- Conexiones de clientes a redes inseguras o falsas (OWISAM-TR-009)

- Verificación de integridad DNS:

- Comparación entre IP legítima y la IP a la que se está conectando un dominio.

- Análisis de accesibilidad web (código HTTP).

- Interfaz de menú interactivo para facilitar el uso.

- Preparado para entornos con adaptadores en modo monitor (ej. wlan0mon).

---

## **Plan de Desarrollo**

### **Objetivos**
- Detectar SSID/BSSID disponibles y mostrar datos relevantes para auditorías.

- Analizar tráfico inalámbrico en tiempo real para detectar redes no autorizadas y actividad sospechosa de clientes.

- Validar dominios mediante comparación de IP legítima y activa.

- Proveer una herramienta todo-en-uno para la validación OWISAM-TR-001, OWISAM-TR-007 y OWISAM-TR-009.

---

### **Herramientas Necesarias**

#### **Lenguaje**
- Python3.

#### **Librerías y Utilidades**
`scapy`: Captura y análisis de paquetes 802.11

`dns.resolver`: Resolución de dominios

`requests`: Verificación de accesibilidad web

`socket`: Resolución DNS a nivel de sistema

#### **Entorno**
- Kali Linux

- Adaptador Wi-Fi compatible con modo monitor

- Acceso root para sniffing de red

---
