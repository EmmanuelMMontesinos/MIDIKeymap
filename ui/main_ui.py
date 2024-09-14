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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QKeySequenceEdit,
    QLCDNumber, QLineEdit, QMainWindow, QMenu,
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
        self.groupBox.setGeometry(QRect(10, 0, 561, 141))
        self.boton_detectar = QPushButton(self.groupBox)
        self.boton_detectar.setObjectName(u"boton_detectar")
        self.boton_detectar.setGeometry(QRect(390, 40, 141, 24))
        self.boton_detectar.setStyleSheet(u"")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 110, 171, 24))
        self.input_status = QLineEdit(self.groupBox)
        self.input_status.setObjectName(u"input_status")
        self.input_status.setGeometry(QRect(30, 40, 81, 21))
        self.input_key = QLineEdit(self.groupBox)
        self.input_key.setObjectName(u"input_key")
        self.input_key.setGeometry(QRect(120, 40, 81, 21))
        self.comboBox_tipe = QComboBox(self.groupBox)
        self.comboBox_tipe.setObjectName(u"comboBox_tipe")
        self.comboBox_tipe.setGeometry(QRect(210, 40, 171, 22))
        self.input_nombre = QLineEdit(self.groupBox)
        self.input_nombre.setObjectName(u"input_nombre")
        self.input_nombre.setGeometry(QRect(90, 80, 171, 21))
        self.input_atajo = QKeySequenceEdit(self.groupBox)
        self.input_atajo.setObjectName(u"input_atajo")
        self.input_atajo.setGeometry(QRect(310, 80, 171, 21))
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
        self.input_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.comboBox_tipe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo de MIDI", None))
        self.input_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.menu_opciones.setTitle(QCoreApplication.translate("MainWindow", u"Opciones", None))
    # retranslateUi




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())