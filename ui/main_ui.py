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
from PySide6.QtWidgets import (QApplication, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QToolBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_configuracion = QAction(MainWindow)
        self.action_configuracion.setObjectName(u"action_configuracion")
        self.action_Info = QAction(MainWindow)
        self.action_Info.setObjectName(u"action_Info")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(100, 50, 361, 114))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 361, 54))
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 75, 24))
        self.toolBox.addItem(self.page, u"Inicio")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 361, 54))
        self.toolBox.addItem(self.page_2, u"final")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
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

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MIDIKeymap", None))
        self.action_configuracion.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.action_Info.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Crear Perfil", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"final", None))
        self.menu_opciones.setTitle(QCoreApplication.translate("MainWindow", u"Opciones", None))
    # retranslateUi

