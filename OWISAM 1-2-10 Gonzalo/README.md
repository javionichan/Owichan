
# 🛡️ WiFiOpenWEP

WiFiOpenWEP es una herramienta de auditoría Wi-Fi desarrollada en Python para distribuciones Linux. Su objetivo principal es detectar redes inalámbricas abiertas o cifradas con WEP, consideradas vulnerables según estándares de seguridad, incluyendo la norma OWISAM-TR-007

# 📌 Características

- Escaneo de redes Wi-Fi en modo monitor.
- Detección de redes **abiertas (OPN)** y con cifrado **WEP**.
- Generación de reporte con BSSID, ESSID, canal y tipo de cifrado.
- Soporte para adaptadores en modo monitor (ej. `wlan0mon`).
- Preparado para su uso en auditorías de seguridad (Kali Linux).

# ⚙️ Requisitos

- **Python 3.x**
- **Kali Linux** (u otra distro con herramientas como `airodump-ng`)
- Permisos de **root**
- Adaptador Wi-Fi compatible con **modo monitor**

# 🧪 Instalación

Clona este repositorio:
```bash
git clone https://github.com/tuusuario/WiFiOpenWEP.git
cd WiFiOpenWEP
```

# 🛠️ Modo de Empleo

**TR001-002 OWISAM.py**
Pasaremos el parámetro -i para especificar la interfaz en la que queremos realizar las pruebas (añade `-t` si deseas especificar el tiempo).
```bash
sudo python3 TR001-002 OWISAM.py -i <interfaz> [-t <tiempo_de_escaneo>]
```

**TR010.py**
Al igual que con el script anterior, añadimos la información de la interfaz de red.
```bash
sudo python3 TR010.py -i <interfaz>
```


Creado por: Antonio Rodríguez Vázquez, Gonzalo López-Escobar García, Alejandro Pérez Fuentes
