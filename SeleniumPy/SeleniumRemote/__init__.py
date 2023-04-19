
import time
import requests
import os
import shutil
import pickle
import threading, random
import subprocess
import base64
from subprocess import Popen, PIPE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType
from bs4 import BeautifulSoup

from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as exp_con



class SeleniumRemote():
    def __init__(self, port, Index):
 
        self.port = port
        self.index = Index

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("detach", True)
        
        proxies = str(random.choice(open("Proxy.txt",'r').readlines())).strip()
        PROXY_IP = proxies.split(":")[0]
        PROXY_PORT = proxies.split(":")[1]
        # options.add_argument('--proxy-server=http://{}:{}'.format(PROXY_IP, PROXY_PORT))
        self.driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=options)
        self.driver.set_window_position(300*self.index, 0)
        self.driver.set_window_size(200, 800)


    def ElemenWait_Click(self, element: str, sleep: int = 10):
        try:
            WebDriverWait(self.driver, sleep).until(EC.visibility_of_element_located(
                (By.XPATH, element)
            )).click()
            return True
        except:
            return False


    def ElemenWait_SendKeys(self, element: str, sleep: int = 10, keys=str):
        try:
            WebDriverWait(self.driver, sleep).until(EC.visibility_of_element_located(
                (By.XPATH, element)
            )).send_keys(str(keys))
            return True
        except:
            return False


    def Element_Find(self, element: str):
        try:
            Ele = self.driver.find_element(By.XPATH, element)
            return Ele
        except: 
            return False

    def Element_Scroll(self, element: str):
        try:
            Sele = self.driver.find_element(By.XPATH, element)
            actions = ActionChains(self.driver)
            actions.move_to_element(Sele)
            actions.perform()
            return True
        except:
            return False


    def Element_ClearText(self, element: str, sleep: int = 10):
        try:
            WebDriverWait(self.driver, sleep).until(EC.visibility_of_element_located(
                (By.XPATH, element)
            )).clear()
            return True
        except:
            return False

 
    def Element_Scroll_End(self,):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            return True
        except:
            return False
