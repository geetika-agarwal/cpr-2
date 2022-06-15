import csv
import pandas as pd


def getSkillsF(jobrole):

    role = str(jobrole)
    skills = []
    with open("cpr\Datasets\jobroles.csv", "r", encoding="utf8") as jobs:
        reader_obj = csv.reader(jobs)
        for job in reader_obj:
            if(job[15] == role):
                skills = job
                break

    return skills
