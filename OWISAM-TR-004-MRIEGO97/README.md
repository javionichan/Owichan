# Herramienta OWISAM-TR-004: Auditoría de Claves WEP/WPA/WPA2 Basada en Diccionario
**Kit de Herramientas para Pruebas de Penetración Wi-Fi**

Este repositorio contiene un conjunto de scripts en Python diseñados para automatizar tareas de pruebas de penetración Wi-Fi. El kit de herramientas es modular e incluye scripts para escanear redes, capturar paquetes, realizar ataques de desautenticación y crackear contraseñas Wi-Fi.

## **Características**

- Escaneo de redes Wi-Fi cercanas: Identificar redes objetivo y sus detalles (BSSID, canal, etc.)
- Captura de paquetes y handshakes WPA/WPA2.
- Ataque de desautenticación: Forzar la desconexión de dispositivos de una red objetivo, facilitando la captura de paquetes.
- Crackeo de contraseñas: Crackear contraseñas Wi-Fi utilizando los paquetes de handshake capturados y una lista de palabras.

---

## **Requisitos**

- Sistema operativo basado en Linux (por ejemplo, Kali Linux).
- Python 3.x.
- Suite Aircrack-ng (airmon-ng, airodump-ng, aireplay-ng, aircrack-ng).
- Adaptador de red inalámbrica capaz de operar en modo monitor

---

### **Instalacion**
1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/...
    ```

2. **Asegúrate de que los scripts sean ejecutables:**

    ```bash
    cd ...
    chmod +x 1scan.py 2deauth.py 3crack.py
    ```

---
### **Uso** 

1. Escanear y Capturar Paquetes

  Ejecuta el script `1scan.py` para escanear redes Wi-Fi cercanas y capturar paquetes de handshake:

  ```bash
  sudo python3 1scan.py
  ```

2. Realizar un Ataque de Desautenticación
  ```bash
  sudo python3 2deauth.py
  ```
  Ingresa el BSSID de la red objetivo cuando se te indique

3. Descifrar la Contraseña
  ```bash
  sudo python3 3crack.py
  ```
  Ingresa el nombre del archivo de captura (sin la extensión .cap) y la ruta a la lista de palabras
