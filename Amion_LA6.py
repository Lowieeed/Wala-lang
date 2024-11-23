while True:
    n1 = float(input("Enter First Number: "))
    n2 = float(input("Enter Second Number: "))
    
    Total = n1 + n2 
    
    print(f"The sum of {n2} and {n2} is {Total}")
    
    again = input("Do you want to try again? [Y/N]: ").lower()
    
    if again == 'n':
        print("thankyou")
        break