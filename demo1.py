import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel, QComboBox, QSlider, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口大小和标题
        self.setWindowTitle('My App')
        self.resize(800, 600)
        # 布局
        main_vbox = QVBoxLayout()
        # 左右布局
        hbox = QHBoxLayout()
        # 左半部分
        vbox_left = QVBoxLayout()
        self.textedit = QTextEdit()
        vbox_left.addWidget(self.textedit)
        # 右半部分
        vbox_right = QVBoxLayout()
        # 下拉框
        combo_box = QComboBox()
        combo_box.addItems(['选项一', '选项二', '选项三'])
        vbox_right.addWidget(QLabel('下拉框'))
        vbox_right.addWidget(combo_box)
        # 音量滑动条
        slider_volume = QSlider(Qt.Horizontal)
        slider_volume.setMinimum(0)
        slider_volume.setMaximum(100)
        vbox_right.addWidget(QLabel('音量'))
        vbox_right.addWidget(slider_volume)
        # 语速滑动条
        slider_speed = QSlider(Qt.Horizontal)
        slider_speed.setMinimum(0)
        slider_speed.setMaximum(100)
        vbox_right.addWidget(QLabel('语速'))
        vbox_right.addWidget(slider_speed)
        # 确认按钮
        btn_confirm = QPushButton('确认')
        vbox_right.addWidget(btn_confirm)
        # 添加到右半部分布局中
        hbox.addLayout(vbox_left)
        hbox.addLayout(vbox_right)
        # 滚动条放在中央页面
        main_vbox.addLayout(hbox)
        self.setLayout(main_vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
