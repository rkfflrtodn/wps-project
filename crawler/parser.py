# parser.py
# import requests
# from bs4 import BeautifulSoup
# import json
# import os
#
# # python파일의 위치
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#
# req = requests.get('https://www.yogiyo.co.kr/mobile/#/')
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
# my_titles = soup.select(
#     # 'div > span'
#     'div > strong'
#     )
#
# data = {}
#
# for title in my_titles:
#     data[title.text] = title.get('href')
#
# with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
#     json.dump(data, json_file)
# ==============================================================================
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
#
# url = "https://www.rottentomatoes.com/"
# html = urlopen(url)
# source = html.read() # 바이트코드 type으로 소스를 읽는다.
# html.close() # urlopen을 진행한 후에는 close를 한다.
#
# soup = BeautifulSoup(source, "html5lib") # 파싱할 문서를 BeautifulSoup 클래스의 생성자에 넘겨주어 문서 개체를 생성, 관습적으로 soup 이라 부름
# table = soup.find(id="Top-Box-Office")
# movies = table.find_all(class_="middle_col")
#
# for movie in movies:
#     title = movie.get_text()
#     print(title, end=' ')
#     link = movie.a.get('href')
#     url = 'https://www.rottentomatoes.com' + link
#     print(url)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import json
import os
path = "/usr/bin/chromedriver"


driver = webdriver.Chrome(path)
driver.get('https://www.yogiyo.co.kr/mobile/#/')

# assert "Google" in driver.title

element = driver.find_element_by_name("address_input")
element.clear()
element.send_keys("서울 송파구 가락1동")
element.send_keys(Keys.ENTER)
# element.submit()

driver.get('https://www.yogiyo.co.kr/mobile/#/서울/138161/')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div > ul > li.min-price.ng-binding')

print("complete")
for n in notices:
    print(n.text.strip())