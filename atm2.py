import getpass
num = 600
username = input("What is your username? \n")
password = getpass.getpass("What is your password \n")
print(password)
process = input("Welcome " + username + " what would you like to do? (deposit, balance or withdrawal) \n")
if process == "deposit":
    def deposit(num):
        depositamnt = int(input("How much would you like to deposit?\n"))
        amnt = depositamnt + num
        print("Your new total is: " + str(amnt) + " Goodbye")
elif process == "withdrawal":
    def withdrawal(num):
        withdrawalamnt = int(input("How much would you like to withdraw?\n"))
        if withdrawalamnt <= num:
            amnt = num - withdrawalamnt
            print("Your new total is: " + str(amnt) + " Goodbye")
        else: print("withdrawal amount too high!")
elif process == "balance":
    def balance(num):
        print("Your balance is "+ str(num) + " Goodbye")
def main():
    deposit(600)
    withdrawal(600)
    balance(600)
if __name__==__name__:
    main()