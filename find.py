from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from time import time
from flask import Flask, request, render_template,send_from_directory
import matplotlib.pyplot as plt
import llcount as ll
import find_img as fi
import os
import random
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route("/output", methods=['POST'])
def get_data():
	if request.method == "POST":
		players = request.form.getlist('check')
		ur = dict()
		q=[]
		#print(players)
		f = open("data.txt","w")
		for link in players:
			
			imgcount= fi.find_image(link)
			load_time=ll.get_load_time(link)
			linkcount=ll.get_link_count(link)
			contentcount=ll.get_content_count(link)
			l = []
			l.append(load_time)
			l.append(imgcount)
			l.append(linkcount)
			l.append(contentcount)
			q.append(l)
			f.write(str(link))
			f.write(" ")
			for i in l:
				f.write(str(i))
				f.write(" ")
			f.write("\n")

			ur[link]=l
		f.close()
		x=[1,2,3,4]
		plt.plot(x,q[0], label = "link 1") 
		plt.plot(x,q[1], label = "link 2") 
				
		plt.xlabel('x - axis') 
# naming the y axis 
		plt.ylabel('y - axis') 
		i=random.randint(10,100)
# giving a title to my graph 
		plt.title('Difference of web pages')
		target = os.path.join(APP_ROOT,'images/')
		print(target)
		if not os.path.isdir(target):
			os.mkdir(target)
		else:
			print('could\'nt create directory')
		filename=str(i)+".png"
		destination = "/".join([target,filename])
		print('saving it to ',destination)
		print('incoming file',filename)
		i=i+1
		#plt.show()
		plt.legend()
		plt.savefig(destination)
		#print(ur)
		#ur = { i : players[i] for i in range(0, len(players) ) }
		#ur=query
	return render_template("output.html",ur=ur,img_name=filename)
@app.route('/output/<filename>')
def send_image(filename):
	return send_from_directory("images",filename) 			
             

if __name__ == "__main__":
    app.run(port=80,debug =True)

