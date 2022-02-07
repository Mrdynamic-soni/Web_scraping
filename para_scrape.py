#import libraries 
import requests
from bs4 import BeautifulSoup

#User agent to tell website that it's a person  not a bot
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
#path/url of website
url ="https://insights.blackcoffer.com/how-is-login-logout-time-tracking-for-employees-in-office-done-by-ai/"

#scraping data from website 
req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text,"html.parser")

file = open("data.text","a")
for item in soup.find_all('p'): #iterating over the website data 
            print(item.get_text())  # printing extractred data 
            file.write(item.get_text()) #append data in file 