"""
-*-author : QzmVc1 -*-
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
# 显示等待
from selenium.webdriver.support.wait import WebDriverWait
# 设置等待执行语句
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from PIL import Image
from urllib.request import urlretrieve
from os.path import dirname,join
import random

USERNAME = input("请输入正方账号：")
PASSWORD = input("请输入正方密码：")

# 登陆正方
driver = webdriver.Chrome()
driver.get('http://jwxt.njupt.edu.cn/')
# 输入账号
driver.find_element_by_id('txtUserName').clear()
driver.find_element_by_id('txtUserName').send_keys(USERNAME)

# 密码处理
driver.find_element_by_id('Textbox1').click()
driver.find_element_by_xpath('//*[@id="form1"]/div/div[1]/h2/img').click()
driver.find_element_by_id('TextBox2').clear()
driver.find_element_by_id('TextBox2').send_keys(PASSWORD)
# path = join(dirname(__file__),'save.png')
# urlretrieve('http://jwxt.njupt.edu.cn/CheckCode.aspx',path)
# im = Image.open(path)
# im.show()
# 手动输入验证码
cap = input("请输入验证码：")
driver.find_element_by_id('txtSecretCode').send_keys(cap)
# WebDriverWait(driver,10).until(
#     EC.presence_of_element_located(
#        (By.ID,'TextBox2'),
#     )
# )
driver.find_element_by_id('Button1').click()
print("------------南邮正方系统自动登陆成功！------------")
try:
    driver.switch_to.alert.accept()
except:
    pass
print("------------开始自动填写教学质量评价！------------\n...")
length1 = len(driver.find_elements_by_xpath('//*[@id="headDiv"]/ul/li[3]/ul/li'))

for k in range(1,3):
    for i in range(1,length1+1):
        drop_down = driver.find_element_by_xpath('//*[@id="headDiv"]/ul/li[3]/a/span')
        action = ActionChains(driver)
        action.move_to_element(drop_down).perform()
        action.move_by_offset(0,i*20).click().perform()
        try:
            driver.switch_to.alert.accept()
        except:
            pass
        driver.switch_to.frame('iframeautoheight')
        length1_ = len(driver.find_elements_by_xpath('//*[@id="DataGrid1"]/tbody/tr'))-1
        if k == 1:
            for j in range(2,length1_+1):
                Select(driver.find_element_by_id('DataGrid1__ctl{0}_JS1'.format(j))).select_by_value("完全认同")
            Select(driver.find_element_by_id('DataGrid1__ctl{0}_JS1'.format(length1_+1))).select_by_value("相对认同")
            driver.find_element_by_name('Button1').click()
            if i == length1:
                driver.find_element_by_name('Button2').click()
                try:
                    driver.switch_to.alert.accept()
                except:
                    pass
            print("...\n")
        else:
            for j in range(2, length1_ + 1):
                Select(driver.find_element_by_id('DataGrid1__ctl{0}_JS1'.format(j))).select_by_value("好")
            Select(driver.find_element_by_id('DataGrid1__ctl{0}_JS1'.format(length1_ + 1))).select_by_value("较好")
            if i != length1:
                driver.find_element_by_name('Button1').click()
            else:
                driver.find_element_by_name('Button1').click()
                try:
                    driver.switch_to.alert.accept()
                except:
                    pass
                driver.find_element_by_name('Button2').click()
                try:
                    driver.switch_to.alert.accept()
                except:
                    pass
            print("...\n")
        driver.switch_to.default_content()

driver.quit()

print("------------教学质量评价已全部自动填写完毕！------------")
