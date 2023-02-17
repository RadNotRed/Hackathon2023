from currency_converter import CurrencyConverter

c = CurrencyConverter()

print("Welcome to the currency converter!")
print("Please enter the amount of money you would like to convert: ")
money = float(input())

print("Please enter the currency you would like to convert to: ")
print("1. Euro")
print("2. British Pound")
print("3. Japanese Yen")
print("4. Mexican Peso")
print("5. Australian Dollar")
currency = int(input())

if currency == 1:
    print("You have converted", money, "USD to", c.convert(money, 'USD', 'EUR'), "EUR")
elif currency == 2:
    print("You have converted", money, "USD to", c.convert(money, 'USD', 'GBP'), "GBP")
elif currency == 3:
    print("You have converted", money, "USD to", c.convert(money, 'USD', 'JPY'), "JPY")
elif currency == 4:
    print("You have converted", money, "USD to", c.convert(money, 'USD', 'MXN'), "MXN")
elif currency == 5:
    print("You have converted", money, "USD to", c.convert(money, 'USD', 'AUD'), "AUD")
else:
    print("Invalid currency")
