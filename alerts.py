from PySide6.QtWidgets import QWidget, QTableWidgetItem
from gui.alerts import Ui_Form
import json

class AlertsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Set up table headers
        self.ui.alerts_table.setColumnCount(4)
        self.ui.alerts_table.setHorizontalHeaderLabels(["Timestamp", "Type", "Source IP", "Severity"])

    def populate_table(self, alerts: list):
        self.ui.alerts_table.setRowCount(len(alerts))
        for row, alert in enumerate(alerts):
            details = json.loads(alert["details"])

            self.ui.alerts_table.setItem(row, 0, QTableWidgetItem(alert["timestamp"]))
            self.ui.alerts_table.setItem(row, 1, QTableWidgetItem(alert["type"]))
            self.ui.alerts_table.setItem(row, 2, QTableWidgetItem(details.get("source_ip", "N/A")))
            self.ui.alerts_table.setItem(row, 3, QTableWidgetItem(details.get("severity", "N/A")))