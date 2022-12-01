# 수정용
# 예측용 모델 크롤링
import re
import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

category = ['판타지', '로맨스', 'sf', '개그', '액션', '모험']
pages = [239, 231, 56, 58, 42, 25]
pages_2 = [41, 40, 11, 11, 4, 5]

options = webdriver.ChromeOptions()
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)
df_title = pd.DataFrame()
url = 'https://www.aniplustv.com/list'

for i in range(7, 8):   # 카테고리를 없애지말고 range만 바꾸기
    titles = []
    summary = []
    driver.get(url)
    driver.maximize_window()        # 윈도우창 최대화
    time.sleep(1)

    category_xpath1 = '//*[@id="root"]/div[3]/div/div[1]/div/div/div/div[1]/div[2]/div/a'  # 더보기 클릭
    driver.find_element('xpath', category_xpath1).click()
    time.sleep(1)

    category_xpath2 = '//*[@id="root"]/div[3]/div/div[1]/div/div/div/div[1]/div[2]/dl/dd[{}]/div/label'.format(i)     # 카테고리 선택버튼
    driver.find_element('xpath', category_xpath2).click()
    time.sleep(1)

    prev_height = driver.execute_script("return document.body.scrollHeight")