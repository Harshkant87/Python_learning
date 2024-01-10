import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/", verify=False)
content = req.content
soup = BeautifulSoup(content, "html.parser")

# print(soup.prettify())
all = soup.find_all("div", {"class" : "property-card-primary-info"})
print(all)
