#import sys
#from scapy.all import *  
from scapy.layers.dot11 import Dot11
from scapy.sendrecv import sniff

IFACE_NAME = "Intel(R) Wi-Fi 6 AX201 160MHz"
devices = set() 
def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        dot11_layer = pkt.getlayer(Dot11)
          
        if dot11_layer.addr2 and (dot11_layer.addr2 not in devices):
            devices.add(dot11_layer.addr2)
            print(len(devices), dot11_layer.addr2, dot11_layer.payload.name)
  
  
sniff( count=1, prn=PacketHandler )


  
  
