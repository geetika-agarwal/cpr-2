import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics


def CybersecurityFunc(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    cyberSecurity = pd.read_csv(
        "cpr\Datasets\CyberSecurity.csv", header=None)

    cyberSecurity.loc[0] = skillList

    for i in range(16):
        cyberSecurity[i] = cyberSecurity[i].str.lower(
        )

    encoder = OrdinalEncoder()
    encoder.fit(cyberSecurity)

    cyberSecurity_encoded = encoder.transform(
        cyberSecurity)
    cyberSecurity_encoded = np.nan_to_num(
        cyberSecurity_encoded)

    skillList = cyberSecurity_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\cyberSecurity_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(cyberSecurity_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    cyberSecurity_num = pd.read_csv(
        "cpr\Datasets\cyberSecurity_Encoded.csv", header=None, names=col_names)

    cyberSecurity_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = cyberSecurity_num[features_col].values
    y = cyberSecurity_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    cyberSecurity_list = cyberSecurity_num.values.tolist()

    rowN = -1
    for row in range(0, len(cyberSecurity_list)):
        if result == int(cyberSecurity_list[row][15]):
            rowN = row
            break

    cyberSecurityResult = encoder.inverse_transform(
        cyberSecurity_num).tolist()

    return cyberSecurityResult[rowN][15]
