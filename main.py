from PyQt5.QtWidgets import QApplication, QWidget

#from ui import Ui_Form
from test0 import Ui_Form


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
