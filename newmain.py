from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

file = open('log.txt', 'w')
#driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
#option.add_argument('--headless')
driver = webdriver.Chrome(options=option)

driver.get('https://www.lambdatest.com/selenium-playground/iframe-demo/')
driver.maximize_window()

sleep(1)

iframe = driver.find_element(By.XPATH, '//*[@id="iFrame1"]')
driver.switch_to.frame(iframe)
lon = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]')
sleep(2)
lon.send_keys(Keys.CONTROL + 'a')
lon.send_keys(Keys.DELETE)
bold_button_iframe = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/button[1]')
bold_button_iframe.click()
lon.send_keys('New Message')
file.close()