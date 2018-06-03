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



driver = webdriver.Chrome(executable_path="/Users/dale/Downloads/chromedriver")

s = Session()
req = Request('GET',  url, data=data, headers=headers)

s.get("https://cas.uwaterloo.ca/cas/login?service=https://waterlooworks.uwaterloo.ca/waterloo.htm")
s.auth = ('xy29chen', '')
s.headers.update({'x-test': 'true'})

