'''
根据163邮箱所有给用户发送验证码的邮件获取注册用户的学号并存储
'''


from selenium import webdriver
import time
import csv
from bs4 import BeautifulSoup
import pandas as pd

driver=webdriver.Chrome()
driver.get("https://mail.163.com/")
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("six_past_twentytwo") #输入账号
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("*****")#输入密码

driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()

time.sleep(6)
html=driver.page_source
soup=BeautifulSoup(html)

# snumbers.csv--存储学号信息的csv文件
f=open('snumbers.csv','w',newline='',encoding='utf-8-sig')
csv_writer=csv.writer(f)
csv_writer.writerow(['学号']) # 标题

totalPage=int(driver.find_element_by_class_name('nui-select-text').text.split('/')[1]) #总页面数
for i in range(totalPage):
    html = driver.page_source
    soup = BeautifulSoup(html)
    maillist = soup.find_all(attrs={"sign": "letter"})  # 提取到这一页所有邮件信息
    for m in maillist:
        if m.attrs['aria-label'].startswith('【二十二点零六】验证码'):
            if('发送成功' in m.find(attrs={"sign":"logo"}).attrs['title']):
                text=m.find(attrs={"sign":"start-from"})
                csv_writer.writerow([text.string]) # 获取发送成功的学号
    # 有个坑，不要最小化页面，会刷新，然后造成点击的按钮过时而点击失败的情况
    driver.find_element_by_xpath('//*[@title="下一页"]').click() # 翻页
    time.sleep(1)

driver.quit()

frame=pd.read_csv("snumbers.csv")
frame["学号"].apply(str)
data=frame.drop_duplicates(subset=["学号"],keep="first",inplace=False) #剔除重复元素
data.to_csv('users.csv',encoding='utf-8-sig')



