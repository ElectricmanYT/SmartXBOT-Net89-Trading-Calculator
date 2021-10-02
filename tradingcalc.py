print("""""
Please select one of the option:
1. Personal Profit
2. Total Profit
3. Topped Up Personal Profit
4. Topped Up Total Profit
""""")
Whichprofit = int(input("Select one of the options above: "))

if Whichprofit == 1:
    USD = int(input("How many USD did you deposit: "))
    if 500 <= USD > 2500:
        print("Your bot price is 500 USD")
        Botfee = 500
        print("Your profit share is 50%")
        Profitshare = 50%
    elif 2500 <= USD > 5000:
        print("Your bot price is 2500 USD")
        Botfee = 2500
        print("Your profit share is 55%")
        Profitshare = 55%
    elif 