from ui.main_ui import Ui_MainWindow
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
    QWidget,QLabel,QVBoxLayout)
import sys
from controllers.midi_asociaton import MIDIControllers,MIDIbind,MIDIkeys,MIDIcc,MIDIPads


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.actualizar_panel()

        # Conectar botones
        self.ui.boton_detectar.clicked.connect(self.detectar)

    # Funciones Botones
    def detectar(self):
        status,key = MIDIControllers.all_midis(MIDIControllers,ui=True)

        self.ui.input_status.setText(status)
        self.ui.input_key.setText(key)
        self.update()

    def actualizar_panel(self):
        midi = MIDIbind()
        midi.load_bind()
        keys = MIDIkeys.controlls
        cc = MIDIcc.controlls
        pads = MIDIPads.controlls

        if keys:
            self.ui.led_keys.display(len(keys))
            for key in keys.values():
                str_command = ' + '.join(key.command)
                label = QLabel(f"{key.name.title()} 🎹 {key.number} - {str_command.title()}")
                group_box = self.ui.box_keys
                layout = group_box.layout()

                if not layout:
                    layout = QVBoxLayout()
                    group_box.setLayout(layout)

                layout.addWidget(label)
        if cc:
            self.ui.led_cc.display(len(cc))
            for c in cc.values():
                str_command = ' + '.join(c.command)
                label = QLabel(f"{c.name.title()} 🎚️ {c.number} - {str_command.title()}")
                group_box = self.ui.box_cc
                layout = group_box.layout()

                if not layout:
                    layout = QVBoxLayout()
                    group_box.setLayout(layout)
                layout.addWidget(label)

        if pads:
            self.ui.led_pads.display(len(pads))
            for pad in pads.values():
                str_command = ' + '.join(pad.command)
                label = QLabel(f"{pad.name.title()}: ⬛ {pad.number} - {str_command.title()}")
                group_box = self.ui.box_pads_2
                layout = group_box.layout()

                if not layout:
                    layout = QVBoxLayout()
                    group_box.setLayout(layout)
                layout.addWidget(label)

        self.update()
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())