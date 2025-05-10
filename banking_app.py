import datetime

def datetimeshow():
    return datetime.date.today()


#Create Account Number 
def Create():
    import random
    random_number = random.randint(999, 10000)
    number= random_number   
    return number


#Deposite 
Balance=50000
def Deposite(amount):
    if amount>=0:
        global Balance
        Balance+=amount
        print(f"Successfully deposited {amount}.New balance:{Balance}")

        with open('transation_history.txt', 'a') as file:
            file.write(f"{amount},{Balance}\n")
            
        return Balance
    

#Withdraw
def Withdraw(amount):
    global Balance

    if amount < Balance:
    
        Balance-=amount
        print(f"Successfully withdrawn {amount}. New balance:{Balance}")

        with open('transation_history.txt', 'a') as file:
            file.write(f"{amount},{Balance}\n")

        return Balance 
    
    elif amount>Balance:
        print("Insufficient balance.")
        return


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
        print("created account for", User_name)
        print("Your account number:")
        Acc_Num=Create()
        print(Acc_Num)

        with open('user_details.txt', 'a') as file:
            file.write(f"{User_name},{password},{Address},{NIC_Number},{Acc_Num}\n")


    
    elif choice=="2":
         Acc_Num=int(input("Enter Your Account Number:"))
         User_name=input("Enter Your Name:")

         amount=float(input("Enter amount to deposite Rs:"))
         Deposite(amount)

         with open('deposite_details.txt','a') as file:
             file.write(f"{User_name},{Acc_Num},{amount},{Balance}\n")
         print("Deposite successful.")


    elif choice=="3":
         Acc_Num=int(input("Enter your Account Number:"))
         User_name=input("Enter your Name:")

         amount=float(input("Enter the amount to withdraw Rs:"))
         Withdraw(amount)
         if amount> Balance:
                print("Insufficient balance")

         with open('withdraw_details.txt','a') as file:
             file.write(f"{User_name},{Acc_Num},{amount},{Balance}\n")
         print("withdraw successful.")


    elif choice=="4":
        Acc_Num=int(input("Enter Your Account Number:"))
        User_name=input("Enter Your Name:")

        print("Your available balance is Rs:")
        print(Balance)

        with open('Available_balance.txt' , 'a') as file:
            file.write(f"{User_name},{Acc_Num}, {Balance}\n")



    elif choice=="5":
        Acc_Num=int(input("Enter Your Account Number:"))
        User_name=input("Enter Your Name:")
    
        print("your transation history " , datetimeshow())

        with open('deposite_details.txt','r') as file:
            for i in file:
                test = i.split(",")
                print(i)

        with open('withdraw_details.txt','r') as file:
            for j in file:
                test = j.split(",")
                print(j)
          
            
        
    elif choice == "6":
        print("Thank you for using our online banking system.")
        break
        
    else:
        print("Invalid choice. Please select a number between 1-6")
        