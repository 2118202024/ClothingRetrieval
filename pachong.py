# -*- encoding: utf-8 -*-
import re
import requests
import time
import os
import bs4

def get_one_html(url):  # 获取一个页面的html页面并返回
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
        r = requests.get(url, headers=headers)
        # print(r.text)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            return r.text
    except Exception as er:
        print(er)


def get_pic_url(html):  # 用正则提取每一页的关键信息返回
    soup=bs4.BeautifulSoup(html,'html.parser')
    pic_urls = soup.find_all(attrs={'class': 'p-img'})

    # pic_urls = re.findall('"pic_url":"(.*?)"', html, re.S)
    img_url = []  # 创建空列表，装每一页的所有图片的链接
    for one_pic_url in pic_urls:
        k=one_pic_url.find("a")
        img=one_pic_url.find("img")
        href= img.get('source-data-lazy-img')
        img_url.append('http:' + href)
    return img_url  # 返回图片的链接的列表


def write_to_file(page, img_urls,keyword):  # 写入文件（下载）
    i = page  # 利用页码，防止后面的写入会覆盖之前的
    n = 0
    rootpath='./picture/1/'
    for pic_url in img_urls:
        pic = requests.get(pic_url)
        if not os.path.exists(rootpath):
            os.makedirs(rootpath)
            print("目录创建成功！")
        with open(rootpath + str(i) +"-" +str(n) + '.jpg', 'wb') as f:
            f.write(pic.content)
        print('---第{}页第{}张图下载成功---'.format(str(i), str(n)))
        n += 1


def main(keyword, page, url):
    html = get_one_html(url)  # 调用函数得到该页的hml
    img_urls = get_pic_url(html)  # 调用函数得到该页的所有图片的链接
    write_to_file(page, img_urls,keyword)  # 调用函数，写入即下载图片
cloth_dict={
0	:'牛仔裤',
1	:'鞋子',
2	:'双肩背包',
3   :'长袖外套',
4   :'鸭舌帽',
5   :'连衣裙'
}

if __name__ == '__main__':
    keyword = input('请输入关键词：')
    page_num = eval(input('请输入要爬取的页数：'))
    # keyword ="裙子"
    # page_num = 1
    try:
        # os.mkdir('D:/pictures/')
        for page in range(1, page_num+1):
            # url = 'http://jd.com/search?q=' + keyword + '&s=' + str(page)
            # url = 'http://s.taobao.com/search?q=' + keyword + '&s=' + str(page)
            url = "https://search.jd.com/Search?keyword=%s&enc=utf-8&page=%s"%(keyword,page*2-1)
            main(keyword, page, url)
            if page % 2 == 0:
                time.sleep(2)  # 每爬取2页停留10秒
    except Exception as err:
        print(err)
