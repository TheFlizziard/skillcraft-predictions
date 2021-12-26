from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

# To launch the hello world api, do in cmd: 
# export FLASK_APP=hello
# export FLASK_ENV=development
# flask run