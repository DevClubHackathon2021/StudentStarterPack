# StudentStarterPack
This is a bot that actually consists of many bots which are: 
- CodeForces Bot
- Impartus Lecture viewer Bot
- Price Tracker Bot

**To be able to use this bot in your system you have to follow following steps:**
- Download ChromeDriver which is available at: https://chromedriver.chromium.org/downloads
Check your Chrome version and download the chrome driver version accordingly and just copy and paste the ```chromedriver.exe``` file to path: ```C:\Program Files (x86)\```.
- Install python and set up python from https://www.python.org/downloads/
- Install selenium library using ```pip install selenium``` in cmd.
- Install beautifulSoup Library using ```pip install bs4```
- Install schedule Library using ```pip install schedule```
- Install requests Library using ```pip install requests```
- Install html5 library using ```pip install html5lib```
- Also, in the bots we have asked user to enter credentials each time he/she runs the program, if you do not want to enter them again and again just open the python file and follow following steps:
   1. Look for the following code : ```password.sendkey(pwd)```
   2. Now change the ```pwd``` to ```<your password without these angular brackets>``` and delete the following line: ```pwd=getpass("Please enter password (Your password will       not appear on screen while typing):")```
   3. For the username code do the same thing , delete the print code that requests for username and replace the ```input()``` with your username.  
 ***For the amazonTrackerBot you need to follow following steps:***
- Google -> "what is my user agent?" and copy the result and paste it in :
   ```page = requests.get(url, headers = {"User-Agent" : "<your user agent goes here>"   })```
   
- In the code search for url and paste the product url there
- 
