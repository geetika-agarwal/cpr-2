import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics


def DevOpsFunc(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    devOps = pd.read_csv(
        "cpr\Datasets\DevOps.csv", header=None)

    devOps.loc[0] = skillList

    for i in range(16):
        devOps[i] = devOps[i].astype(
            str).str.lower()

    encoder = OrdinalEncoder()
    encoder.fit(devOps)

    devOps_encoded = encoder.transform(
        devOps)
    devOps_encoded = np.nan_to_num(
        devOps_encoded)

    skillList = devOps_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\devOps_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(devOps_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    devOps_num = pd.read_csv(
        "cpr\Datasets\devOps_Encoded.csv", header=None, names=col_names)

    devOps_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = devOps_num[features_col].values
    y = devOps_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    devOps_list = devOps_num.values.tolist()

    rowN = -1
    for row in range(0, len(devOps_list)):
        if result == int(devOps_list[row][15]):
            rowN = row
            break

    devOpsResult = encoder.inverse_transform(
        devOps_num).tolist()

    return devOpsResult[rowN][15]
