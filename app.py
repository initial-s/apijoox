from flask import Flask,json,request
import src

joox = src.Object()
app = Flask(__name__)

@app.route('/',methods=['GET'])
def get_home():
	return ("Berhasil")

@app.route('/api/joox/search',methods=['GET'])
def get_searchResults():
	if 'q' in request.args:
		results = joox.searchResults(keywords=request.args['q'])
		return json.dumps({"results":results, "status":200})

@app.route('/api/joox/songid',methods=['GET'])
def get_songinfoResults():
	if 'q' in request.args:
		results  = joox.songinfoResults(songid=request.args['q'])
		return json.dumps({"results":results, "status":200})

if __name__ == "__main__":
	app.run(debug=True)