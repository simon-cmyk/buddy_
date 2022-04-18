import sys

from PySide2 import QtCore
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, \
    QProgressBar, QScrollBar, QSlider, QGroupBox, QHBoxLayout

from daily_input import daily_input
from targetwindow import targetWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.groupBox = None
        self.buttons = list()
        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

    def createLayout(self):
        self.groupBox = QGroupBox("Log prestasjon/sett mål/reflekter på ting")
        self.groupBox.setFont(QFont("Sanserif", 13))

        hbox = QHBoxLayout()

        button = QPushButton("Nytt Target", self)
        button.setMinimumHeight(40)
        self.buttons.append(button)
        hbox.addWidget(button)
        self.groupBox.setLayout(hbox)
        button.pressed.connect(self.newTarget)

        self.show()
    def newTarget(self):
        target = targetWindow()