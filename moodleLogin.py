from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys 
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# command = sys.argv[1]
username = sys.argv[1]
password = sys.argv[2]
course = sys.argv[3]


driver.get("https://moodle.iitd.ac.in/login/index.php")
loginId = driver.find_element_by_id("username")
loginId.send_keys(username)

pwd = driver.find_element_by_id("password")
pwd.send_keys(password)

captcha = driver.find_element_by_id("login")

st = captcha.text
ls = st.split(" ")

flag = 1
for i in range(len(ls)):
    if ls[i] == '+':
        res = int(ls[i-1]) + int(ls[i+1])
        break
    elif ls[i] == '-':
        res = int(ls[i-1]) - int(ls[i+1])
        break
    elif ls[i] == 'second':
        flag = 2
    elif ls[i] == ',':
        if flag == 1:
            res = int(ls[i-1])
        else:
            res = int(ls[i+1])
        break

captchaAnswer = driver.find_element_by_id("valuepkg3")
captchaAnswer.clear()

captchaAnswer.send_keys(str(res))    
submit_button = driver.find_element_by_id("loginbtn")
submit_button.click()

# if command == 'login':
#     username = sys.argv[2]
#     password = sys.argv[3]
#     login(username, password)

siteHomeClass = driver.find_element_by_id("inst4")
listOfa = siteHomeClass.find_elements_by_tag_name("a")
siteHome = listOfa[1]
linkSiteHome = siteHome.get_attribute("href")
driver.get(linkSiteHome)

maindiv = driver.find_element_by_id("frontpage-course-list")
courseClass1hd = maindiv.find_elements_by_tag_name("h3")

for i in range(len(courseClass1hd)):
	courseClass1a = courseClass1hd[i].find_element_by_tag_name("a")
	courseClass1Name = courseClass1a.text
	if course in courseClass1Name:
		link = courseClass1a.get_attribute("href")
		driver.get(link)
		break
impartusClass = driver.find_elements_by_class_name("activityinstance")
impartusClassA = impartusClass[1].find_element_by_tag_name("a")
link = impartusClassA.get_attribute("href")
driver.get(link)

#boom we r at the lectures page