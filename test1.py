from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
#转换后的py类改为这样
class Ui_mm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)


    def setupUi(self, mm):
        mm.setObjectName("mm")
        mm.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(mm)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(mm)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(mm)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(mm)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(mm)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.retranslateUi(mm)
        QtCore.QMetaObject.connectSlotsByName(mm)

    def retranslateUi(self, mm):
        _translate = QtCore.QCoreApplication.translate
        mm.setWindowTitle(_translate("mm", "Form"))
        self.pushButton_4.setText(_translate("mm", "PushButton"))
        self.pushButton_2.setText(_translate("mm", "PushButton"))
        self.pushButton_3.setText(_translate("mm", "PushButton"))
        self.pushButton.setText(_translate("mm", "PushButton"))
#调用做相应修改
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_mm()
    ui.show()
    sys.exit(app.exec_())

