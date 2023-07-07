import mysql.connector as m
class bank:
    
    def register(self,account,aadhar,name,password,balance):
        self.account=account
        self.name=name
        self.aadhar=aadhar
        self.balance=balance
        self.password=password
        c=mysql()
        cur=c.cursor()
        cur.execute(f"insert into customer(account,aadhar,name,balance,password) values('{self.account}','{self.aadhar}','{self.name}','{self.balance}','{self.password}');")
        c.commit()
        c.close()
        print("Data Inserted")

class banker(bank):
           
    def update(self,name,balance,password,account):
        
        c=mysql()
        cur=c.cursor()
        cur.execute(f"update customer set name='{name}',balance='{balance}',password='{password}' where account='{account}'")
        c.commit()
        c.close()
        print("Data Updated")
        


class customer(bank):
    pass
bankerr=banker()
def mysql():
      return m.connect(
        host="localhost",
        user="root",
        password="kp@123",
        database="bank"
        ) 
def bankerlogin(username,password):
        #user=username
        #self.password=password
        
        c=mysql()
        cur=c.cursor()
        cur.execute(f"select username,password from banker where username='{username}' and password='{password}';")
        r=cur.fetchall()
        
        #print(r)
        if len(r)==0:
            print("Invalid Username or Password")
           
        else:
          while True:
            print("Login Success")
            print("Select Choice as a Banker")
            print("1) Register")
            print("2) Login As Customer")
            print("3) Update Customer")
            print("4) view Customer")
            print("5) Delete Customer")

            bchoice=input("Enter: ")

            if bchoice=="1":
                c=mysql()
                cur=c.cursor()
                while True:
                      account=int(input("Enter Account Number: "))
                      cur.execute(f"select account from customer where account='{account}';")
                      r=cur.fetchall()
                      if len(r)<1:
                          while True:
                                try:
                                  aadhar=int(input("Enter Aadhar Number: "))
                                  name=input("Enter Your Name: ")
                                  balance=int(input("Enter Opening Ammount: "))
                                  password=input("Enter Password: ")
                                  bankerr.register(account,aadhar,name,password,balance)
                                  break
                                except ValueError:
                                    print("Enter Currect value")
                                    print("Renter Values")
                      else:
                          print("Account Number Already Exist Please choose another Number:")
                
            
            elif bchoice=="2":
                c=mysql()
                cur=c.cursor()
                while True:
                    account=int(input("Enter Account Number: "))
                    password=input("Enter Your Password: ")
                    
                    
                    cur.execute(f"select name,account,aadhar,balance from customer where account='{account}' and password='{password}';")
                    r=cur.fetchall()[0]
                    print(list(r))
                    
                    

            elif bchoice=="3":
                while True:
                      account=int(input("Enter Account Number: "))
                      cur.execute(f"select * from customer where account='{account}';")
                      r=cur.fetchall()
                      if len(r)==1:
                          print(r)
                          while True:
                                try:
                                    name=input("Enter Your Name: ")
                                    balance=int(input("Enter Opening Ammount: "))
                                    password=input("Enter Password: ")
                                    bankerr.update(name,balance,password,account)
                                    break
                                except ValueError:
                                    print("Invalid Value Please Enter Valid Values")
                          
                      else:
                          print("Account Not Found:")
                          
            elif bchoice=="4":
                pass
            elif bchoice=="5":
                pass
            else:
                print("Invalid Choice")
 

while True:
        print("Who are you: ")
        print("1) Banker")
        print("2) Customer")
        print("3) Exit")


        choice=input("Enter choice: ")

        if choice=="1":
           username=input("Enter username: ")
           password=input("Enter Password: ")
           bankerlogin(username,password)
           break

        
        elif choice=="2":
            customer()
        
        elif choice=="3":
            break
        else:
            print("Invalid Choice")
