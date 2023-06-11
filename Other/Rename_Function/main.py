from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,js2py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import threading
from selenium.webdriver.common.action_chains import ActionChains
import pickle
import json,os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service


os.system('cls')
class Selenium():
    def __init__(self,i):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--app=https://httpbin.org/ip") #nó sẽ hiển thị chrome đó như một cái app
        options.add_argument("--window-size=200,400")
        
        self.App = webdriver.Chrome(service = Service("chromedriver.exe"),options=options)
        if i >= 5: 
            y = 400
            i = i - 5
        else: 
            y = 0
            
        self.App.set_window_position(200*i, y, windowHandle ='current')
        

        
        

    def Open(self):
        self.App.get('https://pyobfuscate.com/py')
        self.App.execute_script("document.body.style.zoom='40%'")
        time.sleep(5)
        elem = self.App.find_element(By.XPATH, '//*[@id="message"]')  # Find the search box
        elem.send_keys('print("Hello")')
        print(self.App.get_cookies())
        time.sleep(1)
        print('+'*80)
        elem = self.App.find_element(By.XPATH,'//*[@id="work"]')
        self.App.execute_script("arguments[0].click();", elem)
        
 
        #Space Keys
        action = ActionChains(self.App)
        action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
        ####
        element = self.App.find_element(By.ID, 'myInput').text
        a = open('main.txt','w+',encoding = 'utf-8').write(element)
        print(element)
        #self.App.close()
    def Dulingo(self,i):
        #Load Cookie
        cookies = pickle.load(open("Cookie1.pkl", "rb"))
        self.App.get('https://www.duolingo.com/learn')
        for cookie in cookies:
            self.App.add_cookie(cookie)
        self.App.refresh()
        self.App.execute_script("document.body.style.zoom='80%'")


        # Get Cookie To File
        #xxx = input('AnyKey:')
        #pickle.dump(self.App.get_cookies(), open('Cookie.pkl','wb'))
        while True:
            time.sleep(5)
            
            # Go To Site
            self.App.get('https://www.duolingo.com/checkpoint/en/0')
            time.sleep(5)
            # Click X_Path 
            self.App.find_element(By.XPATH,'//*[@id="session/PlayerFooter"]/div/div/button').click()

            p = 0
            while True:
                p = p + 1
                time.sleep(0.5)
                self.App.implicitly_wait(1)
                actions = ActionChains(self.App)
                actions.send_keys('2')
                actions.perform()
                XX = self.App.find_element(By.XPATH,'//*[@id="session/PlayerFooter"]/div/div/button/span').is_displayed()
                try: XX_1 = self.App.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/textarea').is_displayed()
                except: XX_1 = False
                try: XX_2 = self.App.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/input').is_displayed()
                except: XX_2 = False


                if XX_1 == True and XX == True: 
                    self.App.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/textarea').send_keys('ok')
                    print('Find Element Done')
                
                if XX_2 == True and XX == True: 
                    self.App.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/input').send_keys('ok')
                    print('Find Element Done')
                
                


                print(f'{XX}|{XX_1}|{XX_2}')
                if XX == True:
                    self.App.implicitly_wait(1)
                    self.App.find_element(By.XPATH,'//*[@id="session/PlayerFooter"]/div/div/button/span').click()
                    # self.App.execute_script("arguments[0].click();", elem)
                    print(f'=====>>>Done:{p}')
                else:
                    break
            print('Slove Done')
            time.sleep(5)
            while True:
                self.App.implicitly_wait(1)
                time.sleep(0.5)
                try:
                    XX = self.App.find_element(By.XPATH,'//*[@id="session/PlayerFooter"]/div/div/button').is_displayed()
                    if XX == True:
                        self.App.find_element(By.XPATH,'//*[@id="session/PlayerFooter"]/div/div/button').click()
                    else:
                        break
                    print(XX)
                except Exception as e:
                    break
            # self.App.close()
                
            



def Main():
    for k in range(10):
        time.sleep(5)
        App = Selenium(k)
        print(f'{k}=====>>>')
        x = threading.Thread(target = App.Dulingo ,args = (k,))
        x.start()
Main()
