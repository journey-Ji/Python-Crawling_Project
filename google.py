from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import ssl

#https를 사용하는 경우 인증서 인증의 차이 때문에 아래 코드를 입력해주어서 오류발생을 방지한다.
ssl._create_default_https_context = ssl._create_unverified_context



#executable_path=r'경로' 를 통해 경로설정이 필요하다.
#chromedriver와 google.py 파일이 같은 경로상에 존재해야한다.
driver = webdriver.Chrome(executable_path=r'/Users/journey/Desktop/journey_coding/google_image_crawl/selenium/chromedriver')
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
#홈페이지의 요소들을 찾는 함수
elem = driver.find_element_by_name("q") #이름이 q인 요소를 찾아감. 실제로 name='q'는 검색창으로 설정되어있음
#우리가 원하는 입력값을 전송할 수 있다.
elem.send_keys("조코딩")
elem.send_keys(Keys.RETURN)#엔터키를 전송한다.

SCROLL_PAUSE_TIME = 1

# Get scroll height
# 브라우저의 높이를 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    # 브라우저의 끝까지 스크롤을 내린다.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    # 로드가 끝날때 까지, 기다린다
    time.sleep(SCROLL_PAUSE_TIME)


    # Calculate new scroll height and compare with last scroll height
    # 브라우저의 높이를 다시 구해서 new_height에 저장
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height: # 이전의 브라우저 높이와 새로구한 높이가 같다면 (더 이상 불러올 것이 없다면)
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height


imgaes = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')
count = 1
for image in imgaes:
    try:
        image.click()
        time.sleep(1)
        
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count)+".jpg")
        count = count +1
    except:
        pass

driver.close()

'''

    
    #이미지 저장하기 방법 1
    #src = driver.find_element_by_css_selector('.n3VNCb').get_attribute("src")
    #driver.get(src)#주소를 가져와서 driver에 저장
    #driver.save_screenshot(str(count) +".jpg") # driver에 저장된 이미지를 변수의 이름으로 컴퓨터에 저장
    #count = count + 1
    

방법 2
import urllib.request
imgUrl = driver.find_element_by_css_selector('.n3VNCb').get_attribute("src")
urllib.request.urlretrieve(imgUrl, 'test.jpg')
'''

