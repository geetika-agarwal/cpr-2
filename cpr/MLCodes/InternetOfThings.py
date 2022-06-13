import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics


def internetOfThingsFunc(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    internetOfThings = pd.read_csv(
        "cpr\Datasets\Internet Of Things.csv", header=None)

    internetOfThings.loc[0] = skillList

    for i in range(16):
        internetOfThings[i] = internetOfThings[i].astype(
            str).str.lower()

    encoder = OrdinalEncoder()
    encoder.fit(internetOfThings)

    internetOfThings_encoded = encoder.transform(
        internetOfThings)
    internetOfThings_encoded = np.nan_to_num(
        internetOfThings_encoded)

    skillList = internetOfThings_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\internetOfThings_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(internetOfThings_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    internetOfThings_num = pd.read_csv(
        "cpr\Datasets\internetOfThings_Encoded.csv", header=None, names=col_names)

    internetOfThings_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = internetOfThings_num[features_col].values
    y = internetOfThings_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    internetOfThings_list = internetOfThings_num.values.tolist()

    rowN = -1
    for row in range(0, len(internetOfThings_list)):
        if result == int(internetOfThings_list[row][15]):
            rowN = row
            break

    internetOfThingsResult = encoder.inverse_transform(
        internetOfThings_encoded).tolist()

    return internetOfThingsResult[rowN][15]
