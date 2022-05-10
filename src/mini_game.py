#importing the important stuff
import pandas as pd
import numpy as np
import random as rd


data_file = 'src/data/data_toub_conv.csv'
data = pd.read_csv(data_file)


def main():
    userInput = ''
    prompt()
   
    while not(userInput == 'exit'):
        userInput = input()
        proc_input(userInput)


def prompt():
    print('Type "play" to test your smarts on unit conversion or be lame and type "exit" to leave the game')

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
    option = ['a', 'b', 'c', 'd']
    newOpt = rd.choice(option)
    rem_options = list(set(option).difference(set(newOpt)))
    #print(rem_options)
    
    correctAns = gen_ans(randomUnitNum, randomDimNum, randomNum) 

    print("What is " + str(randomNum)+ " " + randomUnit + " equal to?")
    randGen1 = gen_rand_wrong_ans(randomUnitNum, randomDimNum, randomNum)
    randGen2 = gen_rand_wrong_ans(randomUnitNum, randomDimNum, randomNum)
    randGen3 = gen_rand_wrong_ans(randomUnitNum, randomDimNum, randomNum)
    key_value = {newOpt: correctAns, rem_options[0]:randGen1, rem_options[1]:randGen2, rem_options[2]:randGen3}
    
    for x in sorted (key_value):
        print(x + ") " + key_value[x])   
    # print(newOpt + ")  " + correctAns)
    # print(rem_options[0] + ")  " + gen_rand_wrong_ans(randomUnitNum, randomDimNum, randomNum))
    # print(rem_options[1] + ")  " + gen_rand_wrong_ans(randomUnitNum, randomDimNum, randomNum))
    # print(rem_options[2] + ")  " + gen_rand_wrong_ans(randomUnitNum, randomDimNum, randomNum))

    inp = ''
    while not (inp == newOpt): 
        inp = input()
        if(inp == newOpt):
            print("Correct! Aren't you so smart")
        elif(inp == 'exit'):
            break  
        elif(inp != newOpt):
            print("You suck, try again")
            
            print("What is " + str(randomNum)+ " " + randomUnit + " equal to?")
            for x in sorted (key_value):
                print(x + ") " + key_value[x])   
            
if __name__ == "__main__":
    main()



