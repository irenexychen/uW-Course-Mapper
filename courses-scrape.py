from bs4 import BeautifulSoup
import re
import urllib3
from pymongo import MongoClient


client = MongoClient('localhost', 27071)
collection = client.courses
posts = collection.posts



class Post(Document):
    course_name = StringField(required=True)
    course_id = NumberInt()
    prereq = StringField(required=False)
    antireq = StringField(required=False)
    desc = DateTimeField(required=True)



class data():

	def __init__(self):
		self.url = "http://www.ucalendar.uwaterloo.ca/1819/COURSE/course-CS.html"
		self.page
		self.soup
		self.courses
		self.db

	def scrape(self):
		self.page = urllib3.urlopen(url)
		self.soup = BeautifulSoup(page, 'html.parser').find_all(True)

		for drop in self.soup

		self.courses = soup.find_all("a")

		for course in self.courses:
			course = re.findall('"([^"]+)"', str(course))
			if "CS" in course:

    #fill




data.scrape()







# f = open("prettified-cs.html", "w")
# f.write(str(soup))
# f.close()

print ("done")