#基金抓取
from urllib import request
import chardet
from bs4 import  BeautifulSoup

page1_url="http://fund.eastmoney.com/fund.html"
page2_url="http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=2,200&dt=1505405262745&atfc=&onlySale=0"

def getHtml(pageUrl):
    response =request.urlopen(pageUrl)
    raw_html=response.read()
    getEncoding=chardet.detect(raw_html)['encoding']
    return raw_html.decode(getEncoding)
def getPage(html):
    soup = BeautifulSoup(html, "html.parser")
    pageHtml=soup.find("div",id="pager").find("span","nv").get_text()
    return ''.join(filter(str.isdigit, pageHtml))