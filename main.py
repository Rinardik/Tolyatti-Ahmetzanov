import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6 import QPoint
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6 import uic
from ui import Ui_MainWindow

class Example(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # uic.loadUi('UI.ui', self)
        self.setupUi(self)
        self.setWindowTitle('Рисование')
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True


    def draw_flag(self, qp):
        R = randint(20, 100)
        x = randint(0, 500)
        y = randint(0, 500)
        qp.serBrush(QColor(255, 255, 0))
        qp.drawEllipse(QPoint(x, y), R / 2, R / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())