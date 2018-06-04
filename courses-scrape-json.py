import pandas as pd
import requests
from bs4 import BeautifulSoup


res = requests.get("http://www.ucalendar.uwaterloo.ca/1819/COURSE/course-CS.html")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')
df = pd.read_html(str(table))
print(df)
