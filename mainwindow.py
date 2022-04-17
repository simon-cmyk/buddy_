import sys

from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, \
    QProgressBar, QScrollBar, QSlider

from daily_input import daily_input


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Din egen Buddy_")
        instruction_lab = QLabel("Legg til korsan dagen er (eit håp, ein frykt og ein generell kommentar :)")
        hope_lab = QLabel("Håpet:")
        fear_lab = QLabel("Frykta:")
        general_lab = QLabel("Generelt:")

        self.input_hope = QLineEdit()
        self.input_fear = QLineEdit()
        self.input_general = QLineEdit()
        self.input_hope.textChanged[str].connect(lambda text: self.input_hope.setText(text))
        self.input_fear.textChanged[str].connect(lambda text: self.input_fear.setText(text))
        self.input_general.textChanged[str].connect(lambda text: self.input_general.setText(text))

        self.rating_lab = QLabel()
        self.rating = QSlider()
        self.rating.setOrientation(QtCore.Qt.Horizontal)
        self.rating.setMaximum(100)
        self.rating.setMinimum(0)
        self.rating.valueChanged.connect(self.changeSlider)
        daily_input_done = QPushButton("Submit how you feel today: (leave blank to skip)")
        daily_input_done.clicked.connect(self.submit_daily_input)
        self.rating_lab.setText("slider verdi: " + str(self.rating.value()))

        layout = QVBoxLayout()
        layout.addWidget(instruction_lab)
        layout.addWidget(hope_lab)
        layout.addWidget(self.input_hope)
        layout.addWidget(fear_lab)
        layout.addWidget(self.input_fear)
        layout.addWidget(general_lab)
        layout.addWidget(self.input_general)
        layout.addWidget(self.rating_lab)
        layout.addWidget(self.rating)
        layout.addWidget(daily_input_done)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def submit_daily_input(self):
        daily_input(self.input_hope.text(), self.input_fear.text(), self.input_general.text(), self.rating.value())

    def changeSlider(self, value):
        self.rating_lab.setText("slider verdi: " + str(value))
