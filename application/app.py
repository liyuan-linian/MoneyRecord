from flask import Flask,jsonify,request
from  flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)
@app.route('/')
def index():
    return 'fuck'

@app.route('/test/get',methods=["GET"])
def login():
    return jsonify({ "name" : "petter" , "password": 123456 })

@app.route("/test/post",methods=["POST"])
def post_task():
    data = request.get_json()
    print(data)
    return jsonify({ "name" : "petter" , "password": 123456 })

if __name__ == "__main__":
    app.run(debug=True)