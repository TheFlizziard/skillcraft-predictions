from flask import Flask, render_template, request, flash, url_for, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

# To launch the hello world api, do in cmd: 
## export FLASK_APP=api/app
## export FLASK_ENV=development
## flask run
## CTRL+C to stop 
# Go to http://127.0.0.1:5000/

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prediction', methods=('GET', 'POST'))
def prediction():
    if request.method == 'POST':
        feature1 = request.form['feature1']
        feature2 = request.form['feature2']

        if not feature1:
            flash('feature1 is required !')
        elif not feature2:
            flash('feature2 is required !')
        else:
            print(f'Title : {feature1}')
            print(f'Content : {feature2}')
            return redirect(url_for('index'))

    return render_template('prediction.html')