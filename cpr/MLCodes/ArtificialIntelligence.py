import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics


def ArtificialIntelligenceFunc(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    artificialIntelligence = pd.read_csv(
        "cpr\Datasets\Artificial Intelligence.csv", header=None)

    artificialIntelligence.loc[0] = skillList

    for i in range(16):
        artificialIntelligence[i] = artificialIntelligence[i].astype(
            str).str.lower()

    encoder = OrdinalEncoder()
    encoder.fit(artificialIntelligence)

    artificialIntelligence_encoded = encoder.transform(artificialIntelligence)
    artificialIntelligence_encoded = np.nan_to_num(
        artificialIntelligence_encoded)

    skillList = artificialIntelligence_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\ArtificialIntelligence_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(artificialIntelligence_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    artificialIntelligence_num = pd.read_csv(
        "cpr\Datasets\ArtificialIntelligence_Encoded.csv", header=None, names=col_names)

    artificialIntelligence_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = artificialIntelligence_num[features_col].values
    y = artificialIntelligence_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    artificialIntelligence_list = artificialIntelligence_num.values.tolist()

    rowN = -1
    for row in range(0, len(artificialIntelligence_list)):
        if result == int(artificialIntelligence_list[row][15]):
            rowN = row
            break

    artificialIntelligenceResult = encoder.inverse_transform(
        artificialIntelligence_encoded).tolist()

    return artificialIntelligenceResult[rowN][15]
