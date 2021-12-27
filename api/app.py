from flask import Flask, render_template, request, flash, url_for, redirect

from models import preprocessing, model_important_features

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

        APM = float(request.form['APM'])
        SelectByHotkeys = float(request.form['SelectByHotkeys'])
        AssignToHotkeys = float(request.form['AssignToHotkeys'])
        ActionLatency = float(request.form['ActionLatency'])
        GapBetweenPACs = float(request.form['GapBetweenPACs'])

        input = [APM, SelectByHotkeys, AssignToHotkeys, ActionLatency, GapBetweenPACs]

        if not APM:
            flash('APM is required !')
        else:
            print(f'APM : {APM, type(APM), type(float(APM))}')
            
            data = preprocessing()
            pred, score = model_important_features(data, input)
            print(f'You have been predicted {pred} with a precision of {score}%')
            
            return redirect(url_for('index'))

    return render_template('prediction.html')
