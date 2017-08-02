import numpy as np
import matplotlib as p
import pdb
from pandas import *


data = read_csv('train.csv',sep=',')
print ( data)
men = data[data.sex == 'male']
women = data[data.sex == 'female']

proportion_women_survived = float(sum(women.survived))/len(women)
proportion_men_survived = float(sum(men.survived))/len(men)

data['prediction']=0

data.prediction[data.sex == 'female']=1

print ( data)

print ( len(unique(data.sex)))



data['fare_bracket']=0
data.fare_bracket=np.array([min(int(price/10),3) for price in data.fare])

data.pclass.hist()

look_up=dict()
for sex in unique(data.sex):
    for pclass in unique(data.pclass):
        for fare_bracket in unique(data.fare_bracket):
            look_up[(sex, pclass, fare_bracket)]= np.mean(data.survived[(data.sex == sex) & (data.pclass == pclass) & (data.fare_bracket == fare_bracket)])


            # read in the file
        test = read_csv('testpanda.csv',sep=',')
        # make new column
        test['prediction'] = 0
        # move that column to the first
        print (test)
        print ((len(test.columns)))
        print (range(len(test.columns)))

     # new_order = [len(test.columns) - 1] + range(len(test.columns) - 1)
     #   test = test.reindex(columns=test.columns[new_order])
        # make a new column to contain information on the fare_bracket
        test['fare_bracket'] = 0
        # we find that one of the entries is missing its fare entry
        print ("asdf")
        sum(test.fare != test.fare)

    # we first find that one (it has a NaN so checking if it is
    # equal to itself will return a False)
    wh_badfare = np.flatnonzero(test.fare != test.fare)
    # we save the value
    sv = test.fare[test.fare != test.fare]
    # we change it to be scaled by the pclass
    test.fare[test.fare != test.fare] = (3 - test.pclass) * 11
    # now we find the new fare_brackets for the test data
    test.fare_bracket = np.array([min(int(price / 10), 3) for price in test.fare])
    # now we replace the NaN from before
    test.fare[wh_badfare] = sv

    # Now we assign predictions
    for i in range(len(test)):
        test.prediction[i] = round(look_up[(test.sex[i], test.pclass[i], test.fare_bracket[i])])
    # and write the file
    test.to_csv('genderclasspricebasedmodelpy.csv', index=False)