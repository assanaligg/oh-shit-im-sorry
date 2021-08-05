# Здесь должен быть твой код
import pandas as pd
import time

def fill_sex(sex):
    if sex == 'M':
        return 1
    return 0

def fill_yes_no(item):
    if item == 'yes':
        return 1
    return 0

def fill_edu(item):
    if item == 'primary education (4th grade)':
        return 1
    if item == '5th to 9th grade':
        return 2
    if item == 'secondary education':
        return 3
    if item == 'higher education':
        return 4
    return 0

def fill_study_time(item):
    if item == '2 to 5 hours':
        return 1
    if item == '5 to 10 hours':
        return 2
    if item == 'more than 10 hours':
        return 3
    return 0 

def fill_free_time(item):
    if item = 'high':
        return 1
    if item == 'medium':
        return 2
    if item == 'low':
        return 3
    if item == 'very low':
        return 4
    return 0

df = pd.read_csv('train.csv')
print(df.info())

df['Medu'].fillna('5th to 9th grade', inplace = True)
df['Fedu'].fillna('5th to 9th grade', inplace = True)
df['guardian'].fillna('mother', inplace = True)

df.drop(['Mjob', 'Fjob', 'reason', 'guardian', 'famsize', 'traveltime', ' farmel'], axis = 1, inplace = True)
