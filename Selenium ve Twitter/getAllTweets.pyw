from selenium import webdriver
import loginInfo
import time
browser = webdriver.Firefox()
browser.get("https://twitter.com/")
time.sleep(3)
girisyap = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]")
girisyap.click()
time.sleep(2)

username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
password = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")


username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

time.sleep(3)

login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")
login.click()
time.sleep(3)

 
"""searchArea = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")
searchArea.send_keys("sorupdururlar")
searchArea.send_keys(u'\ue007')

time.sleep(3)"""


lenOfPage = browser.execute_script("window.scrollTo(0,document.body.scrollHeight); var lenOfPage = document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    tweetField = browser.find_elements_by_css_selector(".css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim")
    for tweet in tweetField:
        try:
            if tweet.get_attribute("data-testid") == "like":
                tweet.click()
    except Exception:
        print("Hata")
    lenOfPage = browser.execute_script("window.scrollTo(0,document.body.scrollHeight); var lenOfPage = document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
tweetler = []

tweetler = set()
tweetField = browser.find_elements_by_css_selector(".css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0")
for tweet in tweetField:
        try:
            if tweet.get_attribute("data-testid") == "like":
                tweet.click()
    except Exception:
        print("Hata")

"""tweetCount = 1
with open("tweetler.txt","w",encoding ="UTF-8") as file:
    for tweet in tweetler\
            :
        file.write(str(tweetCount) + "\n" + tweet + "\n")
        file.write("****************************\n")
        tweetCount += 1
time.sleep(2)"""


    

browser.close()

