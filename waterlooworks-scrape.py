import os
import libraries
import re
import urllib2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pandas as pd

from requests import Request, Session


option = webdriver.ChromeOptions()
option.add_argument(“ — incognito”)

browser = webdriver.Chrome(executable_path=".", chrome_options=option)
browser.implicitly_wait(1)
browser.get("https://cas.uwaterloo.ca/cas/login?service=https://waterlooworks.uwaterloo.ca/waterloo.htm")
browser.implicitly_wait(1)
browser.title
browser.save_screenshot("aaa")

browser.
browser.
browser.
browser.


s.auth = ('xy29chen', '')
s.headers.update({'x-test': 'true'})

