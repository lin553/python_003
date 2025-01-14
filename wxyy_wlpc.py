# 原名：文心一言_网络爬虫.py

# 失败
import requests  
from bs4 import BeautifulSoup  
from urllib.parse import urlparse  
import re  
  
def is_ad(url):  
    # 根据广告链接的特点判断是否为广告链接，这里仅作示例，实际操作中可能需要更复杂的规则  
    return 'googleads' in url  
  
def get_links(keyword):  
    url = f'https://www.baidu.com/s?wd={keyword}'  
    response = requests.get(url)  
    soup = BeautifulSoup(response.text, 'html.parser')  
    results = soup.find_all('a', href=True)  # 获取所有链接  
  
    real_links = []  # 过滤掉广告链接后的结果  
    for result in results:  
        href = result['href']  
        if not is_ad(href):  # 如果不是广告链接，保留该链接  
            real_links.append(href)  
            print(f'非广告链接: {href}')  # 输出非广告链接，你可以在这里进行你的处理，比如保存到文件等。  
    return real_links[:30]  # 返回前30条非广告链接  



'''
def get_title(link):  
    response = requests.get(link)  
    soup = BeautifulSoup(response.text, 'html.parser')  
    title = soup.title.string  
    return title  
  
def main(keyword):  
    links = get_links(keyword)  
    for link in links:  
        print(f'链接: {link}')  
        print(f'标题: {get_title(link)}')
'''






def main(keyword):  
    links = get_links(keyword)  
    for link in links:  
        print(f'链接: {link}')  # 输出链接，你可以在这里进行你的处理，比如保存到文件等。  
      #  print(f'摘要: {get_summary(link)}')  # 输出摘要，你可以在这里进行你的处理，比如保存到文件等。
