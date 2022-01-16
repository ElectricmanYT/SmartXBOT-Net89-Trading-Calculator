import time
#Options
print("This is SmartXBOT Trading Calculator v0.4.3")
time.sleep(0.5)
print("""""")
time.sleep(0.5)
print("""Please select one of the option:
1. Personal Profit
2. Total Profit
3. Topped Up Personal Profit (Work In Progress)
4. Topped Up Total Profit (Work In Progress)
5. Calculate a singular profit earned
6. Calculate a singular profit cut
""")
time.sleep(1)
Whichprofit = int(input("Select one of the options above: "))

#Function
def EndScript():
    value = True
    while (value):
        time.sleep(1)

def USDCalculate(USD):
    if (500 <= USD and 2500 > USD):
        print("Your bot price is 100 USD")
        Botfee = 100
        time.sleep(1)
        print("Your profit share is 50%")
        Profitshare = 0.5
        time.sleep(1)
    elif (2500 <= USD and 5000 > USD):
        print("Your bot price is 500 USD")
        Botfee = 500
        time.sleep(1)
        print("Your profit share is 55%")
        Profitshare = 0.55
        time.sleep(1)
    elif (5000 <= USD and 12500 > USD):
        print("Your bot price is 1,000 USD")
        Botfee = 1000
        time.sleep(1)
        print("Your profit share is 60%")
        Profitshare = 0.6
        time.sleep(1)
    elif (12500 <= USD and 25000 > USD):
        print("Your bot price is 2,500 USD")
        Botfee = 2500
        time.sleep(1)
        print("Your profit share is 70%")
        Profitshare = 0.7
        time.sleep(1)
    elif (25000 <= USD and 50000 > USD):
        print("Your bot price is 5,000 USD")
        Botfee = 5000
        time.sleep(1)
        print("Your profit share is 80%")
        Profitshare = 0.8
        time.sleep(1)
    elif (50000 <= USD):
        print("Your bot price is 10,000 USD")
        Botfee = 10000
        time.sleep(1)
        print("Your profit share is 90%")
        Profitshare = 0.9
        time.sleep(1)
    else:
        print("Your bot is not listed here.")
        value = True
        while (value):
            time.sleep(1)
    USDProfit = (USD - Botfee) * 0.01
    Trader = USDProfit * Profitshare
    IDR = Trader * 13000
    TD = int(input("Estimate your trading days: "))
    if 22 < TD:
        TD = 22
        print('Your Estimation is over the top estimation of Loss Trading Days')
        EndScript()
    Totalprofit = IDR * TD

    return Totalprofit

#Profit
if (Whichprofit == 1):
    USD = float(input("How many USD did you deposit: "))
    print("""""")
    Totalprofit = USDCalculate(USD)
    cut = float(input('Cut percentage (do not include "%"): '))
    coma = "{:,.2f}".format(Totalprofit)
    print("""""")
    print("Your estimated total profit is Rp " + coma + "/month")
    time.sleep(1)
    Profitcut = Totalprofit * cut/100
    s = "{:,.2f}".format(Profitcut)
    print("Your estimated cut profit is Rp " + s + "/month")
elif (Whichprofit == 2):
    USD = float(input("How many USD did you deposit: "))
    print("""""")
    Totalprofit = USDCalculate(USD)
    s = "{:,.2f}".format(Totalprofit)
    print("""""")
    print("Your estimated total profit is Rp " + s + "/month")
elif (Whichprofit == 3):
    print("""""")
    print("This option is work in progress.")
elif (Whichprofit == 4):
    print("""""")
    print("This option is work in progress.")
elif (Whichprofit == 5):
    USD = float(input("How many USD did you earn: "))
    print("""""")
    Profitearned = USD * 13000
    s = "{:,.2f}".format(Profitearned)
    print("You have earned Rp " + s)
elif (Whichprofit == 6):
    USD = float(input("How many USD did you earn: "))
    Profitearned = USD * 13000
    cut = float(input('Cut percentage (do not include "%"): '))
    print("""""")
    Profitcut = Profitearned * cut/100
    stotal = "{:,.2f}".format(Profitearned)
    s = "{:,.2f}".format(Profitcut)
    print("You have earned a total of Rp " + stotal)
    time.sleep(1)
    print("You have earned a profit cut of Rp " + s)
else:
    print("Your choice is not listed in the options.")

value = True
while (value):
    time.sleep(1)