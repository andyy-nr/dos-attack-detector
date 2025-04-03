from scapy.all import sniff, IP 
import time 
from typing import Callable 

class DoSDetector:
    def __init__(self, alert_callback: Callable [[dict], None]):
        self.alert_callback = alert_callback
        self.packet_counts ={
            'total':0,
            'syn': 0,
            'udp':0
        }
        self.last_check= time.time()
    def start (self, interface: str=None):
        #Start monitoring nw traffic 
        sniff(prn=self._analyze_packet,
              iface=interface
              store=false)
        
        