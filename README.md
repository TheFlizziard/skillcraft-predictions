# skillcraft-predictions

By BESSIS Hugo and BLANOT Antoine, Dec 2021

## Introduction

This project is an university project which constists of analyzing a given dataset with Python and answering a problematic.

As a team of two students, we worked on a dataset that contains datas about players statistics on the famous game Starcraft II, developped by Blizzard Entertainment.
The dataset is made of 3395 observations and 20 variables, where `LeagueIndex` is the label and other variables are features.

This project is coded in Python 3.9 and is composed of a Jupyter Notebook file, with the detailed process and analysis explained in it, and a basic flask API to predict players rank.

### Goal

The goal of this project is to try to predict the rank of any Starcraft II players based on their statistics on the game.

Our dataset can be found here: https://archive.ics.uci.edu/ml/datasets/SkillCraft1+Master+Table+Dataset

### Requirements

To run the code and see the result you will need:
- Python 3.9
- Jupyter Notebook
- flask

To be able to run the code on python, you will need to install the following Python packages:
- numpy
- pandas
- sklearn
- matplotlib
- plotly

## Result

Here are the results of our models prediction on ranks:

- KNN Classifier model : around 38%
- SVC model: around 39%
- LDA model: around 40%
- Random Forest Classifier model: around 42%

All these models have a low accuracy (around 40%) which is obviously not enough at all for a decent ranking prediction.

Here are the results for the supervised learning over two, three and four rank groups:

- Random Forest Classifier on 4 predefined groups: around 69%
- Random Forest Classifier on 3 predefined groups: around 75%
- Random Forest Classifier on 2 predefined groups: around 80%

The accuracy for 3 and 4 groups are good and interesting, but the 2 grouping one is not interesting to study even if it has the highest score. Using the 4 groups model seems to be the best since the Gold leagues is not in the same group than the Diamond league and as player, we know there is a high gap of level and expertise between these two leagues.

## Conclusion

With our dataset, we can not predict exactly the rank of any Starcraft II players. Maybe because we need other features that can explained more the rank of a player or maybe because it's not possible with our knowledge to predict it precisely.

However, with the data we have, we can try to get an idea of a player's level by grouping up the leagues together and forming new groups. 
Knowing that, we can ask ourselves if the leagues in this game are well deifned or not. Some of them could be irrelevant because of the gap of level between players in the same league. We could maybe imagine another ranking system with more or less leagues. Another model of ranking could give us a better rank prediction model.



## flask API

### How to use it

To use the flask API and get your predicted rank, you should do as follows in the the project folder:

Bash:

- export FLASK_APP=api/app
- export FLASK_ENV=development
- flask run
- Go to http://127.0.0.1:5000/

Command prompt (CMD):

- set FLASK_APP=api/app
- set FLASK_ENV=development
- flask run
- Go to http://127.0.0.1:5000/


Press CTRL+C to stop.

Be sure to have flask installed on your computer first.

### HTML result

## PUT SOME IMAGES OF WEB PAGE
Our flask API is made of three HTML pages:

- index HTML page: welcome and introduction page 
- prediction HTML page: page that allows us to choose what kind of prediction we want and to put our in-game statistics
- result HTML page: page that shows us our prediction rank based on the input we made in the prediction HTML page.

![alt text](./images/prediction_html_page.PNG?raw=true)
![alt text](./images/result_html_page.PNG?raw=true)


## Credits

Team members:
- BESSIS Hugo - Engineering student at ESILV - Social media: https://github.com/TheFlizziard
- BLANOT Antoine - Engineering student at ESILV - Social media: https://github.com/AntoineBlanot 


## License

This project is under MIT License. See the LICENCE.txt file for more information.




