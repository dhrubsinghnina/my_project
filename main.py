accounts={
    101:{"Name":"Ram","Balance":10000}
}
# ADDING ACCOUNT:
def addaccount():
    accno=int(input("Enter accno :"))
    name=str(input("Enter name :"))
    amount=int(input("Enter amount :"))
    if accno in accounts:
        print("Account is exist already!")
    else:
        accounts[accno]={"Name":name,"Balance":amount}
        
# DELETEING ACCOUNT: 
def deleteacount():
    accno=int(input("Enter accno :"))
    if accno not in accounts:
        print("The account is not exist :")        
    else:
        accounts.pop(accno)
        
def updating():
    accno=int(input("Enter accno:"))
    amount=int(input("Enter amount:"))
    type=int(input("Enter 1 for deposit and -1 for credit :"))
    if type==1:
        accounts[accno]["Balance"]+=amount
    if type==-1 :
        if(accounts[accno]["Balance"]>=amount):
            accounts[accno]["Balance"]-=amount
        else:
            print(f"Balance is low :{accounts[accno]["Balance"]}<{amount}")
   
def save(accounts):
    with open("bank.txt",'w') as f:
        f.write(f"{str(accounts)}")
        print("\n")
   
def display(accounts):
    for i in accounts:
        print(f"{i} : {accounts[i]}")    

c=int(input("Enter 0 to start :"))           
while(c!=-1):
    c=int(input("""Enter 1 to add account :
        Enter 2 to to delete :
        Enter 3 to update :
        Enter 4 to display :
        Enter -1 to stop :"""))
    if c==1:
        addaccount()
    elif c==2:
        deleteacount()
    elif c==3:
        updating()
    elif c==4:
        display(accounts)
    save(accounts)
    
    
        
        
    
    
    
    