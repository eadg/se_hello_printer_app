from selenium import webdriver
from time import sleep

dri = webdriver.Firefox()
dri.get("https://www.wp.pl")
dri.maximize_window()
sleep(3)

dri.quit()
