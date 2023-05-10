import asyncio
import aiohttp
import requests
import concurrent.futures
import numpy as np
import random
import re
from bs4 import BeautifulSoup
import os 
import json
import logging
import aiofiles

# 第一步翻页抓取所有的页面的超链接及对应的名字，在本地新建目录  此处可以用线程池来实现
# 第二步根据超链接及对应名字去下载超链接里面对应的图片链接

# 目前代码已经完成了，但是还缺少优化

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# 1153
pageids = np.arange(10)
baseUrl = "https://www.adoutu.com/article/list/{}"
baseLink = "https://www.adoutu.com"
dataPath = "./download/"

dataMaps = {}

USER_AGENT_LIST = [
    'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
    'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
    'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
    'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
    'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
    'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
    'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
]

# 并发声明
semaphore = asyncio.Semaphore(10)

async def downloadImg(name, url):
    logging.info("download url is %s", url)
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            img = await response.read()
            async with aiofiles.open(name, mode='wb') as f:
                await f.write(img)
                await f.close()

async def getImageInfo(name, url):
    logging.info('scraping name is %s url is %s', name, url)
    mkDataDir(name)
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        content = await response.text()
        soup = BeautifulSoup(content, "lxml")
        # logging.info("%s", "a")
        for key in soup.find_all("div", class_="detail-picture"):
            # logging.info("%s", "b")
            link = key.img.get('src')
            imgName = os.path.join(dataPath, name, link.split("/")[-1])
            logging.info("imgName is %s", imgName)
            task = asyncio.create_task(downloadImg(imgName, link))
            await task
            # await downloadImg(imgName, link)

async def getPageInfos(i):
    url = baseUrl.format(i)
    logging.info('scraping %s', url)
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        content = await response.text()
        soup = BeautifulSoup(content, "lxml")
        keyword_list = [tag for tag in soup.find_all("div", class_="list-group article-part")]
        for key in keyword_list:
            name = key.span.contents[0]
            link = baseLink + key.a.get('href')
            dataMaps[name] = link
            # await getImageInfo(name, url)

    
def mkDataDir(name):
    dataDir = os.path.join(dataPath, name)
    if not os.path.exists(dataDir):
        os.mkdir(dataDir)
        print(f'{dataDir} created successfully.')
    
        
    
async def main():
    tasks = []
    # tasks.append(getPageInfos(11))    # 将请求放到列表里，再通过gather执行并发
    # tasks.append(getPageInfos(10))    # 将请求放到列表里，再通过gather执行并发
    # tasks.append(getImageInfo("黄夏温和男朋友吵架表情包", 'https://www.adoutu.com/article/info/11535'))
    # await asyncio.gather(*tasks)
    for i in range(1,5):
        await getPageInfos(i)
    
    for k, v in dataMaps.items():
        # tasks.append(getImageInfo(k,v))
        # await asyncio.gather(*tasks)
        await getImageInfo(k, v)
        
    # await getImageInfo("暹罗猫表情包", "https://www.adoutu.com/article/list/2")
        
    
if __name__ == "__main__":
    asyncio.run(main())