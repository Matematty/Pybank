from bankclass import User 
from bankclass import Bank
while True:
    try:
        option = int(input('welcome to pybank.....\
                        \n1. Create Account\
                        \n2. Login\
                        \n3. Exit'))
        if option == 1:
            Bank.create_acct()
            first_deposit = str(input("Do you want to deposit Yes/No"))
            if first_deposit == "yes":
                new_user = User(id,"name","email","phone","pin","password","acct_no")
                new_user.deposit()
                print("we run deposit here")
            else:
                break

        elif option == 2:
            Bank.login()
        else:
            print('Exited PyBank')
            break
        
    except ValueError:
        print('invalid entry')
        continue
    else:
        break




















