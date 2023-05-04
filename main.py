from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

from ui import Ui_Form
# from test0 import Ui_Form
from pyui import Ui_MainWindow


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
