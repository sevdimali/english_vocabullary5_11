import codecs
from googletrans import Translator
import xlsxwriter
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def translate(word):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='D:/chromedriver.exe', options=chrome_options)
    try:
        # driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
        driver.get("http://dilmanc.az/")
        driver.find_element_by_id('id_from').send_keys(word)
        driver.find_element_by_id('id_translate_submit').click()
        # time.sleep(5)
        tr_word = driver.find_element_by_id('id_to').text
        if tr_word == '':
            cimis = driver.find_element_by_name('li')
            cimis2 = cimis.find_element_by_name('span').text
            print(cimis2)
        driver.quit()
    except:
        tr_word = ''
    return tr_word


def extract_word(word):
    parts = word.partition('/')
    ac_word = parts[0].strip()
    spelling_tup = parts[1:]
    spelling = ''.join(spelling_tup)
    spelling = spelling.replace('\r\n','')
    word_az = translate(ac_word)
    dict_word = {'word':ac_word,'spelling': spelling, 'word_az': word_az}
    return dict_word


lines = codecs.open('words_demo.txt', encoding='utf-8')
all_words = []
for line in lines:
    dudu = extract_word(line)
    print(dudu)
    all_words.append(dudu)

workbook = xlsxwriter.Workbook('5.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for row, data in enumerate(all_words):
    worksheet.write_string(row, col, data.get('word'))
    worksheet.write_string(row, col+1, data.get('spelling'))
    worksheet.write_string(row, col+2, data.get('word_az'))
workbook.close()
