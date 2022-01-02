# skillcraft-predictions

## Introduction

This project is an university project which constists of analyzing a given dataset and answer to a problematic.

As a team of two students, we worked on a dataset that contains datas about players statistics on the famous game Starcraft II, developped by Blizzard Entertainment.

This project is coded in Python 3.9.9 and is composed of a Jupyter Notebook file, with the detailed process and analysis, and a basic flask API to predict players rank.

### Goal

The goal of this project is to try to predict the rank of any Starcraft II players based on their statistics on the game.

Our dataset can be found here: https://archive.ics.uci.edu/ml/datasets/SkillCraft1+Master+Table+Dataset

### Librairies needed

To be able to run the code on python, you will need to install the following librairies:
- numpy
- pandas
- sklearn
- matplotlib
- plotly

##




## flask API

### How to use it

To use the flask API and get your predicted rank, you should do as follow in the the project folder:

- export FLASK_APP=api/app
- export FLASK_ENV=development
- flask run
- CTRL+C to stop 
- Go to http://127.0.0.1:5000/

Be sure to have flask installed on your computer first.

### Result

## PUT SOME IMAGES OF WEB PAGE
Our flask API is made of three HTML pages:

- index HTML page: welcome and introduction page 
- prediction HTML page: page that allows us to choose what kind of prediction we want and to put our in-game statistics
- result HTML page: page that shows us our prediction rank based on the input we made in the prediction HTML page.

