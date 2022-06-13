import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics


def BlockchainFunc(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    blockchain = pd.read_csv(
        "cpr\Datasets\Blockchain.csv", header=None)

    blockchain.loc[0] = skillList

    for i in range(16):
        blockchain[i] = blockchain[i].str.lower()

    encoder = OrdinalEncoder()
    encoder.fit(blockchain)

    blockchain_encoded = encoder.transform(blockchain)
    blockchain_encoded = np.nan_to_num(
        blockchain_encoded)

    skillList = blockchain_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\Blockchain_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(blockchain_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    blockchain_num = pd.read_csv(
        "cpr\Datasets\Blockchain_Encoded.csv", header=None, names=col_names)

    blockchain_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = blockchain_num[features_col].values
    y = blockchain_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    blockchain_list = blockchain_num.values.tolist()

    rowN = -1
    for row in range(0, len(blockchain_list)):
        if result == int(blockchain_list[row][15]):
            rowN = row
            break

    blockchainResult = encoder.inverse_transform(
        blockchain_num).tolist()

    return blockchainResult[rowN][15]
