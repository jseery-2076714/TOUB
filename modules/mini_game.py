#importing the important stuff
import pandas as pd
import numpy as np
import random as rd
import importlib, importlib.util

correctChoiceForBot = ''
 

data_file = 'src/data/data_toub_conv.csv'
data = pd.read_csv(data_file)

def module_directory(name_module, path):
    p = importlib.util.spec_from_file_location(name_module, path)
    import_module = importlib.util.module_from_spec(p)
    p.loader.exec_module(import_module)
    return import_module
    
CONVERT = module_directory("convert", "./modules/convert.py")
SHEETS = module_directory("sheets", "./modules/sheets.py")

def prompt():
    return 'Test your unit conversion smarts with this fun minigame. Use the reactions to pick the correct option'


def proc_input(input):
    # error checking
    # return stuff if wrong
    if (input == 'play'):
        game_func1()

#generates the correct answer given a unit, dimension, and amount 
def gen_ans(unit, dim, amount):
    # cols = data.columns.to_numpy()
    # colvals = data[cols[dim]].to_numpy()
    # randomCorrectAnswer = rd.randint(0, 4)

    # anotherRandUnit = colvals[randomCorrectAnswer]
    # givenUnitIntoCm = colvals[unit] 
    # ratio = givenUnitIntoCm / anotherRandUnit
    # ans = str(amount * ratio)


    secondUnit = CONVERT.unit_select(unit, 3)
    result = CONVERT.convert_unit(amount, unit, secondUnit)
    
    return result

#generates wrong answers given a unit, dimension, and amount 
def gen_rand_wrong_ans(unit, dim, amount):
   
    wrongNum = rd.randint(1,3)
    ### wrongUnitNum = rd.randint(0,4)
    wrongUnit = CONVERT.unit_select(unit, 3)

    #loops so that the same unit and number
    #that was passed in cannot be used again
    while(wrongUnit == unit):
        wrongUnit = rd.randint(0,4)
    
    while(wrongNum == dim):
        wrongNum = rd.randint(1,3)

    wrongSecondUnit = CONVERT.unit_select(wrongUnit, wrongNum)
    wrongResult = CONVERT.convert_unit(amount, wrongUnit, wrongSecondUnit)
    
    return wrongResult 

    # cols = data.columns.to_numpy()
    # colvals = data[cols[wrongNum]].to_numpy()

    # anotherRandUnit = colvals[wrongUnit]
    # givenUnitIntoCm = colvals[wrongNum] 
    # ratio = givenUnitIntoCm / anotherRandUnit
    # ans = str(amount * ratio) 

    #return ans + " " + data.loc[wrongUnit][0]



#game function. Creats the unit, dimension and amount for question
#calls other methods to generate the right answer and wrong answer
#returns a string with the prompt and choices
def game_func1(): 
    randomUnitNum = rd.randint(0,4)
    randomDimNum = rd.randint(1,3)
    convArr = data.loc[randomUnitNum].to_numpy()
    randomUnit = convArr[0]
    randomNum = rd.randint(0, 100)

    # random not the unit above
    # generate 4 other relevant options
    option = ['1', '2', '3', '4']
    correctChoice = rightChoice()
    rem_options = list(set(option).difference(set(correctChoice)))

    ###instead of unit num, need to pass in the unit!
    ### this will get a unit that is of any of the three levels
    unitRand = CONVERT.unit_select("inch", 3)
    correctAns = gen_ans(unitRand, randomDimNum, randomNum) 

    print(correctChoice + " : " + correctAns)

    randGen1 = gen_rand_wrong_ans(unitRand, randomDimNum, randomNum)
    randGen2 = gen_rand_wrong_ans(unitRand, randomDimNum, randomNum)
    randGen3 = gen_rand_wrong_ans(unitRand, randomDimNum, randomNum)
    key_value = {correctChoice: correctAns, rem_options[0]:randGen1, rem_options[1]:randGen2, rem_options[2]:randGen3, '5': "None of the above"}
    
    returner = "What is " + str(randomNum)+ " " + randomUnit + " equal to? \n"
    for x in sorted (key_value):
        returner += x + ") " + key_value[x]  + "\n"
    return returner  


#returns the correct choice so 
#it can be checked with the discord bot
def rightChoice():
    global correctChoiceForBot
    option = ['1', '2', '3', '4']
    correctChoice = rd.choice(option)
    correctChoiceForBot = correctChoice
    return correctChoice

def correctChoiceForBotGetter():
    return correctChoiceForBot

#returns string for when game is won
def game_won():
        return ("Correct! Aren't you so smart")



