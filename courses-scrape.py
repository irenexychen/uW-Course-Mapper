from bs4 import BeautifulSoup
import re
import urllib2
import pymongo

client = MongoClient('localhost')
db = courses.cs
posts = db.posts


class Post(Document):
    course_name = StringField(required=True)
    prereq = StringField(required=False)
    antireq = StringField(required=False)
    desc = DateTimeField(required=True)



url = "http://www.ucalendar.uwaterloo.ca/1819/COURSE/course-CS.html"

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

courses = soup.find_all("a")
for course in courses:
	course = re.findall('"([^"]+)"', str(course))
	if "CS" in course:



# f = open("prettified-cs.html", "w")
# f.write(str(soup))
# f.close()

print ("done")