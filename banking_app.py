import datetime

#Deposite 
Balance=50000
def Deposite(amount):
    if amount>=0:
        global Balance
        Balance+=amount
        print(f"Successfully deposited {amount}.New balance:{Balance}")
        return Balance
        
#Withdraw
def Withdraw(amount):
    global Balance
    if amount > Balance:
        print("Insufficient balance.")
       
        Balance-=amount
        print(f"Successfully withdrawn {amount}. New balance:{Balance}")
        return Balance 

    elif amount>Balance:
        print("Insufficient balance.")

    else:
        Balance-=amount
        print(f"Successfully withdrawn {amount}. New balance:{Balance}")  
        return Balance
    

while True:
    print("1.Create Account")
    print("2.Deposite Money")
    print("3.Withdraw Money")
    print("4.Check Balance")
    print("5.Transation History")
    print("6.Exit")

    choice=input("Enter your choice(1-6):")

    if choice=="1":
        User_name=input("Enter your name:")
        password=int(input("Enter the password:"))
        Address=input("Enter your address:")
        NIC_Number=input("Enter your NIC number:")
        with open('user_details.txt', 'a') as file:
            file.write(f"{User_name},{password},{Address},{NIC_Number}\n")
        print("created account for", User_name)
        Account_Number=

    elif choice=="2":
         amount=float(input("Enter amount to deposite Rs:"))
         Deposite(amount)
         with open('deposite_details.txt','a') as file:
             file.write(f"{amount},{Balance}\n")
         

    elif choice=="3":
         amount=float(input("Enter the amount to withdraw Rs:"))
         Withdraw(amount)
         with open('withdraw_details.txt','a') as file:
             file.write(f"{amount},{Balance}\n")
         print("withdraw successful.")

    elif choice=="4":
        print("Your available balance is Rs:")
        print(Balance)


    elif choice=="5":
        print("your transation history " , datetime.datetime.now())
        with open('deposite_details.txt','withdraw_details.txt','r') as file:
            
            file.read()
        
        
    elif choice == "6":
        print("Thank you for using our online banking system.")
        break
        
    else:
        print("Invalid choice. Please select a number between 1-6")