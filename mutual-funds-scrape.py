from bs4 import BeautifulSoup
from selenium import webdriver

url="https://www.tdassetmanagement.com/fundDetails.form?fundId=818&prodGroupId=1&lang=en&site=TDCT"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.implicitly_wait(1)
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, "lxml")

parentdiv = str(soup.findAll("div", {"class": "td-layout-grid9 td-layout-column td-layout-column-first"}))
start = parentdiv.find("<strong>") + 8
end = parentdiv.find("</strong>")

price = parentdiv[start:end]
end = price.find("\\")
realprice = price[1:end]

print (realprice)