import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.request import urlopen



def location(filePath):
	searchUrl = 'http://www.google.hr/searchbyimage/upload'
	multipart = {'encoded_image': (filePath, open(filePath, 'rb'))}
	response = requests.post(searchUrl, files=multipart, allow_redirects=False)
	
	fetchUrl = response.headers['Location']


	chrome_options = Options()  
	chrome_options.add_argument("--headless")      
	driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
	driver.get(fetchUrl)
	source = driver.page_source
	
	
	soup = BeautifulSoup(source,features="html5lib")
	
	

	#result = source.find('h" value="')
	result = soup.find('div', attrs = {'class' : 'kno-rdesc'})

	#print(soup)
	#kno-rdesc
	#document.getElementsByClassName("kno-rdesc")[0].textContent
	article=""
	
	for i in result:
		print(i.text)

	for i in result:
		
		article = article + i.text
		

    		
	article = article.replace('Description',"")
	article = article.replace('Wikipedia',"")
	ans = article
	
	return ans 


