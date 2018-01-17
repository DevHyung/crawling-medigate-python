from CONFIG import *
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
headers = {
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection':'keep-alive',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
if __name__=="__main__":

    exit(-1)
    driver = webdriver.Chrome('./chromedriver')
    driver.get('http://www.medigate.net/index.jsp')
    # login start
    driver.find_element_by_xpath('//*[@id="contentID"]/div[1]/div[2]/div[1]/form/fieldset/div[2]/input[1]').send_keys(ID)
    driver.find_element_by_xpath('//*[@id="contentID"]/div[1]/div[2]/div[1]/form/fieldset/div[2]/input[2]').send_keys(PW)
    driver.find_element_by_xpath('//*[@id="contentID"]/div[1]/div[2]/div[1]/form/fieldset/div[2]/button').click()
    # login end

    """selenium cookie To requests
    cookies_list = driver.get_cookies()
    s = requests.Session()
    for cookie in cookies_list:
        s.cookies.set(cookie['name'], cookie['value'])
    html = s.get('http://www.medigate.net/cbiz/recjob.do?cmd=list&menuGroupCode=CBIZ&menuCode=RECJOB&ctgCode=job&pageNo=3&_nil=1&_nil=',headers=headers)
    bs4 = BeautifulSoup(html.text,'lxml')
    print(bs4.prettify())
    driver.quit()
    
    
    with open('test.jpg', "wb") as file:
        # get request
        response = requests.get('http://image.medigate.net/upload/2017/02/1486943727887_34172.jpg')
        # write to file
        file.write(response.content)
    """


