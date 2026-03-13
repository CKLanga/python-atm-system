balance = 10000
pin  = 1234
x = int(input("Enter PIN : "))
if(x == pin):
    while True:
        print("What would you like to do : ")
        print("1. Check Balance.")
        print("2. Withdraw money.")
        print("3. Deposite money.")
        print("4. Exit.")
        choice = int(input("Enter choice : "))
        if(choice == 1):
            print("Balance : ",balance)
        elif(choice == 2):
            ammount = int(input("Enter ammount : "))
            if(ammount < balance):
                balance -= ammount
            else : print("Insufficient ammount.")
        elif(choice == 3):
            amm = int(input("Enter ammount : "))
            if(amm > 0) :
                balance += amm
            else : print("You cannot deposite a negative value.")
        elif(choice == 4):
            print("Exiting..")
            break
        else: print("Error input.")
    
else: print("Wrong pin")

