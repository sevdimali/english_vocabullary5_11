from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
driver.maximize_window()
driver.get("http://dilmanc.az/")
driver.find_element_by_id('id_from').send_keys('Hello')
driver.find_element_by_id('id_translate_submit').click()
time.sleep(3)
tr_word = driver.find_element_by_id('id_to').text
