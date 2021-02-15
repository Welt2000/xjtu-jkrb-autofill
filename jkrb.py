# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : $2021.2.10 $13:34
# @Author  : Welt
# @File    : $jkrb.py

from selenium import webdriver
import sys
import os
import time
import random
try:
    f = open("id.txt","r")#暂时采用文件输入的形式保存用户名和密码
except Exception as e:
    print("未检测到或id.txt文件损坏，请重新配置！")
    os.system("pause")
    sys.exit()
user = f.readline()
password = f.readline()
f.close()
try:
    driver = webdriver.Edge(executable_path='msedgedriver.exe')#可以自适应启动EDGE或Chrome
except Exception as e:
    try:
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
    except Exception as e:
        try:
            driver = webdriver.Firefox(executable_path='geckodriver.exe')
        except Exception as e:
            print("Edge，Chrome，Firefox版本与驱动均不匹配，请更新浏览器或驱动，脚本将在按任意键后退出。\n")
            os.system("pause")
            sys.exit()
url = r'http://jkrb.xjtu.edu.cn/EIP/user/index.htm'#健康日报地址
driver.get(url)
driver.maximize_window()#最大化窗口以便于后续操作
#登录部分
driver.find_element_by_name("username").send_keys(user)
driver.find_element_by_name("pwd").send_keys(password)
driver.find_element_by_id("account_login").click()
driver.implicitly_wait(10)#网卡的可以酌情调节所有等待部分
#进入本科生每日健康填报页面
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mini-17$body$2"]/iframe'))
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="ab0ab54c0e7048a7b583d5c1c8da7c06"]/div/div[2]/div[2]/iframe'))
driver.find_element_by_xpath('//*[@id="form"]/div[2]/div/ul[1]/li[2]/div/a').click()
driver.switch_to.default_content()
driver.implicitly_wait(10)
time.sleep(1)
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mini-17$body$3"]/iframe'))
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/ul/li[1]").click()
driver.implicitly_wait(10)
driver.switch_to.default_content()
time.sleep(1)
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mini-17$body$4"]/iframe'))
try:
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mini-14$body$2"]/iframe'))
except Exception as e:
    print("今日已填报！Already Completed!")
    os.system("pause")
    driver.quit()
    sys.exit()
driver.find_element_by_id("mini-3$ck$2").click()#勾选健康码为绿色
driver.implicitly_wait(10)
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
print("完成填报!Completed!")
sys.exit()