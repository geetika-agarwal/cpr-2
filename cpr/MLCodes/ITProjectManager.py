import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics


def ITProjectManagerFunc(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    itProjectManager = pd.read_csv(
        "cpr\Datasets\IT Project Manager.csv", header=None)

    itProjectManager.loc[0] = skillList

    for i in range(16):
        itProjectManager[i] = itProjectManager[i].astype(
            str).str.lower()

    encoder = OrdinalEncoder()
    encoder.fit(itProjectManager)

    itProjectManager_encoded = encoder.transform(
        itProjectManager)
    itProjectManager_encoded = np.nan_to_num(
        itProjectManager_encoded)

    skillList = itProjectManager_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\itProjectManager_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(itProjectManager_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    itProjectManager_num = pd.read_csv(
        "cpr\Datasets\itProjectManager_Encoded.csv", header=None, names=col_names)

    itProjectManager_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = itProjectManager_num[features_col].values
    y = itProjectManager_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    itProjectManager_list = itProjectManager_num.values.tolist()

    rowN = -1
    for row in range(0, len(itProjectManager_list)):
        if result == int(itProjectManager_list[row][15]):
            rowN = row
            break

    itProjectManagerResult = encoder.inverse_transform(
        itProjectManager_num).tolist()

    return itProjectManagerResult[rowN][15]
