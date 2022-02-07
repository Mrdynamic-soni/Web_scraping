# library used to perform action
import xlrd
# from posixpath import split
import requests
import html5lib
from bs4 import BeautifulSoup

#User agent to tell website that it's a person  not a bot
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

#opening excel file where all the links are stored
wb = xlrd.open_workbook("C:\\Users\\Acer\\Desktop\\assignment\\input.xlsx")  #opening complete workbook
sheet = wb.sheet_by_index(0)    #opening particular worksheet i.e. excel
sheet.cell_value(0,0)  #initial point of excel


#iterraing on the  link to get the websites to get the data
#thid below code is to iterating over the whole excel file and iterating over every links provided there and scraping data from website and storing that data into txt file for firther analysis
for i in range(1,sheet.nrows+1): 
    print(sheet.cell_value(i,1)) # printing the data on thta particular cell
    url = sheet.cell_value(i,1)  # storing that data in url to extract data in file
    req = requests.get(url,headers=headers) # hitting wesite to scrape the data from that particular website
    soup = BeautifulSoup(req.text,"html.parser")  # #using bs4 library to beautify the data scraaped from website
    with open(f"C:\\Users\\Acer\\Desktop\\assignment\\scraped_files\\{i}.txt","a", encoding='UTF-8')as file:  # creating diffirent file with filename as i.txt to store the scraped data from website
        for item in soup.find_all('p'): #iterating over the website data 
            print(item.get_text())  # printing extractred data 
            file.write(item.get_text()) # append data in file
            file.write("\n")
