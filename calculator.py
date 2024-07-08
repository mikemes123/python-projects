def calculator(num1, num2, string):
    if (string == "multiply"):
        print(num1 * num2)
    elif(string == "divide"):
        print(num1 / num2)
    elif(string == "add"):
        print(num1 + num2)
    elif(string == "subtract"):
        print(num1-num2)
    elif(string == "power"):
        print(num1**num2)
    else:
        print("Error")
calculator(5,6,"add")
calculator(5,4,"subtract")
calculator(3,2,"multiply")
calculator(6,2,"divide")
calculator(2,2, "power")