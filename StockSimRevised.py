import random


# Symbol creation

# (Symbol) one day calculation based on 8 hours.

def day():
    #when game is started full function is rand but when day two happens starting total needs to be skipped and replaced with current account.
    startingAccountTotal = float(300)
    randomDailyMultiplyer = num.rand(1-7)
    #random addition or subtraction needs to take place to the account 
    fullTradetime = float(6)
    dailyMultiplicationFunction = utility.math.multiplication

    todaysTotal = startingAccountTotal * randomDailyMultiplier 
