from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QWidget
# from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtWidgets import QApplication, QWidget

from config import speakers


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)

        self.hBoxLayout1 = QtWidgets.QHBoxLayout(Form)
        self.hBoxLayout1.setObjectName("hBoxLayout1")
        # self.hBoxLayout1.setContentsMargins(0, 0, 0, 0)

        self.text = QtWidgets.QPlainTextEdit(Form)
        self.hBoxLayout1.addWidget(self.text)

        self.vBoxLayout1 = QtWidgets.QVBoxLayout(Form)
        self.vBoxLayout1.setObjectName("vBoxLayout1")

        self.gBoxLayout1 = QtWidgets.QGridLayout(Form)
        self.gBoxLayout1.setObjectName("gBoxLayout1")

        self.lbl1 = QtWidgets.QLabel(Form)
        self.lbl1.setText("角色:")

        self.combox = QtWidgets.QComboBox(Form)
        # self.combox.addItem("云希")
        self.combox.addItems(speakers)

        self.lbl2 = QtWidgets.QLabel(Form)
        self.lbl2.setText("语速:")
        
        self.lbl4 = QtWidgets.QLabel(Form)
        self.lbl4.setText("")
        self.lbl5 = QtWidgets.QLabel(Form)
        self.lbl5.setText("")

        self.speed = QtWidgets.QSlider(Form)
        self.speed.setMaximum(10)
        self.speed.setMinimum(0)
        self.speed.setValue(5)
        self.speed.setSliderPosition(1)
        self.speed.setOrientation(QtCore.Qt.Horizontal)
        self.speed.setInvertedAppearance(False)
        self.speed.setInvertedControls(False)
        self.speed.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.speed.setTickInterval(1)

        self.lbl3 = QtWidgets.QLabel(Form)
        self.lbl3.setText("音调:")

        self.volumn = QtWidgets.QSlider(Form)
        self.volumn.setMaximum(10)
        self.volumn.setMinimum(0)
        self.volumn.setValue(5)
        self.volumn.setSliderPosition(1)
        self.volumn.setOrientation(QtCore.Qt.Horizontal)
        self.volumn.setInvertedAppearance(False)
        self.volumn.setInvertedControls(False)
        self.volumn.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.volumn.setTickInterval(1)
        
        self.gBoxLayout1.addWidget(self.lbl1, 0, 0, 1, 1)
        self.gBoxLayout1.addWidget(self.combox, 0, 1, 1, 2)
        self.gBoxLayout1.addWidget(self.lbl2, 1, 0, 1, 1)
        self.gBoxLayout1.addWidget(self.speed, 1, 1, 1, 1)
        self.gBoxLayout1.addWidget(self.lbl4, 1, 2, 1, 1)
        self.gBoxLayout1.addWidget(self.lbl3, 2, 0, 1, 1)
        self.gBoxLayout1.addWidget(self.volumn, 2, 1, 1, 1)
        self.gBoxLayout1.addWidget(self.lbl5, 2, 2, 1, 1)
        
        self.ok = QtWidgets.QPushButton(Form)
        self.ok.setText("提交")

        self.vBoxLayout1.addLayout(self.gBoxLayout1)
        self.vBoxLayout1.addWidget(self.ok)
        
        self.hBoxLayout1.addLayout(self.vBoxLayout1)
        self.hBoxLayout1.setStretch(0, 2)
        self.hBoxLayout1.setStretch(1, 1)
        
        self.lbl4.setText(str(self.speed.value()))
        self.lbl5.setText(str(self.volumn.value()))

        Form.setLayout(self.hBoxLayout1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = QWidget()
    ui = Ui_Form()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
