from scapy.all import sniff, IP ,TCP,UDP
import time 
from typing import Callable 
"""
DoS Detection Engine
Handles packet analysis and attack detection
"""
class DoSDetector:
    def __init__(self, alert_callback: Callable [[dict], None]):
        """
        Initialize detector with alert callback
        
        Args:
            alert_callback: Function that receives alert dicts with format:
                {
                    'type': str (attack type),
                    'rate': int (packets/sec),
                    'timestamp': float
                }
        """
        self.alert_callback = alert_callback
        self.packet_counts ={
            'total':0, #todous
            'syn': 0, #SYN packets for syn floods 
            'udp':0 # for udp floods 
        }
        self.last_check= time.time()

    def start (self, interface: str=None):
        """Start monitoring nw traffic 
        Args:
            interface: Network interface to monitor (None for default)
            
        Note: RUN INDEFINIDAMENTE ASI QUE HAY QUE TERMINAR EL PROGRAMA
        """
        sniff(prn=self._analyze_packet,
              iface=interface,
              store=False)
        
        
    def _analyze_packet(self,packet):
        """ Process each incoming packet """
        self.packet_counts['total'] +=1

        if IP in packet:
            if TCP in packet and packet[TCP].flags =='S': #SYN flag
                self.packet_counts['syn'] +=1
                #UDP flood detection
            elif UDP in packet:
                self.packet_counts['udp']+=1

            #Threshold checks every second 
            if time.time() - self.last_check >= 1.0:
                self._check_thresholds()
                self.last_check = time.time()

    def _check_thresholds(self):
        """Evaluate traffic against attack thresholds
            Triggers alerts when thresholds exceeded
        """
        if self.packet_counts['total'] > 1000:  # Example threshold
            self.alert_callback({
                'type': 'HIGH_TRAFFIC',
                'rate': self.packet_counts['total'],
                'timestamp': time.time()
            })
        
        # Reset counters
        self.packet_counts = {k: 0 for k in self.packet_counts}