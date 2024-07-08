def atm():
    x = True
    num = int(input("What is your starting amount? \n "))
    while x == True:
        process = input("What would you like to do? (deposit or withdrawal) \n")
        if process == "deposit":
            depositamnt = int(input("How much would you like to deposit?\n"))
            num = depositamnt + num
            print("Your new total is: " + str(num))
        
        elif process == "withdrawal":
            withdrawalamnt = int(input("How much would you like to withdraw?\n"))
            if withdrawalamnt <= num:
                num = num - withdrawalamnt
                print("Your new total is: " + str(num))
            else: print("withdrawal amount too high!")
        
        else:
            print("Error")
        response = input("Are you done? (answer in lowercase) \n")
        if response == "yes":
                break
atm()
