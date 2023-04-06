#===============================================
#I heard that Beautiful soup is a nice way of making
#web-scrapers. So I will look into that.
#===============================================
import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)
