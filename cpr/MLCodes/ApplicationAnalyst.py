import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder


def ApplicationAnalystFunc(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    applicationAnalyst = pd.read_csv(
        "cpr\Datasets\Application Analyst.csv", header=None)

    applicationAnalyst.loc[0] = skillList

    for i in range(16):
        applicationAnalyst[i] = applicationAnalyst[i].str.lower()

    encoder = OrdinalEncoder()
    encoder.fit(applicationAnalyst)

    applicationAnalyst_encoded = encoder.transform(applicationAnalyst)
    applicationAnalyst_encoded = np.nan_to_num(applicationAnalyst_encoded)

    skillList = applicationAnalyst_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\ApplicationAnalyst_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(applicationAnalyst_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    applicationAnalyst_num = pd.read_csv(
        "cpr\Datasets\ApplicationAnalyst_Encoded.csv", header=None, names=col_names)

    applicationAnalyst_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = applicationAnalyst_num[features_col].values
    y = applicationAnalyst_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    applicationAnalyst_list = applicationAnalyst_num.values.tolist()

    rowN = -1
    for row in range(0, len(applicationAnalyst_list)):
        if result == int(applicationAnalyst_list[row][15]):
            rowN = row
            break

    applicationAnalystResult = encoder.inverse_transform(
        applicationAnalyst_num).tolist()

    return applicationAnalystResult[rowN][15]
