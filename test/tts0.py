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

fileName = "算繁星01.txt"
text = ""
mp3Name = str(fileName.split(".")[0]) + ".mp3"

with open(fileName, 'r') as f:
    text = f.read()

async def ttsEvent():
    communicate = edge_tts.Communicate(text, 'zh-CN-XiaoyiNeural', rate = "+20%", volume = "+50%")
    await communicate.save(str(fileName.split(".")[0]) + ".mp3")
    
async def _main() -> None:
    communicate = edge_tts.Communicate(text, 'zh-CN-XiaoyiNeural', rate = "+20%", volume = "+50%")
    with open(mp3Name, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                print(f"WordBoundary: {chunk}")



asyncio.run(_main())