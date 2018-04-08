from bs4 import BeautifulSoup
from urllib import request
from datetime import datetime

# 抓取网页
# response =request.urlopen("http://fund.eastmoney.com/fund.html")
# html=response.read()
# html=html.decode('gb2312')  #这一步是为啥？
# with open("./htmls/1.txt",'wb') as f:
#     f.write(html.encode('utf8'))
#     f.close()
#
#
# with open("./htmls/1.txt",'rb') as f:
#     html=f.read().decode('utf8')
#     f.close()
#
# soup=BeautifulSoup(html,"html.parser")
# fCodes=soup.find("table",id="oTable").tbody.find_all("td","bzdm") #基金编码
# result=()
# for fCode in fCodes:
#     result+=({"fcode":fCode.get_text()
#                  ,"fname":fCode.next_sibling.find("a").get_text()
#                  ,"NAV":fCode.next_sibling.next_sibling.get_text()
#                  ,"ACCNAV":fCode.next_sibling.next_sibling.next_sibling.get_text(),"updatetime":datetime.now().isoformat(sep=' ',timespec="seconds")}
#                   ,)
#
# print(result)
# import pymysql
# from pymysql.cursors import Cursor,SSCursor
# from common.config import dbconfig
# connection = pymysql.connect(**dbconfig)
#
# cursor=Cursor(connection)
# cursor.executemany("""insert into myfund(fcode, fname,NAV,ACCNAV,updatetime)
# values(%(fcode)s,%(fname)s,%(NAV)s,%(ACCNAV)s,%(updatetime)s)
# ON duplicate KEY UPDATE `updatetime`=%(updatetime)s,NAV=%(NAV)s,ACCNAV=%(ACCNAV)s"""
#                ,result)
# connection.commit()
# connection.close()


# from sqlalchemy import create_engine,desc,text
# from mappers.Infos import News
# from sqlalchemy.orm import sessionmaker
# engine = create_engine('',echo=True)
# # Session=sessionmaker(engine)
# # mysession=Session()

# from  Spider.Fund import getHtml,page1_url,getPage,page2_url
# import execjs
# result=getHtml(page2_url)
# js_engine=execjs.get()
#
# js=result+"""
#  let getDB=()=>db;
# """
# compile=js_engine.compile(js)
# res=compile.call('getDB')
# print(res['datas'])

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.PhantomJS()
driver.get("http://fund.eastmoney.com/fund.html")
getPage_text = driver.find_element_by_id("pager").find_element_by_xpath("span[@class='nv']").text
allpage = ''.join(filter(str.isdigit, getPage_text))  # 得到一共多少页
# for

# 得到点击JS的span

pageBtn = driver.find_element_by_id("pager").find_element_by_xpath("span[@value=2']")

pageBtn.click()


def isat(driver):
	return driver.find_element_by_id("pager").find_element_by_xpath("span[@value=2]") \
			   .get_attribute("class").find("at") != -1


WebDriverWait(driver, 20).until(isat)
print(driver.page_source)
  
