# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(762, 500)
        MainWindow.setMinimumSize(QSize(762, 500))
        MainWindow.setMaximumSize(QSize(762, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.image_lbl = QLabel(self.centralwidget)
        self.image_lbl.setObjectName(u"image_lbl")
        self.image_lbl.setGeometry(QRect(10, 10, 91, 71))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 181, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.status_lbl = QLabel(self.centralwidget)
        self.status_lbl.setObjectName(u"status_lbl")
        self.status_lbl.setGeometry(QRect(120, 50, 491, 31))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 90, 281, 351))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(1000, 60))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.alert1_gb = QGroupBox(self.verticalLayoutWidget)
        self.alert1_gb.setObjectName(u"alert1_gb")
        self.label_6 = QLabel(self.alert1_gb)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 30, 171, 20))
        self.alert1_btn = QPushButton(self.alert1_gb)
        self.alert1_btn.setObjectName(u"alert1_btn")
        self.alert1_btn.setGeometry(QRect(100, 50, 83, 29))

        self.verticalLayout.addWidget(self.alert1_gb)

        self.alert2_gb = QGroupBox(self.verticalLayoutWidget)
        self.alert2_gb.setObjectName(u"alert2_gb")
        self.label_5 = QLabel(self.alert2_gb)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 171, 20))
        self.alert2_btn = QPushButton(self.alert2_gb)
        self.alert2_btn.setObjectName(u"alert2_btn")
        self.alert2_btn.setGeometry(QRect(100, 50, 83, 29))

        self.verticalLayout.addWidget(self.alert2_gb)

        self.alert3_gb = QGroupBox(self.verticalLayoutWidget)
        self.alert3_gb.setObjectName(u"alert3_gb")
        self.label_2 = QLabel(self.alert3_gb)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 171, 20))
        self.alert3_btn = QPushButton(self.alert3_gb)
        self.alert3_btn.setObjectName(u"alert3_btn")
        self.alert3_btn.setGeometry(QRect(100, 50, 83, 29))

        self.verticalLayout.addWidget(self.alert3_gb)

        self.activealerts_lbl = QLabel(self.centralwidget)
        self.activealerts_lbl.setObjectName(u"activealerts_lbl")
        self.activealerts_lbl.setGeometry(QRect(300, 150, 279, 60))
        self.activealerts_lbl.setMaximumSize(QSize(1000, 60))
        self.activealerts_lbl.setFont(font1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 210, 441, 60))
        self.label_8.setMaximumSize(QSize(1000, 60))
        self.label_8.setFont(font1)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(300, 270, 451, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)

        self.inbandwith_lbl = QLabel(self.gridLayoutWidget)
        self.inbandwith_lbl.setObjectName(u"inbandwith_lbl")
        font3 = QFont()
        font3.setPointSize(12)
        self.inbandwith_lbl.setFont(font3)
        self.inbandwith_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.inbandwith_lbl, 1, 0, 1, 1)

        self.outbandwith_lbl = QLabel(self.gridLayoutWidget)
        self.outbandwith_lbl.setObjectName(u"outbandwith_lbl")
        self.outbandwith_lbl.setFont(font3)
        self.outbandwith_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.outbandwith_lbl, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 762, 33))
        self.menuDashboard = QMenu(self.menuBar)
        self.menuDashboard.setObjectName(u"menuDashboard")
        self.menuAlerts = QMenu(self.menuBar)
        self.menuAlerts.setObjectName(u"menuAlerts")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuDashboard.menuAction())
        self.menuBar.addAction(self.menuAlerts.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image_lbl.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current status", None))
        self.status_lbl.setText(QCoreApplication.translate("MainWindow", u"More status info", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Last alerts", None))
        self.alert1_gb.setTitle(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Lasted X minutes", None))
        self.alert1_btn.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.alert2_gb.setTitle(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Lasted X minutes", None))
        self.alert2_btn.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.alert3_gb.setTitle(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Lasted X minutes", None))
        self.alert3_btn.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.activealerts_lbl.setText(QCoreApplication.translate("MainWindow", u"Active alerts:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Current bandwith usage", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"In", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Out", None))
        self.inbandwith_lbl.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.outbandwith_lbl.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menuDashboard.setTitle(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.menuAlerts.setTitle(QCoreApplication.translate("MainWindow", u"Alerts", None))
    # retranslateUi

