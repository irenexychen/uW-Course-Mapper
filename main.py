import os
import libraries
import re
import urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd


url = "http://www.ucalendar.uwaterloo.ca/1819/COURSE/course-CS.html"

def basicScrape:
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, ‘html.parser’)

	name_box = soup.find(‘a’, attrs={‘name’: ‘CS%i’})
	name = name_box.text.strip() # strip() is used to remove starting and trailing



def lxmlScrape:
	driver = webdriver.Firefox()
	driver.implicitly_wait(30)
	driver.get(url)

	python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
	python_button.click() #click fhsu link

	soup_level1=BeautifulSoup(driver.page_source, 'lxml')

	datalist = []
	x = 0

	for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
		##code to execute in for loop goes here
	

	driver.quit()

	#combine all pandas dataframes in the list into one big dataframe
	result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))],ignore_index=True)


	#convert the pandas dataframe to JSON
	json_records = result.to_json(orient='records')

	#get current working directory
	path = os.getcwd()

	#open, write, and close the file
	f = open(path + "\\fhsu_payroll_data.json","w") #FHSU
	f.write(json_records)
	f.close()
