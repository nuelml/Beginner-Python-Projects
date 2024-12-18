def tip_calc():
    welcome_message = "Welcome to the \"BEST\" tip calculator in the world!"
    print(welcome_message)
    bill_amount = int(input("Enter bill amount: $"))
    tip_amount  = int(input(f"What your tip percentage? 5% 10% 15% : "))
    if tip_amount in [5, 10, 15]:
        tip_percentage = (tip_amount/100) * bill_amount
        total_bill = tip_percentage + bill_amount
        print(f"Your total bill is:${round(total_bill)}.")
        
    else:
        print("Enter a valid tip!")
        tip_calc()
        
        
tip_calc()