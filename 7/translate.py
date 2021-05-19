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
            extra_txt = driver.find_element_by_id('divResults')
            extra_txt = extra_txt.find_element_by_tag_name('span').text
            tr_word = extra_txt
        driver.quit()
    except:
        tr_word = ''
        driver.quit()
    return tr_word


def extract_word(word):
    word = word.split('–', 1)
    word = word[0]
    # parts = word.partition('/')
    # ac_word = parts[0].strip()
    # spelling_tup = parts[1:]
    # spelling = ''.join(spelling_tup)
    # spelling = spelling.replace('\r\n', '')
    word_az = translate(word)
    dict_word = {'word': word, 'spelling': '', 'word_az': word_az}
    return dict_word


lines = codecs.open('words.txt', encoding='utf-8')
all_words = []
for line in lines:
    dudu = extract_word(line)
    print(dudu)
    all_words.append(dudu)

workbook = xlsxwriter.Workbook('7.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for row, data in enumerate(all_words):
    worksheet.write_string(row, col, data.get('word'))
    worksheet.write_string(row, col + 1, data.get('spelling'))
    worksheet.write_string(row, col + 2, data.get('word_az'))
workbook.close()
