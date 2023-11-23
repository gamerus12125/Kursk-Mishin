import io
import random

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

import sys


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.do_paint = False
        self.pushButton.clicked.connect(lambda x: self.draw_circle())

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            for _ in range(random.randint(2, 10)):
                rx = random.randint(20, 600)
                ry = random.randint(20, 600)
                qp.drawEllipse(rx, ry, rx, rx)
            qp.end()
            self.do_paint = False

    def draw_circle(self):
        self.do_paint = True
        self.pushButton.hide()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())
