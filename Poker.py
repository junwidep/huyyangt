#A poker like game that determines what kind of hand you have
#after you have thrown the duce two times.

#import a file called diceHelper
import diceHelper

#import library randomizer for the dice rolls
import random

#practically our main function in which will be called. The manager function
#when is called will play the game
def playOneRound():

    #throws a random die three times. The first time gives you your five choices (9,T,J,Q,K,A). You can have
    #as many as 5 or over choices. Then you are going to input the choice you would like to roll again. Then the
    #third the same which would give you your result choices.

    print("lets play an awesome game of pokah")
    
    #calls function throwAllDice() in which returns a dictionary of cards (the result of the randomizer)
    dice = throwAllDice()

    #prints out your returned result
    print("First throw: you threw", dice)

    #calls upon the diceHelper function ask() in which 
    rethrow = diceHelper.ask("Which dice do you want to throw again? ")

    #calls the function throwDice in which passes in the dictionary list
    #along with the first dictionary results
    dice = throwDice(rethrow, dice)
    
    print("Second throw: you now have", dice)

    #redeclare rethrow and asks the user if they want to throw another dice
    rethrow = diceHelper.ask("Which dice do you want to throw again? ")

    #calls the function throwDice in which passes in the dictionary list
    #along with the first dictionary results
    dice = throwDice(rethrow, dice)
    print("Final throw: you now have", dice)

    #calls upon the function evaluateHand in which takes in the dicionary
    #of cards. This function will determine what kind of hand you have
    des = evaluateHand(dice)
    print("You have", des)
    return des

def throwAllDice():
    #Rolls your die, and gives you the die results.

    result = []
    for i in range(5):
        result.append(diceHelper.throwDie())

    result.sort()
        
    return result
        
def throwDice(whichToThrow, diceList):

    #Gives the option to input your choice of dice side so the user can roll again """

    for x in whichToThrow:
        index = diceList.index(x)
        diceList[index] = diceHelper.throwDie()

    diceList.sort()

    return diceList

#a function that will evaluate what kind of hand you have. Passes in your whole dictionary
def evaluateHand(originalDice):

    #Defines each hand at the end result. Example would be a straight,
    #a low straight, a pair, a four of a kind etc.

    #a dictionary that is declared by diceSides for the passed in hand
    diceSides = []

    #goes through the for loop of the 6 cards
    for side in '9TJKQA':
        #appens the passed in dictionary in the variable diceSides
        diceSides.append(originalDice.count(side))

    #goes through the for loop of results depending on what kind of
    #hand you have
    if diceSides == [0, 1, 1, 1, 1, 1]:
        return "High Straight"
    elif diceSides == [1, 1, 1, 1, 1, 0]:
        return "Low Straight"
    diceSides.sort()
    if diceSides == [0, 0, 1, 1, 1, 2]:
        return "Pair"
    elif diceSides == [0, 0, 0, 1, 1, 3]:
        return "Three of a kind"
    elif diceSides == [0, 0, 0, 0, 1, 4]:
        return "Four of a kind"
    elif diceSides == [0, 0, 0, 0, 2, 3]:
        return "Full House baby"
    elif diceSides == [0, 0, 0, 1, 2, 2]:
        return "Two Pairs"

    else:
        return "none"
    
     

playOneRound()
