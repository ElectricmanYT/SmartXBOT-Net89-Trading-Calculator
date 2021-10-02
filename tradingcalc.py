import time
print("This is SmartXBOT Trading Calculator v0.1")
print("""Please select one of the option:
1. Personal Profit
2. Total Profit
3. Topped Up Personal Profit (Work In Progress)
4. Topped Up Total Profit (Work In Progress)
""""")
Whichprofit = int(input("Select one of the options above: "))

#Calculates
USD = int(input("How many USD did you deposit: "))
if (500 <= USD and 2500 > USD):
    print("Your bot price is 100 USD")
    Botfee = 100
    print("Your profit share is 50%")
    Profitshare = 0.5
elif (2500 <= USD and 5000 > USD):
    print("Your bot price is 500 USD")
    Botfee = 500
    print("Your profit share is 55%")
    Profitshare = 0.55
elif (5000 <= USD and 12500 > USD):
    print("Your bot price is 1,000 USD")
    Botfee = 1000
    print("Your profit share is 60%")
    Profitshare = 0.6
elif (12500 <= USD and 25000 > USD):
    print("Your bot price is 2,500 USD")
    Botfee = 2500
    print("Your profit share is 70%")
    Profitshare = 0.7
elif (25000 <= USD and 50000 > USD):
    print("Your bot price is 5,000 USD")
    Botfee = 5000
    print("Your profit share is 80%")
    Profitshare = 0.8
elif (50000 <= USD):
    print("Your bot price is 10,000 USD")
    Botfee = 10000
    print("Your profit share is 90%")
    Profitshare = 0.9
else:
    print("Your bot is not listed here.")
    value = True
    while (value):
        time.sleep(1)
USDProfit = (USD - Botfee) * 0.01
Trader = USDProfit * Profitshare
IDR = Trader * 13000
TD = int(input("Estimate your trading days: "))
if 21 <= TD:
    TD = 20
Totalprofit = IDR * TD

#Profit
if (Whichprofit == 1):
    cut = int(input('Cut percentage (do not include "%"): '))
    Profitcut = Totalprofit * cut/100
    s = "{:,.2f}".format(Profitcut)
    print("Your profit is Rp " + s)
elif (Whichprofit == 2):
    s = "{:,.2f}".format(Totalprofit)
    print("Your profit is Rp " + s)

value = True
while (value):
    time.sleep(1)