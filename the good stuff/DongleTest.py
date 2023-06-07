#import sys
#from scapy.all import *  
from scapy.layers.dot11 import Dot11
from scapy.sendrecv import sniff

IFACE_NAME = "RTL8188ETV Wireless LAN 802.11n Network Adapter"
devices = set() 
def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        dot11_layer = pkt.getlayer(Dot11)
          
        if dot11_layer.addr2 and (dot11_layer.addr2 not in devices):
            devices.add(dot11_layer.addr2)
            print(len(devices), dot11_layer.addr2, dot11_layer.payload.name)
  
  
sniff(iface=IFACE_NAME, count=10, prn=PacketHandler )