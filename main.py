from PySide2 import QtWidgets
import sys
from mainwindow import MainWindow
from PySide2.QtCore import Slot,Qt
from PySide2.QtGui import QPalette, QColor, QIcon

# Dark Palette (found on github, couldn't track the original author)
default_palette = QPalette()
dark_palette = QPalette()
dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.black)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setPalette(dark_palette)
    app.setWindowIcon(QIcon("20210522_110856.jpg"))
    widget = MainWindow()
    widget.setWindowTitle("Din egen buddy_")
    widget.resize(800, 400)
    widget.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec_())
