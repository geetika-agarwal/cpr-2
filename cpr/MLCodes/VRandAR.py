import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics


def VRandARFunc(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    vrAndAr = pd.read_csv(
        "cpr\Datasets\Virtual Reality and Augmented Reality.csv", header=None)

    vrAndAr.loc[0] = skillList

    for i in range(16):
        vrAndAr[i] = vrAndAr[i].astype(
            str).str.lower()

    encoder = OrdinalEncoder()
    encoder.fit(vrAndAr)

    vrAndAr_encoded = encoder.transform(
        vrAndAr)
    vrAndAr_encoded = np.nan_to_num(
        vrAndAr_encoded)

    skillList = vrAndAr_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\VrAndAr_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(vrAndAr_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    vrAndAr_num = pd.read_csv(
        "cpr\Datasets\VrAndAr_Encoded.csv", header=None, names=col_names)

    vrAndAr_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = vrAndAr_num[features_col].values
    y = vrAndAr_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    vrAndAr_list = vrAndAr_num.values.tolist()

    rowN = -1
    for row in range(0, len(vrAndAr_list)):
        if result == int(vrAndAr_list[row][15]):
            rowN = row
            break

    vrAndArResult = encoder.inverse_transform(
        vrAndAr_encoded).tolist()

    return vrAndArResult[rowN][15]
