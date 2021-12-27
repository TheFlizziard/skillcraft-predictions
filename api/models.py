import numpy as np
import pandas as pd
import sklearn as sk

from sklearn.ensemble import RandomForestClassifier

def preprocessing():
    data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00272/SkillCraft1_Dataset.csv")
    
    league_names = {1 : 'Bronze', 2 : 'Silver', 3 : 'Gold', 4 : 'Platinum',
                5 : 'Diamond', 6 : 'Master', 7 : 'GrandMaster', 8 : 'Professional'}
    data['LeagueName'] = data['LeagueIndex'].map(league_names)

    data = clean_data(data)

    return data

def clean_data(data):
    cols = data.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    cols = [cols[1]] + [cols[0]] + cols[2:]
    data = data[cols]

    data.replace('?', np.NaN, inplace=True)
    data = data.astype({'Age': float, 'HoursPerWeek' : float, 'TotalHours': float})

    age_mean = data['Age'].mean()
    hours_per_week_mean = data['HoursPerWeek'].mean()
    total_hours_mean = data['TotalHours'].mean()
    data['Age'].replace(np.NaN, age_mean, inplace=True)
    data['HoursPerWeek'].replace(np.NaN, hours_per_week_mean, inplace=True)
    data['TotalHours'].replace(np.NaN, total_hours_mean, inplace=True)

    data.drop([690], inplace= True)
    data.drop([1793,2324], inplace= True)

    return data

def apply_model(X, Y, input):

    rf = RandomForestClassifier(criterion='gini', max_features='sqrt', n_estimators=200, oob_score=True)
    rf.fit(X, Y)
    score = rf.score(X, Y)
    pred = rf.predict(input)

    return pred, score


def model_important_features(data, input):

    imp_features = ['APM', 'SelectByHotkeys', 'AssignToHotkeys', 'ActionLatency', 'GapBetweenPACs']
    input_df = pd.DataFrame(dict(zip(imp_features, input)))

    X = data[imp_features]
    Y = data['LeagueName']

    pred, score = apply_model(X, Y, input_df)

    return pred, score
