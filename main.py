from PySide6.QtWidgets import QApplication, QWidget, QMainWindow

# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
# from PyQt5.QtCore import QEventLoop
# from PySide6.QtCore import QEventLoop
# from quamash import QEventLoop
import qtinter  # <-- import module
from ui import Ui_Form
from bean import TTS
import asyncio
import edge_tts


async def ttsEvent(tts):
    text = """
        协程(Coroutine)本质上是一个函数，特点是在代码块中可以将执行权交给其他协程
        众所周知，子程序（函数）都是层级调用的，如果在A中调用了B，那么B执行完毕返回后A才能执行完毕。协程与子程序有点类似，但是它在执行过程中可以中断，转而执行其他的协程，在适当的时候再回来继续执行。
        协程与多线程相比的最大优势在于：协程是一个线程中执行，没有线程切换的开销；协程由用户决定在哪里交出控制权
        这里用到的是asyncio库(Python 3.7)，这个库包含了大部分实现协程的魔法工具
    """

    print("tts event 任务启动")
    communicate = edge_tts.Communicate(text, "zh-CN-XiaoxiaoNeural")
    await communicate.save("./data/" + str("test") + ".mp3")


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

    async def btnEvent(self):
        print("the ok btn is clicked")
        print("combox is ", self.ui.combox.currentText())
        print("speed is ", self.ui.speed.value())
        print("volumn is ", self.ui.volumn.value())
        print("text is ", self.ui.text.toPlainText())
        self.ui.text.setPlainText("")
        self.ui.speed.setValue(0)
        self.ui.volumn.setValue(0)
        self.tts.set_text(self.ui.text.toPlainText())
        self.tts.set_voice(self.ui.combox.currentText())
        self.tts.set_output_name("test")
        self._task = asyncio.create_task(self.ttsEvent(self.tts))
        print("task is ", self._task)
        res = await self._task
        print("res is ", res)
        # communicate = edge_tts.Communicate("协程(Coroutine)本质上是一个函数，特点是在代码块中可以将执行权交给其他协程", "zh-CN-XiaoxiaoNeural")
        # await communicate.save("./data/" + str("test") + ".mp3")
        
    async def ttsEvent(self, tts):
        text = """
            协程(Coroutine)本质上是一个函数，特点是在代码块中可以将执行权交给其他协程
            众所周知，子程序（函数）都是层级调用的，如果在A中调用了B，那么B执行完毕返回后A才能执行完毕。协程与子程序有点类似，但是它在执行过程中可以中断，转而执行其他的协程，在适当的时候再回来继续执行。
            协程与多线程相比的最大优势在于：协程是一个线程中执行，没有线程切换的开销；协程由用户决定在哪里交出控制权
            这里用到的是asyncio库(Python 3.7)，这个库包含了大部分实现协程的魔法工具
        """

        print("tts event 任务启动")
        print(dir(edge_tts))
        # com = Communicate(text, "zh-CN-XiaoxiaoNeural")
        # print(com)
        communicate = edge_tts.Communicate(text, "zh-CN-XiaoxiaoNeural")
        await communicate.save("./data/" + str("test") + ".mp3")
        await asyncio.sleep(2)
        return "OK"


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    # loop = QEventLoop(app)
    # asyncio.set_event_loop(loop)
    win = Window()
    with qtinter.using_asyncio_from_qt():  # <-- enable asyncio in qt code
        win.show()
        sys.exit(app.exec())
