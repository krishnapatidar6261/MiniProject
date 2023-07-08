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
        
    def login(self):
                c=mysql()
                cur=c.cursor()
                while True:
                  try:
                    account=int(input("Enter Account Number: "))
                    password=input("Enter Your Password: ")
                    
                    
                    cur.execute(f"select name,account,aadhar,balance from customer where account='{account}' and password='{password}';")
                    r=cur.fetchall()
                    c.close()
                    if len(r)<1:
                         print("Invalid username or Password")
                    else:
                        print(list(r[0]))

                        break
                  except ValueError:
                      print("Invalid username or Password") 

class banker(bank):
           
    def update(self,name,balance,password,account):
        
        c=mysql()
        cur=c.cursor()
        cur.execute(f"update customer set name='{name}',balance='{balance}',password='{password}' where account='{account}'")
        c.commit()
        c.close()
        print("Data Updated")
        
    def deleteCustomer(self,account):
        c=mysql()
        cur=c.cursor()
        cur.execute(f"delete from customer where account='{account}';")
        c.commit()
        c.close()
        print("Data Deleted")
        


class customer(bank):
    def withdraw(self,balance,withdrawamt,account):
        self.ammount=balance-withdrawamt
        
        c=mysql()
        cur=c.cursor()
        cur.execute(f"update customer set balance='{self.ammount}' where account='{account}';")
        c.commit()
        c.close()
        customer.view()
        
    def diposite(self,account,balance,dipositeamt):
        balance=balance+dipositeamt
        c=mysql()
        cur=c.cursor()
        cur.execute(f"update customer set balance='{balance}' where account='{account}';")
        c.commit()
        c.close()
        print("Diposite Successfully")
        print("Now Your Balance is: ",balance)
        
        

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
          print("Login Success")
          while True:
            
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
              
                bankerr.login()               

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
                while True:
                    try:
                      account=int(input("Enter Account Number: "))
                      cur.execute(f"select * from customer where account='{account}';")
                      r=cur.fetchall()
                      if len(r)==1:
                          print(r[0])
                          break
                      else:
                          print("Account Not Found:")
                    except ValueError:
                        print("Invalid Account Number")     
            elif bchoice=="5":
                while True:
                    try:
                      account=int(input("Enter Account Number: "))
                      cur.execute(f"select account,name,aadhar,balance from customer where account='{account}';")
                      r=cur.fetchall()
                      if len(r)==1:
                          print(r[0])
                          bankerr.deleteCustomer(account)
                          break
                                                    
                      else:
                          print("Account Not Found:")
                    except ValueError:
                        print("Invalid Account Number")
            else:
                print("Invalid Choice")
 
def customerlogin():
    print("Welcome to Customer App")
    while True:
        print("Select Choice as a Customer")  
        print("1) Register")
        print("2) Login ")
        print("3) Withdraw")
        print("4) deposite")
        print("5) View Balance")
        cchoice=input("Enter: ")

        if cchoice=="1":
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
        elif cchoice=="2":
            customerr.login()
        elif cchoice=="3":
                c=mysql()
                cur=c.cursor()
                while True:
                  try:
                    account=int(input("Enter Account Number: "))
                    password=input("Enter Your Password: ")
                    
                    
                    cur.execute(f"select balance from customer where account='{account}' and password='{password}';")
                    r=cur.fetchall()
                    print(r)
                    if len(r)<1:
                         print("Invalid username or Password")
                    else:
                      
                      balance=r[0][0]
                      print("")
                      withdrawamt=int(input("Enter Withdraw Ammount: "))
                      if withdrawamt>balance:
                          print("Need ",withdrawamt-balance,"money Withdraw")
                      else:
                          customerr.withdraw(balance,withdrawamt,account)
                          break
                       
                      
                  except:
                      print("Invalid username or Password")
                  finally:
                      cur.close()
        elif cchoice=="4":
                c=mysql()
                cur=c.cursor()
                while True:
                      account=int(input("Enter Account Number: "))
                      cur.execute(f"select balance from customer where account='{account}';")
                      r=cur.fetchall()
                      
                      if len(r)<1:
                          print("Account Not Found")
                      else:
                          balance=r[0][0]
                          dipositeamt=int(input("Enter Diposiite Ammount: "))
                          customerr.diposite(account,balance,dipositeamt)
                          break
        elif cchoice=="5":
                c=mysql()
                cur=c.cursor()
                while True:
                      account=int(input("Enter Account Number: "))
                      cur.execute(f"select balance from customer where account='{account}';")
                      r=cur.fetchall()
                      
                      if len(r)<1:
                          print("Account Not Found")
                      else:
                          print(r[0][0])
        else:
 
           print("Invalid Choice")
           
bankerr=banker()
customerr=customer()
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
            customerlogin()
        
        elif choice=="3":
            break
        else:
            print("Invalid Choice")
