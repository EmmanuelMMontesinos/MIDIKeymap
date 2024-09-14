# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QKeySequenceEdit, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(578, 556)
        self.action_configuracion = QAction(MainWindow)
        self.action_configuracion.setObjectName(u"action_configuracion")
        self.action_Info = QAction(MainWindow)
        self.action_Info.setObjectName(u"action_Info")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.box_pads_2 = QGroupBox(self.centralwidget)
        self.box_pads_2.setObjectName(u"box_pads_2")
        self.box_pads_2.setGeometry(QRect(200, 180, 181, 321))
        self.box_cc = QGroupBox(self.centralwidget)
        self.box_cc.setObjectName(u"box_cc")
        self.box_cc.setGeometry(QRect(390, 180, 181, 321))
        self.box_keys = QGroupBox(self.centralwidget)
        self.box_keys.setObjectName(u"box_keys")
        self.box_keys.setGeometry(QRect(10, 180, 181, 321))
        self.box_keys.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 561, 131))
        self.boton_detectar = QPushButton(self.groupBox)
        self.boton_detectar.setObjectName(u"boton_detectar")
        self.boton_detectar.setGeometry(QRect(130, 90, 141, 24))
        self.boton_detectar.setStyleSheet(u"")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 90, 251, 24))
        self.input_status = QLineEdit(self.groupBox)
        self.input_status.setObjectName(u"input_status")
        self.input_status.setGeometry(QRect(200, 30, 61, 21))
        self.input_key = QLineEdit(self.groupBox)
        self.input_key.setObjectName(u"input_key")
        self.input_key.setGeometry(QRect(200, 60, 61, 21))
        self.input_nombre = QLineEdit(self.groupBox)
        self.input_nombre.setObjectName(u"input_nombre")
        self.input_nombre.setGeometry(QRect(400, 30, 141, 21))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 30, 41, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 60, 41, 16))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 101, 16))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 30, 101, 16))
        self.input_atajo = QKeySequenceEdit(self.groupBox)
        self.input_atajo.setObjectName(u"input_atajo")
        self.input_atajo.setGeometry(QRect(400, 60, 141, 21))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 60, 101, 20))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 70, 91, 16))
        font = QFont()
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 50, 91, 16))
        self.label_7.setFont(font)
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 90, 91, 16))
        self.label_8.setFont(font)
        self.led_cc = QLCDNumber(self.centralwidget)
        self.led_cc.setObjectName(u"led_cc")
        self.led_cc.setGeometry(QRect(450, 160, 64, 23))
        self.led_cc.setStyleSheet(u"background:#0af;")
        self.led_pads = QLCDNumber(self.centralwidget)
        self.led_pads.setObjectName(u"led_pads")
        self.led_pads.setGeometry(QRect(260, 160, 64, 23))
        self.led_pads.setStyleSheet(u"background:yellow;")
        self.led_keys = QLCDNumber(self.centralwidget)
        self.led_keys.setObjectName(u"led_keys")
        self.led_keys.setGeometry(QRect(70, 160, 64, 23))
        self.led_keys.setStyleSheet(u"background: #0f2;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 578, 33))
        self.menu_opciones = QMenu(self.menubar)
        self.menu_opciones.setObjectName(u"menu_opciones")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_opciones.menuAction())
        self.menu_opciones.addAction(self.action_configuracion)
        self.menu_opciones.addAction(self.action_Info)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MIDIKeymap", None))
        self.action_configuracion.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.action_Info.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.box_pads_2.setTitle(QCoreApplication.translate("MainWindow", u"Pads", None))
        self.box_cc.setTitle(QCoreApplication.translate("MainWindow", u"CC", None))
        self.box_keys.setTitle(QCoreApplication.translate("MainWindow", u"Keys", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Agregar Atajo MIDI", None))
        self.boton_detectar.setText(QCoreApplication.translate("MainWindow", u"Detectar MIDI", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.input_status.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.input_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key/ID", None))
        self.input_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Key/ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Codigos de Status:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nombre del Atajo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tecla/Combinaci\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"144 - Tecla Piano", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"137 - Pad", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"176 - Slider / Dial", None))
        self.menu_opciones.setTitle(QCoreApplication.translate("MainWindow", u"Opciones", None))
    # retranslateUi

