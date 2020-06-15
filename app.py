from flask import Flask,render_template,redirect,request
import predict
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def traffic():
	if request.method=='POST':
		f=request.files['userfile']
		path="./static/{}".format(f.filename)
		f.save(path)
		output=predict.trafficsign(path)
		result_dic={
		'image'  : path,
		'output' : output
		}
	return render_template('index.html' , result=result_dic)

if __name__ == "__main__":
    app.run(debug=True)
