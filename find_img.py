import requests
import re
def find_image(s):
	website = requests.get(s)
	html = website.text
	pat = re.compile(r'<\s*img [^>]*src="([^"]+)')
	img = pat.findall(html)
	#count =0
	#for i in range(img):

	#    count=count+1;
	return len(img)
