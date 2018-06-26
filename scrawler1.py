#from collections import OrderedDict
from bs4 import BeautifulSoup
import requests
source = requests.get('https://www.naukri.com/java-jobs').text
soup=BeautifulSoup(source,'html.parser')
javajob=[]
for desc in soup.find_all('a',attrs={'class':['content']}):
	a=dict()
	a['count']=int(desc['count'])
	a['designation']=desc.find('li',attrs={'class':['desig']}).text
	a['company_name']=desc.find('span',attrs={'class':['org']}).text
	a['experience']=desc.find('span',attrs={'class':['exp']}).text
	a['location']=desc.find('span',attrs={'class':['loc']}).text
	a['comp_descr']=desc.find('span',attrs={'class':['org']}).text+desc.find('span',attrs={'class':['loc']}).text
	

	url=desc['href']
	desc_url = requests.get(url).text
	url_soup=BeautifulSoup(desc_url,'html.parser')
	for comp_desc in url_soup.find_all('span',attrs={'itemprop':['description']}):
		a.update({'comp_descr': comp_desc.find('div',attrs={'class':['discp']}).text}) 
	

	javajob.append(a)
#print javajob
	
		
	


	


