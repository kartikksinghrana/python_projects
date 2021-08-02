from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait 
import random

comments=["Nice shot!","i love your profile","your feed is an inspiration","just incredible","what camera do you use?","nice"]
randomNum=random.randint(20,45)
username="your_username"
browser =  webdriver.Chrome("I:\Python_projects\insta_Bot\chromedriver.exe")
#open instagram
browser.get("https://www.instagram.com")  
#wait for 3 sec to fully load the page
time.sleep (3)

#identify user field and send username
username_input = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("your_username")
#identify password field and send password
password_input = browser.find_element_by_css_selector("input[name='password']").send_keys("your_password")
#find and click submit
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()
time.sleep(2)
#click on notNow button for save info popup
try:
    notNowButton = WebDriverWait(browser, 15).until(
        lambda d: d.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button'))
    notNowButton.click()
except:
    pass

#save login not now button 
time.sleep(2)
notNowButton2 = WebDriverWait(browser, 15).until(
    lambda d: d.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]'))
notNowButton2.click()
time.sleep(3)

#loop for following people from suggestion
for i in range (randomNum):
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button/div').click()
    browser.refresh()
    time.sleep(3)



# ==============================================================================================================================================================$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$            not working        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# going to profile page
# profile_img_button=browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img')
# profile_img_button.click()
# time.sleep(1)

# profile_button =browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[1]/svg/path')
# profile_button.click()

# # getting follwing
# following_list=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')
# ==============================================================================================================================================================$$$$$$$$$


# going to profile page
profile_img_button=browser.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(username))
profile_img_button.click()
time.sleep(3)

# getting follwing
following_list=browser.find_element_by_xpath("//a[contains(@href,'/{}/following')]".format(username))
following_list.click()
time.sleep(3)

for i in range(5):
    browser.find_element_by_xpath('//button[text()="Following"]')\
        .click()
    time.sleep(2)
    try:    
        browser.find_element_by_xpath('//button[text()="Unfollow"]')\
            .click()
    except:
        pass
    time.sleep(2)

