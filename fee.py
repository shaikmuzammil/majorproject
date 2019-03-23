from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from time import *
from flask import Flask, request, render_template
import matplotlib.pyplot as plt
from itertools import chain
import threading
import os
app = Flask(__name__)
@app.route("/feed", methods=["GET", "POST"])
def get_feed():
	if request.method == "POST":
		lines = [line.rstrip('\n') for line in open('data.txt')]
		d = dict()
		count=0
		for line in lines:
			l = line.split(' ')
			d[count]=l
			count = count+1
		print(d)

	#return "ok"
	'''ab=request.form.getlist("ke")
		bc=request.form.getlist("va")
		bq=request.form.getlist("vb")
		bw=request.form.getlist("vc")
		
		y=[bc[0],bq[0],bw[0]]
		x=[bc[1],bq[1],bw[1]]
		#z=[bc[2],bq[2],bw[2]]
		i = [float(q) for q in y]
		r = [float(f) for f in x]
		#c = [float(t) for t in z]
		#plt.text(-0.5, -0.25, 'Brackmard minimum')

		plt.plot(i,label='linkone')
		plt.plot(r,label='linktwo')
		#plt.plot(c)
		plt.savefig('images\\myfig.png')
		#plt.show()
		#print(ab)
		ur = dict()
		l=[(i,ab[i]) for i in range(len(ab))]
		ur=dict(l)
		#ur = { i : ab[i] for i in range(0, len(ab) ) }
		print(ur)
		full_filename = os.path.join(app.config['images'], 'shovon.jpg')

		
'''
	return render_template("feed.html",ur=d)
	    


if __name__ == "__main__":
    app.run(port=5010,debug =True)
    