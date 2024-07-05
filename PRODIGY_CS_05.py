from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
import os
import sys


# Function to process each packet
def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"IP Packet: {ip_layer.src} -> {ip_layer.dst}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"TCP Packet: {ip_layer.src}:{tcp_layer.sport} -> {ip_layer.dst}:{tcp_layer.dport}")
            print(f"Payload: {str(bytes(packet[TCP].payload))}")

        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"UDP Packet: {ip_layer.src}:{udp_layer.sport} -> {ip_layer.dst}:{udp_layer.dport}")
            print(f"Payload: {str(bytes(packet[UDP].payload))}")


# Function to start sniffing
def start_sniffing(interface):
    print(f"Starting packet sniffing on interface {interface}")
    try:
        sniff(iface=interface, prn=process_packet, store=False)
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure Npcap is installed and you have the necessary permissions.")


# Ensure the script is run with administrative privileges on Windows
if os.name == 'nt':
    # Check if Npcap is installed
    npcap_installed = 'npcap' in os.popen('sc query npcap').read().lower()
    if not npcap_installed:
        print("Npcap is not installed or not running. Please install it from https://nmap.org/npcap/")
        sys.exit(1)

# Specify the network interface
network_interface = "Wi-Fi"  # Replace with your network interface

# Start sniffing
start_sniffing(network_interface)