def fizz_buzz(num):
    if(num % 3 == 0) & (num % 5 == 0):
        print("Fizz & Buzz")
    elif(num % 3 == 0):
        print("Fizz")
    elif(num % 5 == 0):
        print("Buzz")
    else:
        print("Not fizz or buzz")
fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(7)