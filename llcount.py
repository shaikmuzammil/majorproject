import urllib.request
from time import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
def get_load_time(link):
	req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
	stream = urlopen(req)
	start_time = time()
	output = stream.read()
	end_time = time()
	stream.close()
	return end_time-start_time
	

def get_link_count(link):
	req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
	html = urlopen(req).read()
	#html = urlopen(link)
	bsObj = BeautifulSoup(html);
	count=0
	for link in bsObj.find_all('a'):
	    count=count+1
	    #print(link.get('href'))
	return count

def get_content_count(link):
	req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
	content = urlopen(req).read()
	soup = BeautifulSoup(content,'html.parser')
	a=(soup.get_text())
	b=a.split(' ')
	return len(b)
