# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : $2021.2.10 $13:34
# @Author  : Welt
# @File    : $jkrb.py

from selenium import webdriver
import time
import random
f = open("id.txt","r")#暂时采用文件输入的形式保存用户名和密码
user = f.readline()
password = f.readline()
f.close()
driver = webdriver.Edge()#可以自适应启动EDGE或Chrome
if driver:
    url = r'http://jkrb.xjtu.edu.cn/EIP/user/index.htm'
else:
    driver = webdriver.Chrome()
    url = r'http://jkrb.xjtu.edu.cn/EIP/user/index.htm'
driver.get(url)
driver.maximize_window()#最大化窗口以便于后续操作
#登录部分
driver.find_element_by_name("username").send_keys(user)
driver.find_element_by_name("pwd").send_keys(password)
driver.find_element_by_id("account_login").click()
driver.implicitly_wait(20)#网卡的可以酌情调节所有等待部分
#进入本科生每日健康填报页面
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mini-17$body$2"]/iframe'))
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="ab0ab54c0e7048a7b583d5c1c8da7c06"]/div/div[2]/div[2]/iframe'))
driver.find_element_by_xpath('//*[@id="form"]/div[2]/div/ul[1]/li[2]/div/a').click()
driver.switch_to.default_content()
driver.implicitly_wait(20)
time.sleep(1)
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mini-17$body$3"]/iframe'))
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/ul/li[1]").click()
driver.implicitly_wait(20)
driver.switch_to.default_content()
time.sleep(1)
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mini-17$body$4"]/iframe'))
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mini-14$body$2"]/iframe'))
driver.find_element_by_id("mini-3$ck$2").click()#勾选健康码为绿色
driver.implicitly_wait(20)
time.sleep(1)
target=driver.find_element_by_name("BRTW")
driver.execute_script("arguments[0].scrollIntoView();", target)
target.click()
tm=random.randint(360, 369)
tp=str(tm/10)
print(tp)#在命令行中回显此次填报的温度
target.send_keys(tp)
driver.switch_to.parent_frame()
driver.find_element_by_id("sendBtn").click()
driver.find_element_by_id("mini-17").click()
time.sleep(10)#等待提交
driver.quit()
print("Completed!")