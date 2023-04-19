N=open
D=True
C=print
from selenium import webdriver as F
from selenium.webdriver.common.by import By as B
from selenium.webdriver.common.keys import Keys as G
import time as E,js2py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By as B
from selenium.webdriver.support import expected_conditions as L
import threading as H
from selenium.webdriver.common.action_chains import ActionChains as J
import pickle as M,json,os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as I
os.system('cls')
class K:
	def __init__(B,i):
		A=F.ChromeOptions();A.add_experimental_option('detach',D);A.add_experimental_option('excludeSwitches',['enable-logging']);A.add_argument('--app=https://httpbin.org/ip');A.add_argument('--window-size=200,400');B.App=F.Chrome(service=I('chromedriver.exe'),options=A)
		if i>=7:C=400;i=i-5
		else:C=0
		B.App.set_window_position(200*i,C,windowHandle='current')
	def Open(A):A.App.get('https://pyobfuscate.com/py');A.App.execute_script("document.body.style.zoom='40%'");E.sleep(5);D=A.App.find_element(B.XPATH,'//*[@id="message"]');D.send_keys('print("Hello")');C(A.App.get_cookies());E.sleep(1);C('+'*80);D=A.App.find_element(B.XPATH,'//*[@id="work"]');A.App.execute_script('arguments[0].click();',D);H=J(A.App);H.key_down(G.CONTROL).send_keys('A').key_up(G.CONTROL).perform();F=A.App.find_element(B.ID,'myInput').text;I=N('main.txt','w+',encoding='utf-8').write(F);C(F)
	def Dulingo(A,i):
		V='Find Element Done';U='ok';T='//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/input';S=False;R='//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/textarea';Q='//*[@id="session/PlayerFooter"]/div/div/button/span';L='//*[@id="session/PlayerFooter"]/div/div/button';O=M.load(N('Cookie1.pkl','rb'));A.App.get('https://www.duolingo.com/learn')
		for P in O:A.App.add_cookie(P)
		A.App.refresh();A.App.execute_script("document.body.style.zoom='80%'")
		while D:
			E.sleep(5);A.App.get('https://www.duolingo.com/checkpoint/en/0');E.sleep(5);A.App.find_element(B.XPATH,L).click();G=0
			while D:
				G=G+1;E.sleep(0.5);A.App.implicitly_wait(1);K=J(A.App);K.send_keys('2');K.perform();F=A.App.find_element(B.XPATH,Q).is_displayed()
				try:H=A.App.find_element(B.XPATH,R).is_displayed()
				except:H=S
				try:I=A.App.find_element(B.XPATH,T).is_displayed()
				except:I=S
				if H==D and F==D:A.App.find_element(B.XPATH,R).send_keys(U);C(V)
				if I==D and F==D:A.App.find_element(B.XPATH,T).send_keys(U);C(V)
				C(f"{F}|{H}|{I}")
				if F==D:A.App.implicitly_wait(1);A.App.find_element(B.XPATH,Q).click();C(f"=====>>>Done:{G}")
				else:break
			C('Slove Done');E.sleep(5)
			while D:
				A.App.implicitly_wait(1);E.sleep(0.5)
				try:
					F=A.App.find_element(B.XPATH,L).is_displayed()
					if F==D:A.App.find_element(B.XPATH,L).click()
					else:break
					C(F)
				except Exception as W:break
def A():
	for A in range(14):E.sleep(5);B=K(A);C(f"{A}=====>>>");D=H.Thread(target=B.Dulingo,args=(A,));D.start()
A()