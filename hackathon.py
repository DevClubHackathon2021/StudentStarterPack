from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from PIL import Image
from getpass import getpass
from tabulate import tabulate
from terminaltables import AsciiTable
import time
import os
import linecache



options= webdriver.ChromeOptions()
options.headless=True

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH,options=options)
#write code to login!!!!
# driver.get('https://codeforces.com/enter?back=%2F')
# username=driver.find_element_by_id('handleOrEmail')
# print('Enter Username: ')
# #User Enters his/her username here:
# username.send_keys(input())

# password=driver.find_element_by_id('password')
# #User enters his/her password here:
# pwd=getpass("Please enter password (Your password will not appear on screen while typing):")
# password.send_keys(pwd)

# button=driver.find_element_by_class_name('submit')
# button.click()

# time.sleep(2)

# print("Please enter your command, type help for list of commands: ")
# command=input()

while True:
    try:
     print("Please enter your command, type help for list of commands: ")
     command=input()
     
     if command=='upcoming' or command=='Upcoming':
        driver.get("https://codeforces.com/contests?complete=true")
        time.sleep(1)
        name_list=[]
        date_list=[]
        
        
        
        index=2
        while True:
            try:
                status=driver.find_element_by_xpath(('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table/tbody/tr[{}]/td[5]').format(index))
                status_text=status.text
            
                if "Before" in status_text:
                    contest=driver.find_element_by_xpath(('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table/tbody/tr[{}]/td[1]').format(index))
                    contest_name=contest.text  

                    date=driver.find_element_by_xpath(('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table/tbody/tr[{}]/td[3]').format(index))
                    date_text=date.text
                    
                    name_list.append(contest_name)
                    date_list.append(date_text)
                
                
                index+=1
            except:
                break    
        titles = ['Name','Date']
        data = [titles] + list(zip(name_list, date_list))

        for i, d in enumerate(data):
            line = '|'.join(str(x).ljust(89) for x in d)
            print(line)
            if i == 0:
              print('-' * len(line))
        continue
     
     
     if command=='help' or command=='Help':
        print("----------------------------------------------------------------------")
        print("help           |        gives the list of commands")
        print("----------------------------------------------------------------------")
        print("upcoming       |        gives the list of upcoming CodeForces Contests")
        print("----------------------------------------------------------------------")
        print("rating         |        gives your current rating")
        print("----------------------------------------------------------------------")
        print("exit           |        quits the program")
        print("----------------------------------------------------------------------")
        continue
     
     
     if command=='rating' or command=='Rating':
        print("Enter codeforces handle of user(It is case-sensitive): ")
        userhandle=input()

        driver.get('https://codeforces.com/api/user.rating?handle={}'.format(userhandle))
        content=driver.find_element_by_tag_name('pre').text
        
        if content.rfind("newRating")!=-1:
            bracket_index=content.rfind("}",0,-2)
            print(content[content.rfind("newRating")+11:bracket_index])
        elif "FAILED" in content:
            print("USER NOT FOUND !! INVALID HANDLE")
        else:
            print("Unrated")
        continue


     elif command=='exit':
         break

    except :
        print("Invalid command , type exit to quit")
        continue


'''
if command=='upcoming' or command=='Upcoming':
    driver.get("https://codeforces.com/contests?complete=true")
    time.sleep(1)
    name_list=[]
    date_list=[]
    
    
    
    index=2
    while True:
        try:
          status=driver.find_element_by_xpath(('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table/tbody/tr[{}]/td[5]').format(index))
          status_text=status.text
          
          if "Before" in status_text:
              contest=driver.find_element_by_xpath(('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table/tbody/tr[{}]/td[1]').format(index))
              contest_name=contest.text  

              date=driver.find_element_by_xpath(('//*[@id="pageContent"]/div[1]/div[1]/div[6]/table/tbody/tr[{}]/td[3]').format(index))
              date_text=date.text
              
              name_list.append(contest_name)
              date_list.append(date_text)
              
              
          index+=1
        except:
          break    
    titles = ['Name','Date']
    data = [titles] + list(zip(name_list, date_list))

    for i, d in enumerate(data):
        line = '|'.join(str(x).ljust(89) for x in d)
        print(line)
        if i == 0:
           print('-' * len(line))

if command=='help' or command=='Help':
    print("----------------------------------------------------------------------")
    print("help           |        gives the list of commands")
    print("----------------------------------------------------------------------")
    print("upcoming       |        gives the list of upcoming CodeForces Contests")
    print("----------------------------------------------------------------------")
    print("rating         |        gives your current rating")
    print("----------------------------------------------------------------------")


if command=='rating' or command=='Rating':
   print("Enter codeforces handle of user(It is case-sensitive): ")
   userhandle=input()

   driver.get('https://codeforces.com/api/user.rating?handle={}'.format(userhandle))
   content=driver.find_element_by_tag_name('pre').text
   
   if content.rfind("newRating")!=-1:
       bracket_index=content.rfind("}",0,-2)
       print(content[content.rfind("newRating")+11:bracket_index])
   elif "FAILED" in content:
       print("USER NOT FOUND !! INVALID HANDLE")
   else:
       print("Unrated")        
'''

        
