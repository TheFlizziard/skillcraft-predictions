import numpy as np
import pandas as pd
import sklearn as sk

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

def preprocessing():
    """
    Description: Load the dataset and preprocess it
    Return: Preprocessed dataset
    """
    data = pd.read_csv("SkillCraft1_Dataset.csv")
    
    league_names = {1 : 'Bronze', 2 : 'Silver', 3 : 'Gold', 4 : 'Platinum',
                5 : 'Diamond', 6 : 'Master', 7 : 'GrandMaster', 8 : 'Professional'}
    data['LeagueName'] = data['LeagueIndex'].map(league_names)

    data = clean_data(data)

    return data

def clean_data(data):
    """
    Description: Remove and rearange the data
    Input: data -> dataset to clean
    Return: Cleaned dataset
    """
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
    """
    Description: Apply a RandomForest classifier
    Input:  X -> data to train
            Y -> labels for training
            input -> data to predict
    Return: Prediction of the input, 3 k-fold cross validation score
    """
    rf = RandomForestClassifier(criterion='gini', max_features='sqrt', n_estimators=200, oob_score=True)

    cv_rf = cross_val_score(rf, X, Y, cv=3)
    score = round(cv_rf.mean(), 3)

    rf.fit(X, Y)
    pred = rf.predict(input)

    return pred, score

def model(data, input, all_features, predict_rank):
    """"
    Description: Function called to apply a ML model
    Input:  data -> data used for training
            input -> data to predict
            all_features -> boolean telling us if we use all the features or only important ones
            predict_rank -> boolean telling us if we want to predict the exact rank or group
    Return: Prediction and score of the model 
    """
    features = feature_selection(all_features)

    input_df = pd.DataFrame(dict(zip(features, input)), index=[0])

    X = data[features]
    Y = get_Y(data, predict_rank)

    pred, score = apply_model(X, Y, input_df)

    return pred, score

def feature_selection(all_features):
    """
    Description: Function defining which features to use
    Input: all_features -> boolean telling us if we use all the features or only the important ones
    Return: A list of the features we keep
    """
    if all_features:
        features = ['Age', 'HoursPerWeek', 'TotalHours', 'APM', 'SelectByHotkeys', 'AssignToHotkeys','UniqueHotkeys',
            'MinimapAttacks', 'MinimapRightClicks', 'NumberOfPACs','GapBetweenPACs', 'ActionLatency', 'ActionsInPAC', 
            'TotalMapExplored', 'WorkersMade', 'UniqueUnitsMade', 'ComplexUnitsMade','ComplexAbilitiesUsed']
    else:
        features = ['APM', 'SelectByHotkeys', 'AssignToHotkeys', 'ActionLatency', 'GapBetweenPACs']
    
    return features

def get_Y(data, rank):
    """
    Description: Function defining which prediction we want
    Input:  data -> data 
            rank -> boolean telling us if we want to predict the exact rank or its group
    Return: A list of the corresponding rank/group od the data
    """
    if rank:
        Y = data['LeagueName']
    else:
        group3 = {'Bronze' : 'novice', 'Silver' : 'novice',
          'Gold' : 'expert', 'Platinum' : 'expert', 'Diamond' : 'expert',
          'Master' : 'pro', 'GrandMaster' : 'pro', 'Professional' : 'pro'}
        data['Group3'] = data['LeagueName'].map(group3)

        Y = data['Group3']

    return Y
