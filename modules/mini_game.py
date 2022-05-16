#importing the important stuff
import pandas as pd
import numpy as np
import random as rd


data_file = 'src/data/data_toub_conv.csv'
data = pd.read_csv(data_file)

def prompt():
    return 'Test your unit conversion smarts with this fun minigame. Use the reactions to pick the correct option'

def proc_input(input):
    # error checking
    # return stuff if wrong
    if (input == 'play'):
        game_func1()

def gen_ans(unit, dim, amount):
    cols = data.columns.to_numpy()
    colvals = data[cols[dim]].to_numpy()
    randomCorrectAnswer = rd.randint(0, 4)

    anotherRandUnit = colvals[randomCorrectAnswer]
    givenUnitIntoCm = colvals[unit] 
    ratio = givenUnitIntoCm / anotherRandUnit
    ans = str(amount * ratio)

    return ans + " " + data.loc[randomCorrectAnswer][0]

def gen_rand_wrong_ans(unit, dim, amount):
    wrongUnit = rd.randint(0,4)
    wrongNum = rd.randint(1,3)

    while(wrongUnit == unit):
        wrongUnit = rd.randint(0,4)
    
    while(wrongNum == dim):
        wrongNum = rd.randint(1,3)

    cols = data.columns.to_numpy()
    colvals = data[cols[wrongNum]].to_numpy()
    #randomCorrectAnswer = rd.randint(0, 4)

    anotherRandUnit = colvals[wrongUnit]
    givenUnitIntoCm = colvals[wrongNum] 
    ratio = givenUnitIntoCm / anotherRandUnit
    ans = str(amount * ratio) 

    return ans + " " + data.loc[wrongUnit][0]




def game_func1(): 
    randomUnitNum = rd.randint(0,4)
    randomDimNum = rd.randint(1,3)
    convArr = data.loc[randomUnitNum].to_numpy()
    randomUnit = convArr[0]
    randomNum = rd.randint(0, 10000000)

    # random not the unit above
    # generate 4 other relevant options
    option = ['1', '2', '3', '4']
    correctChoice = rightChoice()
    rem_options = list(set(option).difference(set(correctChoice)))

    correctAns = gen_ans(randomUnitNum, randomDimNum, randomNum) 

    randGen1 = gen_rand_wrong_ans(randomUnitNum, randomDimNum, randomNum)
    randGen2 = gen_rand_wrong_ans(randomUnitNum, randomDimNum, randomNum)
    randGen3 = gen_rand_wrong_ans(randomUnitNum, randomDimNum, randomNum)
    key_value = {correctChoice: correctAns, rem_options[0]:randGen1, rem_options[1]:randGen2, rem_options[2]:randGen3, '5': "None of the above"}
    
    returner = "What is " + str(randomNum)+ " " + randomUnit + " equal to? \n"
    for x in sorted (key_value):
        returner += x + ") " + key_value[x]  + "\n"
    return returner  


def rightChoice():
    option = ['1', '2', '3', '4']
    correctChoice = rd.choice(option)
    return correctChoice

def game_won():
        return ("Correct! Aren't you so smart")



