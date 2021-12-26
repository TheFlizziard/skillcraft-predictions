from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# To launch the hello world api, do in cmd: 
## export FLASK_APP=api/hello
## export FLASK_ENV=development
## flask run
## CTRL+C to stop 
# Go to http://127.0.0.1:5000/