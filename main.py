# -*- coding: utf-8 -*-
import sys
import threading

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QApplication

from gui.dashboard import Ui_MainWindow
from detector import DoSDetector
from alert_manager import AlertManager
from network import BandwidthMonitor

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
        self.alert_manager = AlertManager(self.update_gui_alerts)
        self.detector = DoSDetector(self.alert_manager.new_alert)

        self.start_backend()

        self.bandwidth_timer = QTimer()
        self.bandwidth_timer.timeout.connect(self.update_gui_bandwidth)
        self.bandwidth_timer.start(1000)


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

    def update_gui_alerts(self):
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
