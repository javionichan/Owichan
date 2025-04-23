#!/usr/bin/env python3
import argparse, csv, json
from datetime import datetime
from scapy.all import sniff, Dot11, Dot11Beacon, Dot11ProbeResp, Dot11Elt

devices = {}

def get_channel(pkt):
    ch_elem = pkt.getlayer(Dot11Elt, ID=3)
    return ch_elem.info[0] if ch_elem and ch_elem.info else ""

def get_encryption(pkt):
    if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
        cap = pkt.sprintf("{Dot11Beacon:%Dot11Beacon.cap%}").split('+')
        if "privacy" not in cap:
            return "Abierta"
        elif pkt.getlayer(Dot11Elt, ID=48):
            return "WPA2/WPA3"
        elif pkt.getlayer(Dot11Elt, ID=221):
            return "WPA"
        else:
            return "WEP"
    return "Desconocido"

def packet_handler(pkt):
    if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
        bssid = pkt[Dot11].addr2.upper()
        ssid = pkt[Dot11Elt].info.decode(errors="ignore") or "<oculto>"
        rssi = pkt.dBm_AntSignal
        channel = get_channel(pkt)
        encryption = get_encryption(pkt)
        devices[bssid] = {
            "ssid": ssid,
            "channel": channel,
            "encryption": encryption,
            "rssi": rssi
        }

def run(interface, timeout, output):
    print(f"[+] Capturando en {interface} durante {timeout}s...")
    sniff(iface=interface, prn=packet_handler, timeout=timeout, store=False)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_file = output or f"owisam_fp_{ts}.csv"
    json_file = output or f"owisam_fp_{ts}.json"

    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["bssid", "ssid", "channel", "encryption", "rssi"])
        writer.writeheader()
        for bssid, data in devices.items():
            writer.writerow({"bssid": bssid, **data})

    with open(json_file, "w") as f:
        json.dump(devices, f, indent=2)

    print(f"[+] Guardado: {csv_file}, {json_file}")
    print(f"[+] Total APs detectados: {len(devices)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", required=True, help="Interfaz WiFi en modo monitor")
    parser.add_argument("-t", "--timeout", type=int, default=60, help="Duración de la captura (segundos)")
    parser.add_argument("-o", "--output", help="Prefijo del nombre del archivo de salida")
    args = parser.parse_args()
    run(args.interface, args.timeout, args.output)
