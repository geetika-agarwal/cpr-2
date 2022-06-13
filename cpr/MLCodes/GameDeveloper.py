import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics


def GameDeveloperFunc(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    gameDeveloper = pd.read_csv(
        "cpr\Datasets\Game Developer.csv", header=None)

    gameDeveloper.loc[0] = skillList

    for i in range(16):
        gameDeveloper[i] = gameDeveloper[i].astype(
            str).str.lower()

    encoder = OrdinalEncoder()
    encoder.fit(gameDeveloper)

    gameDeveloper_encoded = encoder.transform(
        gameDeveloper)
    gameDeveloper_encoded = np.nan_to_num(
        gameDeveloper_encoded)

    skillList = gameDeveloper_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\gameDeveloper_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(gameDeveloper_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    gameDeveloper_num = pd.read_csv(
        "cpr\Datasets\gameDeveloper_Encoded.csv", header=None, names=col_names)

    gameDeveloper_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = gameDeveloper_num[features_col].values
    y = gameDeveloper_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    gameDeveloper_list = gameDeveloper_num.values.tolist()

    rowN = -1
    for row in range(0, len(gameDeveloper_list)):
        if result == int(gameDeveloper_list[row][15]):
            rowN = row
            break

    gameDeveloperResult = encoder.inverse_transform(
        gameDeveloper_num).tolist()

    return gameDeveloperResult[rowN][15]
