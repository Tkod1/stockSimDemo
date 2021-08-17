import random


class StockSymbol:
    # volatility engine decides volatility for stock symbol randomly
    def volatilityengine(self):
        volchoice = random.randint(1, 10)  # selects random number to set volatility
        voloutput = volchoice  # volatility choice as a new variable voloutput
        voldevision = int(100) / voloutput  # Devices the random number by 100 to get a percentage.
        print('Volatility Percentage: ', voldevision)  # prints the amount of volatility
        # selects a new stock symbols characters.

    def newstockengine(self):
        self.volatilityengine()
        letterlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        letterchoice = random.choice(letterlist)  # randomly chooses from list of letters
        letterchoice2 = random.choice(letterlist)  # assign the character value to a variable, do this three times
        # for 3 letters.
        letterchoice3 = random.choice(letterlist)
        print('StockSymbol Choice: ', letterchoice, letterchoice2, letterchoice3)

        # strike price is decided at random

    def newstockstrikeprice(self):
        self.newstockengine()
        strikepricechoice = random.randint(1, 17)  # chooses the amount for strikeprice
        strikeoutput = strikepricechoice + .00  # hard coded numbers for cents in dollar value
        print('Strikeprice: $', + strikeoutput)


class_instance = StockSymbol()  # sets class instance variable to the Stock symbol class
# class_instance.newstockstrikeprice()  # calls to the last function withing calls up to the above two functions.

print('Hello Welcome to Stock Simulator.')
print('what is your name?')
userName = input()

print('Alright ' + userName + ' how many days would you like to play? you can choose (1), (2), (3) through (10)')
daysOfPlay = input()

# takes input and generates a new symbol.
print('Do you wish to begin with a new stock symbol? (y) or (n)')
startnewinput = input()
for val in startnewinput:
    if startnewinput == 'y':
        class_instance.newstockstrikeprice()
        if startnewinput == 'n':
            break

accountAmount = 300
print(userName + ' You will start with an account amount of $300.00.')
print('To simulate one day hit (d) + enter) for two days (dd), three (ddd).')
userDaySkip = input()


# simulation day according to input
def nod():
    d = 1
    dd = 2
    ddd = 3
    oneday = userDaySkip * class_instance.volatilityengine()


print("day function reached")
