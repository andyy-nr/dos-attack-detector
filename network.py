import psutil
import time
from typing import Callable
"""
Network Bandwidth Monitor
Tracks real-time bandwidth usage
"""

class BandwidthMonitor:
    def __init__(self, update_callback: Callable[[dict], None], interval: float = 1.0):
        """     Initialize bandwidth monitor
        
        Args:
            update_callback: Receives dicts with format:
                {'in': float, 'out': float} # Mbps
            interval: Update frequency in seconds"""
        self.update_callback = update_callback
        self.interval = interval
        
    def start(self):
        """Start monitoring bandwidth"""
        last_io = psutil.net_io_counters()
        while True:
            time.sleep(self.interval)
            current_io = psutil.net_io_counters()
            # Calculate Mbps (bytes→bits, per second)
            in_mbps = (current_io.bytes_recv - last_io.bytes_recv) * 8 / 1_000_000 / self.interval
            out_mbps = (current_io.bytes_sent - last_io.bytes_sent) * 8 / 1_000_000 / self.interval
            
            self.update_callback({
                'in': round(in_mbps, 2),
                'out': round(out_mbps, 2)
            })
            
            last_io = current_io