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

# 第一步翻页抓取所有的页面的超链接及对应的名字，在本地新建目录  此处可以用线程池来实现
# 第二步根据超链接及对应名字去下载超链接里面对应的图片链接

# 目前代码已经完成了，但是还缺少优化

# 717
pageids = np.arange(717)
baseUrl = "https://www.pkdoutu.com/article/list/?page={}"
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


def getPageAllLiks(i):
    url = baseUrl.format(i)
    try:
        response = requests.get(url, headers={"User-Agent": random.choice(USER_AGENT_LIST)})
        content = response.content.decode('utf-8')
        soup = BeautifulSoup(content, "lxml")
        # 提取 tag
        keyword_list = [tag for tag in soup.find_all("a", class_="list-group-item random_list")]
        for key in keyword_list:
            # print(key.get("href"), key.div.contents[0])
            name = key.div.contents[0]
            link = key.get("href")
            dataMaps[name] = link
    except:
        print("error")
        return str(url) + " is failed"
    return str(url) + " is ok"
    
def mkDataDir(name):
    dataDir = os.path.join(dataPath, name)
    if not os.path.exists(dataDir):
        os.mkdir(dataDir)
        print(f'{dataDir} created successfully.')
       

def urllib_download(url, name):
    from urllib.request import urlretrieve
    print(url, name)
    urlretrieve(url, name)   
        
def getImgLinks(url):
    # url = "https://www.pkdoutu.com/article/detail/2904735"
    try:
        response = requests.get(url, headers={"User-Agent": random.choice(USER_AGENT_LIST)})
        content = response.content.decode('utf-8')
        soup = BeautifulSoup(content, "lxml")
        pathName = soup.find('div', class_='pic-title').h1.a.get_text()
        if not os.path.exists(os.path.join(dataPath, pathName)):
            os.mkdir(os.path.join(dataPath, pathName))
        keyword_list = [tag for tag in soup.find_all("div", class_="artile_des")]
        for key in keyword_list:
            url = key.img.get('src')
            name = key.img.get('alt')
            name = os.path.join(dataPath, pathName, url.split("/")[-1]) 
            urllib_download(url, name)
    except:
        print("error")
        return str(url) + " is failed"
    return str(url) + " is ok"
    
    pass
    
def threadExecutor(func, dataList):
    # 线程池版本
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        # 创建多个Future，每个Future对应一个任务
        futures = [executor.submit(func, i) for i in dataList]

        # 获取每个任务的结果
        for future in concurrent.futures.as_completed(futures):
            content = future.result()
            if content:
                print(content)
                
    with open(os.path.join(dataPath, "data.json"), 'w') as f:
        json.dump(dataMaps, f)

def main():
    # 第一步获取所有的链接并保存成json格式
    threadExecutor(getPageAllLiks, pageids)
    # 第二步爬取二级图像链接
    imgLinks = list(dataMaps.values())
    threadExecutor(getImgLinks, imgLinks)
    
if __name__ == "__main__":
    main()

