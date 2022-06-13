import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics


def SnowflakeFunc(allSkills):
    skills = allSkills

    skillList = []

    for i in range(16):
        if(len(skills) > i):
            skillList.append(skills[i])

        else:
            skillList.append(np.nan)

    snowflake = pd.read_csv(
        "cpr\Datasets\Snowflake.csv", header=None)

    snowflake.loc[0] = skillList

    for i in range(16):
        snowflake[i] = snowflake[i].astype(
            str).str.lower()

    encoder = OrdinalEncoder()
    encoder.fit(snowflake)

    snowflake_encoded = encoder.transform(
        snowflake)
    snowflake_encoded = np.nan_to_num(
        snowflake_encoded)

    skillList = snowflake_encoded[0]
    skillList = skillList[0:15]

    with open("cpr\Datasets\snowflake_Encoded.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(snowflake_encoded)

    col_names = ["skill1", "skill2", "skill3", "skill4", "skill5", "skill6", "skill7", "skill8",
                 "skill9", "skill10", "skill11", "skill12", "skill13", "skill14", "skill15", "JobRoles"]

    snowflake_num = pd.read_csv(
        "cpr\Datasets\snowflake_Encoded.csv", header=None, names=col_names)

    snowflake_num.drop([0], axis=0, inplace=True)

    features_col = ['skill1', 'skill2', 'skill3', 'skill4', 'skill5', 'skill6', 'skill7',
                    'skill8', 'skill9', 'skill10', 'skill11', 'skill12', 'skill13', 'skill14', 'skill15']

    X = snowflake_num[features_col].values
    y = snowflake_num.JobRoles.values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)

    result = clf.predict([skillList])

    snowflake_list = snowflake_num.values.tolist()

    rowN = -1
    for row in range(0, len(snowflake_list)):
        if result == int(snowflake_list[row][15]):
            rowN = row
            break

    snowflakeResult = encoder.inverse_transform(
        snowflake_num).tolist()

    return snowflakeResult[rowN][15]
