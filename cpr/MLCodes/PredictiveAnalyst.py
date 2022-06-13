import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics


def PredictiveAnalystFunc(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    predictiveAnalyst = pd.read_csv(
        "cpr\Datasets\Predictive Analytics.csv", header=None)

    predictiveAnalyst.loc[0] = skillList

    for i in range(16):
        predictiveAnalyst[i] = predictiveAnalyst[i].astype(
            str).str.lower()

    encoder = OrdinalEncoder()
    encoder.fit(predictiveAnalyst)

    predictiveAnalyst_encoded = encoder.transform(
        predictiveAnalyst)
    predictiveAnalyst_encoded = np.nan_to_num(
        predictiveAnalyst_encoded)

    skillList = predictiveAnalyst_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\predictiveAnalyst_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(predictiveAnalyst_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    predictiveAnalyst_num = pd.read_csv(
        "cpr\Datasets\predictiveAnalyst_Encoded.csv", header=None, names=col_names)

    predictiveAnalyst_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = predictiveAnalyst_num[features_col].values
    y = predictiveAnalyst_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    predictiveAnalyst_list = predictiveAnalyst_num.values.tolist()

    rowN = -1
    for row in range(0, len(predictiveAnalyst_list)):
        if result == int(predictiveAnalyst_list[row][15]):
            rowN = row
            break

    predictiveAnalystResult = encoder.inverse_transform(
        predictiveAnalyst_num).tolist()

    return predictiveAnalystResult[rowN][15]
