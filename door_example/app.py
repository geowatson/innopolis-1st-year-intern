from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/init')
def init():
    print("New user connect " + str(request.environ['REMOTE_ADDR']))
    return "none"

@app.route('/')
def home():
    print("Requested to open door with ID#" + request.args["door_id"], "\nUser name:", request.args["name"])
    return "none"


if __name__ =="__main__":
    # put host ip here
    app.run(debug=True,port=8080,host='10.91.42.90')
