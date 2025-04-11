# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alerts.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(762, 500)
        Form.setMinimumSize(QSize(762, 500))
        Form.setMaximumSize(QSize(762, 500))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 131, 31))
        self.time_range_cb = QComboBox(Form)
        self.time_range_cb.setObjectName(u"time_range_cb")
        self.time_range_cb.setGeometry(QRect(110, 30, 231, 28))
        self.type_cb = QComboBox(Form)
        self.type_cb.setObjectName(u"type_cb")
        self.type_cb.setGeometry(QRect(110, 80, 231, 28))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 91, 31))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 30, 131, 31))
        self.ip_le = QLineEdit(Form)
        self.ip_le.setObjectName(u"ip_le")
        self.ip_le.setGeometry(QRect(460, 30, 231, 28))
        self.filter_btn = QPushButton(Form)
        self.filter_btn.setObjectName(u"filter_btn")
        self.filter_btn.setGeometry(QRect(530, 70, 81, 31))
        self.alerts_table = QTableWidget(Form)
        self.alerts_table.setObjectName(u"alerts_table")
        self.alerts_table.setGeometry(QRect(20, 130, 721, 351))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Time range", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Type", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Lookup IP", None))
        self.filter_btn.setText(QCoreApplication.translate("Form", u"Search alert", None))
    # retranslateUi

