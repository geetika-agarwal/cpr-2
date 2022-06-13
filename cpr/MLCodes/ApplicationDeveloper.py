import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder


def ApplicationDeveloperFunct(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    applicationDeveloper = pd.read_csv(
        "cpr\Datasets\Application Developer.csv", header=None)

    applicationDeveloper.loc[0] = skillList

    for i in range(16):
        applicationDeveloper[i] = applicationDeveloper[i].str.lower()

    encoder = OrdinalEncoder()
    encoder.fit(applicationDeveloper)

    applicationDeveloper_encoded = encoder.transform(applicationDeveloper)
    applicationDeveloper_encoded = np.nan_to_num(applicationDeveloper_encoded)

    skillList = applicationDeveloper_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\ApplicationDeveloper_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(applicationDeveloper_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    applicationDeveloper_num = pd.read_csv(
        "cpr\Datasets\ApplicationDeveloper_Encoded.csv", header=None, names=col_names)

    applicationDeveloper_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = applicationDeveloper_num[features_col].values
    y = applicationDeveloper_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    applicationDeveloper_list = applicationDeveloper_num.values.tolist()

    rowN = -1
    for row in range(0, len(applicationDeveloper_list)):
        if result == int(applicationDeveloper_list[row][15]):
            rowN = row
            break

    applicationDeveloperResult = encoder.inverse_transform(
        applicationDeveloper_num).tolist()

    return applicationDeveloperResult[rowN][15]
