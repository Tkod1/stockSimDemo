import random


# stock symbols
class StockSymbol:
    stockName = str()
    currentStrikePrice = float()
    volatility = float()


print('Hello Welcome to Stock Simulator.')
print('what is your name?')
userName = input()

print('Alright ' + userName + ' how many days would you like to play? you can choose (1), (2), (3) through (10)')
daysOfPlay = input()

accountAmount = 300
print(userName + ' You will start with an account amount of $300.00.')
print('To simulate one day hit (d) + enter) for two days (dd), three (ddd).')
userDaySkip = input()


# volatility engine decides volatility for stock symbol randomly
def volatilityengine():
    volChoice = random.randint(1, 10)
    volOutput = volChoice
    print(int(volOutput))
    voldevision = int(100.00) / volOutput
    print(voldevision)


volatilityengine()


def newstockengine():
    letterlist = ['a', 'b', 'c', 'd', 'e']
    
    setvolatility = volatilityengine(volOutput)
