from bs4 import BeautifulSoup
import re
import urllib2
import pymongo

client = MongoClient('localhost')
DB = courses.cs
posts = DB.posts


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

	def browse(self):

	def scrape(self):
		self.page = urllib2.urlopen(url)
		self.soup = BeautifulSoup(page, 'html.parser').find_all(True)

		for drop in self.soup

		self.courses = soup.find_all("a")

		for course in self.courses:
			course = re.findall('"([^"]+)"', str(course))
			if "CS" in course:


	def initDB(self):





# f = open("prettified-cs.html", "w")
# f.write(str(soup))
# f.close()

print ("done")