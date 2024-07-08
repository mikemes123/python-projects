num = int(input("What would you like the countdown to start at? \n"))
def countdown(num):
    for i in range (num):
        print(num-i)


countdown(num)