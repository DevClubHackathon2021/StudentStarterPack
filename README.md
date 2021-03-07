# StudentStarterPack
This is a bot that actually consists of many bots which are: 
- CodeForces Bot
- Impartus Lecture viewer Bot
- Price Bot

**To be able to use this bot in your system you have to follow following steps:**
- Download ChromeDriver which is available at: https://chromedriver.chromium.org/downloads
Check your Chrome version and download the chrome driver version accordingly and just copy and paste the ```chromedriver.exe``` file to path: ```C:\Program Files (x86)\```.
- Install python and set up python from https://www.python.org/downloads/
- Install selenium library using ```pip install selenium``` in cmd.
- Also, in the bots we have asked user to enter credentials each time he/she runs the program, if you do not want to enter them again and again just open the python file and follow following steps:
   1. Look for the following code : ```password.sendkey(pwd)```
   2. Now change the ```pwd``` to ```<your password without these angular brackets>``` and delete the following line: ```pwd=getpass("Please enter password (Your password will       not appear on screen while typing):")```
   3. For the username code do the same thing , delete the print code that requests for username and replace the ```input()``` with your username.  
 
