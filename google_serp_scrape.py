from bs4 import BeautifulSoup
from datetime import date
import requests
import csv

question = input('What info would you like to gain? ')
question = question.replace(" ","+")
today = date.today()

source = requests.get(f"https://www.google.com/search?q={question}").text

csv_file = open(f"{question}_serp_{today}.csv", 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Rank','Meta-Title','URL','Meta-Description'])

soup = BeautifulSoup(source, 'lxml')

meta_title = []
headlines = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
for headline in headlines:
    #print(headline.text)
    meta_title.append(headline.text)
    
meta_title.insert(0,'0')
    
print()
url = []
links = soup.find_all("div", class_="BNeawe UPmit AP7Wnd")
for link in links:
    #print(link.text)
    link = link.text
    link = link.replace(" › ","/")
    url.append(link)   
url.insert(0,'0')


meta_list = []

descriptions = soup.find_all("div", "s3v9rd")
for desc in descriptions:
    meta_list.append(desc.text)
    
del meta_list[1::2]
meta_list.insert(0,'0')



for n in range(1,11):
    print(n)
    title = meta_title[n]
    domain = url[n]
    meta_desc = meta_list[n]
    print(title)
    print(domain)
    print(meta_desc)
    print()
    csv_writer.writerow([n,title,domain,meta_desc])

csv_file.close()
