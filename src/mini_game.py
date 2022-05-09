#importing the important stuff
import pandas as pd
import numpy as np
import random as rd

data_file = 'src/data/data_toub_conv.csv'
data = pd.read_csv(data_file)

def main():
    userInput = ''
    prompt()
   
    # while not(userInput == 'exit'):
    #     userInput = input()
    #     proc_input(userInput)


def prompt():
    print('Options: play || exit')

def proc_input(input):
    # error checking
    # return stuff if wrong
    if (input == 'play'):
        game_func1()
    elif (1):
        return 2 #call func
    return 'Hello'

def gen_ans(unit, dim, amount, rem_options):
    # cols = data.columns.to_numpy() #column names in an array
    # dimNum = 2
    # print(cols[dimNum]) # specific col name
    # colvals = data[cols[dimNum]].to_numpy() #creates list of all day in cols[dimDum]
    # print(colvals)
    # print(colvals[4]) #prints exact unit I want
    # print(data.loc[4][0])

    cols = data.columns.to_numpy()
    # colvals == colvals = data[cols[dim]].to_numpy()


    
    return '0'

def game_func1(): 
    randomUnitNum = rd.randint(0,6)
    randomDimNum = rd.randint(1,3)
    convArr = data.loc[randomUnitNum].to_numpy()
    randomUnit = convArr[0]
    randomDim = convArr[randomDimNum]
    randomNum = rd.randint(0, 10000000)

    # random not the unit above
    # generate 4 other relevant options
    option = ['a', 'b', 'c', 'd']
    newOpt = rd.choice(option)
    newUnit = 'feet'
    newConv = 123177
    rem_options = set(option).difference(set(newOpt))
    print(rem_options)
    # print("What is " + str(randomNum)+ " " + convArr + " equal to?")
    # print("a. " + gen_ans(randomUnit, randomNum))
    # print("b. " + gen_ans(randomUnit, randomNum))
    # print("c. " + gen_ans(randomUnit, randomNum))
    # print("d. " + gen_ans(randomUnit, randomNum))

if __name__ == "__main__":
    main()



