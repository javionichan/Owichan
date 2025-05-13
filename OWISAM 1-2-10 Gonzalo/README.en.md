
# 🛡️ WiFiOpenWEP

WiFiOpenWEP is a Wi-Fi auditing tool developed in Python for Linux distributions. Its main goal is to detect open or WEP-encrypted wireless networks, which are considered insecure according to modern security standards, including the OWISAM-TR-007 specification.

# 📌 Features

- WiFi network scanning in monitor mode.
- Detection of **open (OPN)** and WEP-encrypted networks.
- Report generation including BSSID, ESSID, channel, and encryption type.
- Support for adapters in monitor mode (e.g., `wlan0mon`).
- Suitable for use in security audits (e.g., `Kali Linux`).

# ⚙️ Requirements

- **Python 3.x**
- Kali Linux (or another distro with tools like `airodump-ng`)
- **Root privileges**
- Wi-Fi adapter compatible with **monitor mode**

# 🧪 Installation

Clone this repository:
```bash
git clone https://github.com/tuusuario/WiFiOpenWEP.git
cd WiFiOpenWEP
```

# 🛠️ Usage

**TR001-002 OWISAM.py**
Use the `-i` parameter to specify the interface you want to test (add `-t` to set the scan duration):
```bash
sudo python3 TR001-002 OWISAM.py -i <interface> [-t <scan_duration>]
```

**TR010.py**
As with the previous script, provide the name of the wireless interface:
```bash
sudo python3 TR010.py -i <interface>
```
