from datetime import datetime
import json
from typing import Callable
"""
Alert Management System
Formats and routes alerts to GUI
"""

class AlertManager:
    def __init__(self, gui_handler: Callable):
        """
        Initialize with GUI callback function
        
        Args:
            gui_handler: Function that receives formatted alerts:
                {
                    'timestamp': str (ISO format),
                    'type': str,
                    'details': str (JSON)
                }
        """
        self.gui_handler = gui_handler
        self.alerts = []
        
    def new_alert(self, alert_data: dict):
        """Format and forward alerts to GUI"""
        formatted = {
            'timestamp': datetime.now().isoformat(),
            'type': alert_data.get('type'),
            'details': json.dumps(alert_data) # Serialize for GUI
        }
        self.alerts.append(formatted)
        self.gui_handler(formatted) # Forward to GUI
        