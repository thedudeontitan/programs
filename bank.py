
n = int(input("Enter number of transaction"))

balance = 0

for i in range (n):


    transaction = str(input("Enter D/d for diposite \nEnter W/w for withdrawal\n "))

    if transaction == "D" or transaction == "d" :
        amount=int(input("Enter amount "))
        balance += amount 

    elif transaction =="W" or transaction =="w" :
        amount=int(input("Enter amount "))
        balance -= amount
    else:
        print("please enter a valid transaction. ")
        n -= 1

print ("Remaining balance is: " + str (balance))