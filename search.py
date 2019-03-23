from googlesearch import search
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/display", methods=["GET", "POST"])
def get_data():
	if request.method == "POST":
		query = request.form["search"]
		urls = dict()
		i=1
		for url in search(query, tld="co.in", num=10, stop=1, pause=2):
			urls[i]=url;
			i = i+1
	return render_template("display.html",urls=urls)
			
             

if __name__ == "__main__":
    app.run(debug =True)

