
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

