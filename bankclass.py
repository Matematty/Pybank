import sqlite3
con = sqlite3.connect('bank.db')
cur = con.cursor()
import mysql.connector





# this is the instance of the bank user
class User:
    Status = 'Active'

    def __init__(self,id:int, 
                 full_name:str,
                 email:str, 
                 phone_no:int, 
                 pin:int,pass_word:int,
                 acct_no:int,balance=0):
        
        self.id = id
        self.full_name = full_name
        self.email = email
        self.phone_no = phone_no
        self.pin = pin
        self.pass_word = pass_word
        self.acct_no = acct_no
        self.balance = balance
        
    def transfer(self,amount,target_acct):
        if self.balance >= amount:
            new_balance = self.balance - amount
            print('transfer succesful')
            print(new_balance)
        else:
            print('insufficent funds')
        return self.balance
            

    def withdraw(self,amount):
        while True:
            # use len to check the length of input
            try:
                withdraw_amount = int(input('enter amount... '))
                if self.balance >= amount:
                    new_balance = self.balance - amount

                    # also check if the account that is being sent to exist
                    print('withdraw successful')
                    print(f'New balance is:{new_balance}')
                else:
                    print('insufficent funds')
            except ValueError:
                print('enter only numbers')
                continue
            else:
                break
                pass

        return self.balance

    def deposit(self,amount):

        amount = int(input("Enter the amount you want to send___")).is_integer()
        if amount >= 100:
            self.balance += amount
        elif amount < 100:
            print("can't transfer less than hundred naira")
        else:
            print('amount too small')
        return f'deposited {self.balance}'
        print(self.balance)
    def get_balance(self,balance):
        pass


# this is the instance the of the bank class
class Bank:
    def __init__(self,current_user,
                 db_connect):
        
        self.current_user = current_user
        self.db_connect = db_connect 

    # this function is to create a bank account 
    def create_acct(self):

        while True:
            try:
                full_name = str(input("Enter Your Name____"))
                email_address = str(input("Enter Email____"))
                phone_no = str(input("Enter Phone Number (e.g +2349045455676)____"))
                pass_word = int(input("Enter Password(Enter only numbers)____"))
                acct_no = phone_no[4:] 
                pin = int(input('Enter your 4 digit pin_____'))
                print(acct_no)
                Database_manager.insert_user(self,full_name,email_address,phone_no,pass_word,acct_no,pin)
                
            except ValueError as v:
                print(f'invalid entry{v}')
                continue
            except TypeError as t:
                print(f'Invalid entry {t}')
                continue
            except mysql.connector.Error as err:
                print(f" User with this email already exist")
                continue
            except Exception as e:
                print(f'invalid entry {e}')
                continue
            else:
                break
            return "You have Successfully Created an Account with Pybank"
            
    # this function helps to login into the bank account
    def login(self):
        while True:
            try:
                email_address = str(input("Enter your email address to login...."))
                pass_word = int(input('Enter Your 6 digit Password to login........'))

            except ValueError:
                print('invalid error')
                continue
            except TypeError as t:
                print(f"Type error {t}")
                continue
            except mysql.connector.Error as err:
                print(f"Database Error \nName not found {err}")
                con
            except Exception as e:
                print(f'plenty error{e}')
                continue
            else:
                try:
                   Database_manager.login_user(self,email_address,pass_word)
                   Bank.show_main_main()
                except Exception as e:
                    print(e)
                break

    def show_main_main(self):
        main_main = int(input("1.Transfer\n" \
                            "2.Withdraw\n" \
                            "3.Deposit\n" \
                            "4.Check Balance......."))
        while True:
            if main_main == 1:
                break
                print("you will transfer here ")
            elif main_main == 2:
                print("you withdraw here ")
            elif main_main == 3:
                print("you deposit here ")
            elif main_main == 4:
                print("check your balance ")
            else:
                print("you have exited ")
                break
    
        


        
    def handle_transaction(self):
        pass

#this class is for housing all my sql queries
class Database_manager:
    def __init__(self,host,user,password,database):
        self.connection =  mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database)
        self.cursor = self.connection.cursor()
        self.insert_user_query = "insert into users (full_name,email_address,phone_no,\
                                        pass_word,acct_no,pin)" \
                                        " values (%s,%s,%s,%s,%s,%s);"
        
        self.login_user_query = "select email_address,pass_word,  \
                                case when email_address = %s and " \
                                "pass_word = %s then 'login successfully' " \
                                "else 'login unsuccessful' " \
                                "end as login from users;"
        user_transfer_query = " "

    def insert_user(self,full_name,email_address,phone_no,pass_word,acct_no,pin):
        self.cursor.execute(self.insert_user_query,(full_name,email_address,phone_no,pass_word,acct_no,pin))
        self.connection.commit()
        print('New Record Inserted into Database successfully')

    def login_user(self,email_address,pass_word):
        fetch_it = self.cursor.execute(self.login_user_query,(email_address,pass_word))

    

            



def main(self): 
   # insert_user = "insert into users values ('Acha Saviour','acha@gmail.com', '+2349067860967', '344769', 9067860967, '2003');"
    #db = Database_manager()
    


    print('hello world')
    


if __name__ == "__main__":
    main()
