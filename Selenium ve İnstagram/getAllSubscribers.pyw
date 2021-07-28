from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.get("https://www.instagram.com/")
time.sleep(7)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("")
password.send_keys("")

loginButton = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
loginButton.click()
time.sleep(7)

browser.get("https://www.instagram.com/merveseeenn")
time.sleep(4)

followersButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
followersButton.click()
time.sleep(5)

jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.body.scrollHeight;
return lenOfPage;
"""

lenOfPage = browser.execute_script("jscommand")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("jscommand")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

followersList = []
followers = browser.find_elements_by_css_selector = (".FPmhX.notranslate._0imsa ")

for follower in followers:
    followersList.append(follower.text)
with open ("followers.txt","w",encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")
browser.close()

