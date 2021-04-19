# module diceHelper
# helper functions for the Poker Dice assignment

#function that will return a random card 
def throwDie():
    #return a randlomly-chosen letter from the set 9, T, J, Q, K, A.
    import random
    return random.choice(['9', 'T', 'J', 'Q', 'K', 'A'])
    
def ask(prompt):

    #return a list containing 9, T, J, Q, K, A, based on user unput.
    #Ask the user the question prompt, wait for user input.
    #Assume that the user types a (possibly empty) line containing some combination of 9,T,J,Q,K,A 
    #Extract those characters from the input, and return them as a list, which may be empty.
    
    #the prompt is going to be a passed in string that will ask the user
    #which dice they want to rethrow
    typing = input(prompt + "(9TJQKA): ")

    #this result is going to be in a dictionary
    result = []

    #goes through a for loop and will pick out the chosen letter
    for each in typing.upper():
        if each in '9TJQKA':
            result.append(each)

    #returns result
    return result



