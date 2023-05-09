# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSplitter, QStatusBar,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 619)
        MainWindow.setFocusPolicy(Qt.ClickFocus)
        MainWindow.setAnimated(True)
        self.actionquit = QAction(MainWindow)
        self.actionquit.setObjectName(u"actionquit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 40, 311, 271))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 20, 511, 461))
        self.ok = QPushButton(self.centralwidget)
        self.ok.setObjectName(u"ok")
        self.ok.setGeometry(QRect(590, 330, 113, 32))
        self.splitter_4 = QSplitter(self.centralwidget)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(0, 0, 0, 0))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(540, 110, 241, 91))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.volumn = QLabel(self.widget)
        self.volumn.setObjectName(u"volumn")

        self.gridLayout.addWidget(self.volumn, 0, 0, 1, 1)

        self.horizontalSlider = QSlider(self.widget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMouseTracking(False)
        self.horizontalSlider.setTabletTracking(True)
        self.horizontalSlider.setFocusPolicy(Qt.NoFocus)
        self.horizontalSlider.setInputMethodHints(Qt.ImhNone)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setValue(1)
        self.horizontalSlider.setSliderPosition(1)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(0)

        self.gridLayout.addWidget(self.horizontalSlider, 0, 1, 1, 1)

        self.speaker = QLabel(self.widget)
        self.speaker.setObjectName(u"speaker")

        self.gridLayout.addWidget(self.speaker, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 819, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionquit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionquit.setText(QCoreApplication.translate("MainWindow", u"quit", None))
        self.ok.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.volumn.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u901f", None))
        self.speaker.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e91\u5e0c", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e91\u7476", None))

        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

