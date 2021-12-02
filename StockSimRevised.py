import random


# Symbol creation
def symbol():
    letterList = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]
    


def day():
    #when game is started full function is rand but when day two happens starting total needs to be skipped and replaced with current account.
    startingAccountTotal = float(300)
    randomDailyMultiplyer = random.randint(1,9)
    fullTradetime = float(8)
    dailyAccountMovement = startingAccountTotal + randomDailyMultiplyer * fullTradetime
    print(dailyAccountMovement)


day() 
