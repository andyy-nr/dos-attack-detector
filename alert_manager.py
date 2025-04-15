from datetime import datetime
import json
from typing import Callable
import os
"""
Alert Management System
Formats and routes alerts to GUI
"""

class AlertManager:
    def __init__(self, gui_handler: Callable,json_file: str = "alerts.json"):
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
        self.json_file = json_file
        self.alerts = self._load_alerts() #carga las existentes al iniciar 

    def _load_alerts(self):
        #carga desde el json
        if os.path.exists(self.json_file):
            with open (self.json_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []
    def _save_alerts(self):
        #guarda en el json
        with open(self.json_file, 'w') as f:
            json.dump(self.alerts, f, indent=2)

    def new_alert(self, alert_data: dict):
        """Format and forward alerts to GUI"""
        print(alert_data)
        details = {
        'rate': alert_data.get('rate', 0),
        'source_ip': alert_data.get('source_ip', 'N/A'),
        'severity': 'High' if alert_data.get('rate', 0) > 1000 else 'Medium'
            }   
        
        formatted = {
            'timestamp': datetime.now().isoformat(),
            'type': alert_data['type'],  # Asume que siempre existe
            'details': json.dumps(details)
            }

        self.alerts.append(formatted)
        self._save_alerts()
        # print("DEBUG NEW ALERT ADDED")
        self.gui_handler(formatted) # Forward to GUIç

    def last_two_alerts(self):
        """Return the last 2 alerts"""
        return self.alerts[-2:]