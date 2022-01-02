from flask import Flask, render_template, request, flash, url_for, redirect

from models import preprocessing, model

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

        # Request the type of model: the number of features and the type of prediction
        all_features = True if request.form['features'] == 'all_features' else False
        predict_rank = True if request.form['rank'] == 'rank' else False

        # Request the features
        APM = request.form['APM']
        SelectByHotkeys = request.form['SelectByHotkeys']
        AssignToHotkeys = request.form['AssignToHotkeys']
        ActionLatency = request.form['ActionLatency']
        GapBetweenPACs = request.form['GapBetweenPACs']
        input = [APM, SelectByHotkeys, AssignToHotkeys, ActionLatency, GapBetweenPACs]

        if '' in input:
            flash('All important features are required !')
        else:

            input = map(float, input)
            data = preprocessing()

            pred, score = model(data, input, all_features, predict_rank)

            print(f'You have been predicted {pred[0]} with a precision of {score}%')
            
            return redirect(url_for('result', score=score, pred=pred[0]))

    return render_template('prediction.html')

@app.route('/prediction/result/<float:score>/<string:pred>')
def result(score, pred):

    res = {'score': score, 'pred': pred}

    return render_template('result.html', res=res)