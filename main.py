from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6 import QtCore, QtWidgets

# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
# from PyQt5.QtCore import QEventLoop
# from PySide6.QtCore import QEventLoop
# from quamash import QEventLoop
import qtinter  # <-- import module
from ui import Ui_Form
from bean import TTS
import asyncio
import edge_tts

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi()
        self.tts = TTS()

    def setupUi(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.ui.ok.clicked.connect(self.btnEvent)
        self.ui.ok.clicked.connect(qtinter.asyncslot(self.btnEvent))
        self.ui.speed.valueChanged.connect(self.speedValueChanged)
        self.ui.volumn.valueChanged.connect(self.volumnValueChanged)
        
    def speedValueChanged(self):
        self.ui.lbl4.setText(str(self.ui.speed.value()))

    def volumnValueChanged(self):
        self.ui.lbl5.setText(str(self.ui.volumn.value()))

    async def btnEvent(self):
        self.tts.set_text(self.ui.text.toPlainText())
        self.tts.set_voice(self.ui.combox.currentText())
        self.tts.set_output_name("test")
        
        self.ui.text.setPlainText("")
        self.ui.speed.setValue(0)
        self.ui.volumn.setValue(0)
        
        
        self._task = asyncio.create_task(self.ttsEvent(self.tts))
        res = await self._task
        self.ui.ok.setDisabled(1)
        # if res == "OK":
            # self.ui.ok.setEnabled(1)
            # app.aboutQt()
        
    async def ttsEvent(self, tts):
        communicate = edge_tts.Communicate(self.tts.get_text(), self.tts.get_voice())
        await communicate.save("./data/" + str(self.tts.get_output_name()) + ".mp3")
        return "OK"


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    # loop = QEventLoop(app)
    # asyncio.set_event_loop(loop)
    win = Window()
    with qtinter.using_asyncio_from_qt(): 
        win.show()
        sys.exit(app.exec())
