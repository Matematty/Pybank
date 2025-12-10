# this imports the user and bank class from bankclass.py
from bankclass import User 
from bankclass import Bank
from bankclass import Database_manager

HOST = 'localhost'
USER = 'root'
PASSWORD = 'Acha@004'
DATABASE = 'pybankDB'

db = Database_manager(HOST,USER,PASSWORD,DATABASE)

'''
 this while loop keeps running untill a user types in a number between 1 and 3 and doesn't accpets letters, but if a number other than 1-3 is enter it exits
'''


for i in range(3):
    try:
        option = int(input('welcome to pybank.....\
                        \n1. Create Account\
                        \n2. Login\
                        \n3. Exit__________'))
        
        if option == 1:

            # this calls the create account function in the  bank class in bankclass.py 
            try:
                Bank.create_acct(db)
            except Exception as e:
                print(f"Invalid Entries \n Account Not Created >:< {e}")
            else:
                first_deposit = input("Account Created Succesfully \nWill you like to make your first deposit______").upper()
                if first_deposit == "YES":
                    User.deposit(db)
                else:
                    print("do nothing......")
    

        elif option == 2:
                    
                    log = Bank.login(db)
                    if log == None:
                         print("invalid credentials")

                    else:
                        main_main = int(input("1.Transfer\n" \
                                     "2.Withdraw\n" \
                                    "3.Deposit\n" \
                                    "4.Check Balance......."))
                        if main_main == 1:
                             User.transfer(db)
                        elif main_main == 2:
                             User.withdraw(db)
                        elif main_main == 3:
                             User.deposit(db)
                        else:
                             User.get_balance(db)
        else:
            break
            print('Exited PyBank')
        
    except ValueError:
        print('Invalid entry\nEnter only 1-3')
        continue
    else:
        break


