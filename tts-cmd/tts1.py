import asyncio
import edge_tts
import os 
import sys


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


def preProcess(txtPath):

    txts = os.listdir(txtPath)
    print(txts)
    dataMap = {}

    for fileName in txts:
        text = ""
        mp3Name = os.path.join(txtPath, str(fileName.split(".")[0]) + ".mp3")

        with open(os.path.join(txtPath,fileName), 'r') as f:
            text = f.read()

        dataMap[mp3Name] = text
    return dataMap

# async def ttsEvent():
#     communicate = edge_tts.Communicate(text, 'zh-CN-XiaoyiNeural', rate = "+20%", volume = "+50%")
#     await communicate.save(str(fileName.split(".")[0]) + ".mp3")

async def ttsEvent(text, mp3Name):
    communicate = edge_tts.Communicate(text, 'zh-CN-XiaoyiNeural', rate = "+20%", volume = "+50%")
    with open(mp3Name, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                print(f"WordBoundary: {chunk}")
    
async def _main(dataMap) -> None:
    tasks = []
    for k,v in dataMap.items():
        task = ttsEvent(v, k)
        tasks.append(task)
    await asyncio.gather(*tasks)


txtPath = "./txt"
dataMap = preProcess(txtPath)
# print(dataMap)
asyncio.run(_main(dataMap))