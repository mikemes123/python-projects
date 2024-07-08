def chat_bot():
    print("Welcome fella! ")
    response = input("What can I help you with?\n ")
    if (response == "calculate"):
        #inputs from user
        string = input("What do you wanna calculate?\n")
        num1 = int(input("What is your first number?\n "))
        num2 = int(input("What is your second number?\n "))
        result = 0
        #calculator code from before
        if (string == "multiply"):
            result = (num1 * num2)
        elif(string == "divide"):
            result = (num1 / num2)
        elif(string == "add"):
            result = (num1 + num2)
        elif(string == "subtract"):
            result = (num1-num2)
        elif(string == "power"):
            result = (num1**num2)
        else:
            print("Error")
    print("Your result is " + str(result))
chat_bot()