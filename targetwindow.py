from datetime import datetime

from PySide2 import QtCore
from PySide2.QtGui import QWindow
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSlider, QLabel, QLineEdit, QStyle
from PySide2.QtCore import Slot,Qt
from ruamel import yaml

from daily_input import daily_input


class targetWindow(QWindow):
    def __init__(self):
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
        daily_input_done = QPushButton("Send korsan dagen var: (blank for  å skippe)")
        daily_input_done.clicked.connect(self.submit_daily_input)
        daily_input_done.setMinimumWidth(500)
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

        self.container = QWidget()
        self.container.setLayout(layout)

        self.container.show()


    def submit_daily_input(self):
        # Code to simplify dumpfile. Avoid references/pointers in yaml-file.
        yaml.Dumper.ignore_aliases = lambda *args: True
        input_to_be_submitted = daily_input(self.input_hope.text(), self.input_fear.text(), self.input_general.text(), self.rating.value())
        with open("logfile.yaml") as file:
            file_content = yaml.load(file)
            file_content["daily_inputs"][str(datetime.now())] = input_to_be_submitted
        with open("logfile.yaml", 'w+') as file:
            yaml.dump(file_content, file, default_flow_style=False)




    def changeSlider(self, value):
        self.rating_lab.setText("slider verdi: " + str(value))