# -*- coding: utf-8 -*-
import sys
import threading

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from gui.dashboard import Ui_MainWindow
from detector import DoSDetector
from alert_manager import AlertManager
from network import BandwidthMonitor
import json

class BandwidthData:
    def __init__(self):
        self.download = 0.0
        self.upload = 0.0

    def update(self, data: dict):
        self.download = data['in']
        self.upload = data['out']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.bandwidthData = BandwidthData()
        self.bandwidthAnalysis = BandwidthMonitor(self.bandwidthData.update)
        self.alert_manager = AlertManager(lambda alert: self.update_alerts(alert))
        self.detector = DoSDetector(self.alert_manager.new_alert)

        self.start_backend()

        self.bandwidth_timer = QTimer()
        self.bandwidth_timer.timeout.connect(self.update_gui_bandwidth)
        self.bandwidth_timer.start(1000)

        self.update_alerts(alert=None)

    def start_backend(self):
        # Start detector
        threading.Thread(
            target=self.detector.start,
            daemon=True
        ).start()

        # Start bandwidth monitor
        threading.Thread(
            target=self.bandwidthAnalysis.start,
            daemon=True
        ).start()

    def update_gui_bandwidth(self):
        self.ui.inbandwith_lbl.setText(str(self.bandwidthData.download))
        self.ui.outbandwith_lbl.setText(str(self.bandwidthData.upload))

    def update_dashboards_alerts(self):
        last_alerts = self.alert_manager.last_two_alerts()

        self.ui.label_6.setText("No alert")
        self.ui.label_5.setText("No alert")

        self.ui.alert1_gb.setTitle(" ")
        self.ui.alert2_gb.setTitle(" ")

        labels = [self.ui.label_6, self.ui.label_5]
        groupboxes = [self.ui.alert1_gb, self.ui.alert2_gb]

        for i, alert in enumerate(last_alerts):
            try:
                details = json.loads(alert.get("details", "{}")) or {}
                message = details.get("message") or "No message"
                severity = details.get("severity") or "N/A"
                timestamp = alert.get("timestamp", "Unknown time")

                labels[i].setText(f"{message} | Severity: {severity}")
                groupboxes[i].setTitle(timestamp)
            except Exception as e:
                labels[i].setText(f"Error: {e}")
                groupboxes[i].setTitle(" ")


    def populate_table(self, alerts: list):
        self.ui.alerts_table.setColumnCount(4)
        self.ui.alerts_table.setHorizontalHeaderLabels(["Timestamp", "Type", "Message", "Severity"])

        self.ui.alerts_table.setRowCount(len(alerts))
        for row, alert in enumerate(alerts):
            details = json.loads(alert["details"])

            self.ui.alerts_table.setItem(row, 0, QTableWidgetItem(alert["timestamp"]))
            self.ui.alerts_table.setItem(row, 1, QTableWidgetItem(alert["type"]))
            self.ui.alerts_table.setItem(row, 2, QTableWidgetItem(details.get("Message", "N/A")))
            self.ui.alerts_table.setItem(row, 3, QTableWidgetItem(details.get("severity", "N/A")))

    def update_alerts(self, alert):
        self.populate_table(self.alert_manager.alerts)
        self.update_dashboards_alerts()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
