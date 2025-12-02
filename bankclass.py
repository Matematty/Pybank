import sqlite3
con = sqlite3.connect('bank.db')
cur = con.cursor()

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
        
    def transfer(self,amount,target_acct,):
        if self.balance >= amount:
            new_balance = self.balance - amount
            print('transfer succesful')
            print(new_balance)
        else:
            print('insufficent funds')
            print(self.balance)
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

    def deposit(self):
        amount = int(input("Enter the amount you want to send"))
        if amount > 0:
            self.balance += amount
        elif amount < 2:
            print("can't transfer less than hundred naira")
        else:
            print('amount too small')
        print(f'deposited {self.balance}')
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
                id = 1 # maybe make this auto increasezsgggfe
                name = str(input("Enter Your Name"))
                email = str(input("Enter Email"))
                phone = str(input("Enter Phone Number"))
                password = int(input("enter password"))
                pin = int(input('Enter your 4 digit pin'))
                acct_no = phone[1:]
                # i think this object of the user should happen after the user caalls the depoist function
                #user_obj = User(id,name,email,phone,pin,password,acct_no)
                
            except ValueError:
                print('invalid entry')
                continue
            except TypeError:
                print('Invalid entry')
                continue
            except Exception as e:
                print('invalid entry')
                continue
            else:


                print('run sql statement')
                print('run either deposit or exit')
                break
            
    # this function helps to login into the bank account
    def login(self):
        while True:
            try:
                login_acct_no = int(input("Enter your 10 digit Account Number......"))
                login_password = int(input('Enter Your 5 digit Password........'))
                try:
                    # run sql statement here
                    # select  acct_no, login_password from user where id = 1
                    # 
                    db_2=[12345]
                    db_1= [12345]
                    if login_acct_no in db_2 and login_password in db_1:
                        #run sql statement
                        print("Name found")
                    else:
                        print("Records Do Not Match")
                except ConnectionError:
                    print('name not found')
            except ValueError:
                print('invalid error')
                continue
            except TypeError:
                print("Type error")
                continue
            except Exception as e:
                print('plenty error')
                continue
            else:
                print('do something here')
                break
    def show_main_main(self):

        pass
    def handle_transaction(self):
        pass


def main(): 
    john = User(1,'Acha Saviour','Acha@gmail.com',2349067860967,1094,102345, 9067860967 )
    #john.deposit(2000)
    john.withdraw(1000)
    #john.transfer(1500,9067860967)

if __name__ == "__main__":
    main()
