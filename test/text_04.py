from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get(r"http://www.baidu.com")

driver.find_element(by=By.ID, value="kw").send_keys("baidu")
# driver.find_element(by=By.NAME, value="wd").send_keys("baidu")
# driver.find_element(by=By.CLASS_NAME, value="s_ipt").send_keys("baidu")
# driver.find_element(by=By.TAG_NAME, value="input").send_keys("baidu")
driver.find_element(by=By.XPATH, value="//*[@id='su']").click()
sleep(1)
# driver.find_element(by=By.PARTIAL_LINK_TEXT, value="使用").click()
driver.find_element(by=By.XPATH, value=r"//*[@id='1']/div/h3/a[1]").click()
driver.find_element(by=By.CSS_SELECTOR, value="#kw").send_keys("ss")
