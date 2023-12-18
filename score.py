from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import time

driver = webdriver.Firefox()
driver.get("https://flashscore.com.br")

time.sleep(5)

tab_aovivo = driver.find_element("xpath","/html/body/div[4]/div[1]/div/div/main/div[4]/div[2]/div/div[1]/div[1]/div[2]/div[2]")
tab_aovivo.click()

div_mae = driver.find_element("xpath","/html/body/div[4]/div[1]/div/div/main/div[4]")

html_content = div_mae.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')

#print(soup.prettify())

times_home = soup.find_all('div',class_='event__participant--home')
times_away = soup.find_all('div',class_='event__participant--away')

score_home = soup.find_all('div',class_='event__score--home')
score_away = soup.find_all('div',class_='event__score--away')



for i in range(len(times_home)):
    print(times_home[i].get_text(),score_home[i].get_text(),"X",score_away[i].get_text(),times_away[i].get_text())
    print()

