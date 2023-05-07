import asyncio
import edge_tts


voies = [
"zh-CN-XiaoxiaoNeural",
"zh-CN-XiaoyiNeural",
"zh-CN-YunjianNeural",
"zh-CN-YunxiNeural",
"zh-CN-YunxiaNeural",
"zh-CN-YunyangNeural",
"zh-CN-liaoning-XiaobeiNeural",
"zh-CN-shaanxi-XiaoniNeural",
"zh-HK-HiuGaaiNeural",
"zh-HK-HiuMaanNeural",
"zh-HK-WanLungNeural",
"zh-TW-HsiaoChenNeural",
"zh-TW-HsiaoYuNeural",
"zh-TW-YunJheNeural"
]

async def ttsEvent():
    text = """
        协程(Coroutine)本质上是一个函数，特点是在代码块中可以将执行权交给其他协程
        众所周知，子程序（函数）都是层级调用的，如果在A中调用了B，那么B执行完毕返回后A才能执行完毕。协程与子程序有点类似，但是它在执行过程中可以中断，转而执行其他的协程，在适当的时候再回来继续执行。
        协程与多线程相比的最大优势在于：协程是一个线程中执行，没有线程切换的开销；协程由用户决定在哪里交出控制权
        这里用到的是asyncio库(Python 3.7)，这个库包含了大部分实现协程的魔法工具
    """
    for i in voies:
        communicate = edge_tts.Communicate(text, i)
        await communicate.save(str(i) + ".mp3")


asyncio.run(ttsEvent())