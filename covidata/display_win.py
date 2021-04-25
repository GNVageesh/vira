from PyQt5.QtWidgets import QApplication, QWidget
import sys


def display():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle("Simple Window")
    w.show()

    sys.exit(app.exec_())
