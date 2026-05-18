#currency converter using only variable, input, if/elif/else, while True and print statements.

# This program converts between three currencies: Nigerian Naira (NGN), Euro (EUR), and US Dollar (USD).
print("Welcome to the currency converter!")
print ("Please enter the amount you want to convert:")
allowed_currencies = ("NGN", "EUR", "USD")
while True:
    try:
        amount = float(input())
        if amount <= 0:
            print("Invalid input. please enter a number greater than 0.")
            continue
        
        break

    except ValueError:      
            print("Invalid amount. Please enter a valid number for the amount.\n")

        
        
while True:
        try:
            from_currency = input("Please enter the currency you want to convert from (NGN, EUR, USD): \n ").upper()
        
            to_currency = input("Please enter the currency you want to convert to (NGN, EUR, USD): \n ").upper()
        
            if to_currency not in allowed_currencies or from_currency not in allowed_currencies:
                print("Invalid currency input. Please try again. Make sure to enter NGN, EUR, or USD.\n")
                continue
            

            if from_currency == "NGN" and to_currency == "EUR":
                converted_amount = amount * 0.00063
            elif from_currency == "NGN" and to_currency == "USD":
                converted_amount = amount * 0.00073    
            elif from_currency == "EUR" and to_currency == "NGN":
                converted_amount = amount * 1596.30    
            elif from_currency == "EUR" and to_currency == "USD":
                converted_amount = amount * 1.16   
            elif from_currency == "USD" and to_currency == "NGN":
                converted_amount = amount * 1372.74    
            elif from_currency == "USD" and to_currency == "EUR":
                converted_amount = amount * 0.86
            elif from_currency == "NGN" and to_currency == "NGN":
                converted_amount = amount
            elif from_currency == "EUR" and to_currency == "EUR":
                converted_amount = amount
            elif from_currency == "USD" and to_currency == "USD":
                converted_amount = amount
                
        

            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
            break
        except ValueError:
            print("Invalid input. Please try again.\n")
            continue


print ("Thank you for using the currency converter!")