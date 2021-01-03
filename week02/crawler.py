import requests
from lxml import etree
from time import sleep
def get_news_info(myurl):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    header = {'user-agent': ua}
    response = requests.get(myurl, headers=header)
    selector = etree.HTML(response.text)
    news_sort = selector.xpath('//a[@href='//linux.solidot.org/']')
    news_article = selector.xpath('//a[@href='/story?sid=66496']')

    news_info = dict(zip(news_sort, news_article))
    with open('./week02/newscrawler.txt',
              'w', encoding='utf-8') as f:
        f.write(str(news_info))

if __name__ == "__main__":
    get_news_info('https://www.solidot.org/')