import requests
import time
import schedule
from bs4 import BeautifulSoup as BS
from smtplib import SMTP

url = 'https://www.amazon.in/Apple-Quad-core-10th-Generation-Intel-Core-i5-Processor/dp/B0864HQK2F/ref=sr_1_6?crid=2N6XSGSIG84PN&dchild=1&keywords=apple+laptop&qid=1615130641&sprefix=apple+laptop%2Caps%2C316&sr=8-6'

def extract_Price():
   
    page = requests.get(url, headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36" })
    soup = BS(page.content, 'html.parser')
    price = float(soup.find(id = "priceblock_ourprice").text.split()[1].replace(",",""))
    return price

SMTP_SERVER = "smtp.gmail.com"
PORT = 587
EMAIL_ID = "test230py@gmail.com"
PASSWORD = "djahzmnwbqyysuuj"

def sendMail():
    server = SMTP(SMTP_SERVER,PORT)
    server.starttls()
    server.login(EMAIL_ID, PASSWORD)

    subject = "BUY NOW!!"
    body = "Price of the product that you were looking for has fallen. Go buy it now!!! --- " + url
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(EMAIL_ID, "coolvk230@gmail.com", msg)
    server.quit()

AFFORDABLE_PRICE = 130000

def check():
    if extract_Price()<=AFFORDABLE_PRICE:
        print("Mail sent Buy it now!!")
        sendMail()
        exit()

schedule.every(1).hour.do(check)

while 1:
    schedule.run_pending()
    time.sleep(1)
    
    