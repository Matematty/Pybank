import sqlite3
con = sqlite3.connect('bank.db')
cur = con.cursor()
import mysql.connector




# i did not implement active users
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
        
    def transfer(self):
        sender_acct = int(input("Enter the Account you want to debit....."))
        recipient_acct = int(input("Enter the Account you want to credit......"))
        Database_manager.target_acct_no(self,recipient_acct) # i just decide not to do error handling here
        amount = int(input("Enter amount....."))

        if amount >= Database_manager.acct_balance(self,sender_acct):
            print("insufficient funds")
        elif Database_manager.acct_balance(self,sender_acct) < 50:
            print("you have only 50 naira..")
        elif amount < 100:
            print("Can only transfer 100")
        else:
            pin = int(input("enter your 4 digit payment pin"))
            if pin == Database_manager.user_pin(self,pin):
                try:
                    Database_manager.user_transfer(self,amount,sender_acct,recipient_acct)
                except Exception as e:
                    print(f"transfer error {e}")
                else:
                    print(f"You have successfully Transferred {amount} to {Database_manager.target_acct_no(self,recipient_acct)}")
            else:
                print("Incorrect Pin ")

            

    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw....."))
        debited_acct = int(input("Enter the Account you want to withdraw....."))
        if amount < 100:
            print("Can't withdraw less than 100 naira....")
        elif Database_manager.acct_balance(self,debited_acct) < amount:
            print("Insufficient funds...")
        else:
            try:
                Database_manager.user_withdraw(self,amount,debited_acct)
            except Exception as e:
                print(f"database error {e}")
        
    def deposit(self):

        amount = int(input("Enter the amount you want to send___"))
        if amount < 100:
            print("Can' deposit 100 naira..")
        else:
            acct_no = int(input("enter the account you want to credit___"))
            try:
                Database_manager.user_deposit(self,amount,acct_no)
            except Exception as e:
                print(e)
            print(f"You have successfully deposited: {amount} to {acct_no}")
        

    def get_balance(self):
        acct_no = int(input("Enter your account number....."))
        pass_word = int(input("Enter Account Password....."))
        balance = Database_manager.user_balance(self,acct_no,pass_word)
        
        return f"Your Account balance is: {balance}"


# this is the instance of the bank class
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
                print(f"Your Account Number is: {acct_no}")
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
            for i in range(3):
                try:
                    email_address = str(input("Enter your email address to login...."))
                    pass_word = int(input('Enter Your 6 digit Password to login........'))

                    #Database_manager.login_user(self,email_address,pass_word)
                except ValueError as v:
                    print(f"Value Error {v}")
                    continue
                    
                except TypeError as t:
                    print(f"Type Error {t}")
                    continue
                except Exception as e:
                    print(f"Caught Error {e}")
                    continue
                break
            return Database_manager.login_user(self,email_address,pass_word)

                    


                

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
        
        self.login_user_query = "select * from users  \
                                where email_address = %s and " \
                                "pass_word = %s ;"
        
        self.user_debit_query = "update users " \
                            "set balance = balance - %s " \
                            "where acct_no = %s ;" 
        self.user_credit_query =  "update users " \
                            "set balance = balance + %s " \
                            "where acct_no = %s ;" 
        self.balance_query = "select balance  from users where acct_no = %s and pass_word = %s;"
        self.target_name_query = "select full_name from users where acct_no = %s;"
        self.transfer_balance = "select balance  from users where acct_no = %s;"
        self.user_pin_query = "select pin from users where acct_no = %s; "
                        

    def insert_user(self,full_name,email_address,phone_no,pass_word,acct_no,pin):
        self.cursor.execute(self.insert_user_query,(full_name,email_address,phone_no,pass_word,acct_no,pin))
        self.connection.commit()
        #print('New Record Inserted into Database successfully')

    def login_user(self,email_address,pass_word):
        try:
            self.cursor.execute(self.login_user_query,(email_address,pass_word))
            fetched = self.cursor.fetchone()
            if fetched == None:
                print("Invalid login credential")
            else:
                print(f"Welcome {fetched[1]} To Pybank!!!")
        except Exception as e:
            print(f"database error {e}")
        return fetched 

    def user_transfer(self,amount,acct_no,target_acct):
        self.cursor.execute(self.user_debit_query,(amount,acct_no))
        self.cursor.fetchall()
        self.cursor.execute(self.user_credit_query,(amount,target_acct))
        self.cursor.fetchall()
        self.connection.commit()
    
    def user_deposit(self,amount,target_acct):
        self.cursor.execute(self.user_credit_query,(amount,target_acct))
        self.cursor.fetchall()
        self.connection.commit()

    def user_withdraw(self,amount,acct_no):
        self.cursor.execute(self.user_debit_query,(amount,acct_no))
        self.cursor.fetchall()
        self.connection.commit()
    def user_balance(self,acct_no,pass_word):
        fetch_balance = self.cursor.execute(self.balance_query,(acct_no,pass_word))
        balance = self.cursor.fetchone()
        print(balance[0])
    def target_acct_no(self,acct_no):
        self.cursor.execute(self.target_name_query,(acct_no,))
        fetched = self.cursor.fetchone()
        print(f"You are transfering money to: {fetched[0]}")
    def acct_balance(self,acct_no):
        self.cursor.execute(self.transfer_balance,(acct_no,))
        fetched = self.cursor.fetchone()
        return fetched[0]
    def user_pin(self,pin):
        self.cursor.execute(self.user_pin_query,(pin,))
        fetched = self.cursor.fetchone()
        return fetched
        
    

            



def main(): 
    print('hello world')


if __name__ == "__main__":
    main()
