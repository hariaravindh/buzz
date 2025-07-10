import mysql.connector as m
d=m.connect(host="localhost",user="root",passwd="_Hari04onmars_",charset="utf8",database="project")
cur=d.cursor()
if d.is_connected():
    print("\tWELCOME TO ONLINE BUS RESERVATION FIND BUSES TO YOUR DESTINATION ")
for i in range(3):
    print("***\t\t\t\t***\t\t\t\t***")

print("1.sign up /n 2.login")
ch=input("Your Choice ?")
if ch==1:
    def signup():
        name=input("enter your name")
        mobilenumber=int(input("enter your mobile number"))
        address=input("enter your address")
        email=input("enter your email id")
        sign=[name,mobilenumber,address,email]
        t1=tuple(name,mobilenumber)
        t0=tuple(name,mobilenumber,address,email)
        cur.execute("update table1 set signup=sign")
        print(t0)
        checkdata1=int(input("are your details correct \n 1:yes \n 2:no"))
        if checkdata1==1:
            print("ok")
        else:
            cur.execute("drop table if exists table1")
            print("try again from starting")
           
elif ch==2:
    def login():
        cur.execute("select name,mobilenumber * from table1")
        checkname=input("enter your name as entered in your account")
        checkmobilenumber=int(input("enter your mobile number"))
        tcheck=tuple(checkname,checkmobilenumber)
        if tcheck==t:
            print("successfully you have login")
        else:
            print("try again")
        
    
def location():
    pickup=input("enter your pickup location")
    drop=input("enter your drop location")
    pd=[pickup,drop]
    cur.execute("update table2 set location=pd")
    t2=tuple(pickup,drop)
    print("your desired pickup and drop location are",t2)

def date():
    departure=int(input("enter your departure date in the format of dd/mm/yyyy"))
    arrival=int(input("enter your arrival date in the format dd/mm/yyyy"))
    dt=[departure,arrival]
    cur.execute("update table3 set date=dt")
    t3=tuple(departue,arrival)
    print("your departure and arrival date are",t3)
    

def search():
    db=input("enter your desired bus")
    ac=input("enter if you want an ac or a non ac bus")
    s=[db,ac]
    cur.execute("update table4 set search=s")
    t4=tuple(db,ac)
    print("your desired bus is",t4)
    
    
def details():
    b=int(input("enter either berth or seating \n ch1:berth \nch2:seating"))
    print("all your current details entered till now are\n",t0,"\n",t2,"\n",t3,b,"\n",t4)

def BERTH(): 
    print("seating arrangement") 
    cur.execute("select * from berth") 
    for x in cur: 
        print(x) 
    print("Remaining seats:") 
    cur.execute("select * from berth2")
    for x in cur: 
        print(x) 
s=int(input("Enter your seat number:\t")) 
cur.execute("insert into berth3(berth)values({})".format(s)) 
cur.execute("delete from berth2 where seatnum={}".format(s)) 

def MEALS(): 
    f=open("meals.txt","r") 
    s=" " 
    while s: 
        s=f.readline() 
        print(s,end="") 
f.close() 
h=input("\nenter your choice either V or N\n ") 
while True: 
    if h=="V" or h=="N" or h=="v" or h=="n": 
        cur.execute("insert into meals(meals)values('{}')".format(h)) 
        break 
    else: 
        print("Invalid Choice") 

def PAYMENT():  
    p=[] 
    print("1.Debit Card\n2.Credit Card\n3.UPI") 
    n=int(input("Enter your choice from 1-3:")) 
    while True: 
        if n==1: 
            cn=input("Enter your debit card number:")
            cna=input("Enter your card name:") 
            v=input("Enter your card validity in DD/MM form:") 
            cvv=input("Enter your card cvv") 
            p=[cn,cna,v,cvv] 
            cur.execute("insert into payment(payment)values(%s);",[','.join(p)]) 
        elif n==2: 
            cn=input("Enter your Credit card number") 
            cna=input("Enter your card name") 
            v=input("Enteryour card validity in DD/MM form:") 
            cvv=input("Enter your card cvv") 
            p=[cn,cna,v,cvv] 
            cur.execute("insert into payment(payment)values(%s);",[','.join(p)])  
        elif n==3: 
            print("1.Google pay\n2.Phonpe\n3.Paytm") 
            a=int(input("Enter your choice from 1-3:")) 
            if a==1: 
                gn=input("Enter your google pay number:") 
                gp=input("Enter your google pay pin:") 
                p=[gn,gp] 
                cur.execute("insert into payment(payment)values(%s);",[','.join(p)]) 
            elif a==2: 
                pn=input("Enter your phonpe number:") 
                pp=input("Enter your phonpe pin:") 
                p=[pn,pp] 
                cur.execute("insert into payment(payment)values(%s);",[','.join(p)]) 
            elif a==3: 
                pyn=input("Enter your paytm number:") 
                pyp=input("Enter your paytm pin:") 
                p=[pyn,pyp] 
                cur.execute("insert into payment(payment)values(%s);",[','.join(p)])  
            else: 
                print("Invalid choice") 
        else: 
            print("Invalid choice") 

def CONFIRM(): 
    print("Do you want to cancel your ticket") 
    a=input("Enter C if you want to confirm your booking\n N to cancel your booking\n") 
    if a=='C' or a=='c': 
        print("Booking confirmed\n Your ticket:")
        cur.execute("select * from table2") 
        for x in cur: 
            print(x) 
        cur.execute("select * from table3") 
        for x in cur: 
            print(x) 
        cur.execute("select * from table4") 
        for x in cur: 
            print(x) 
        cur.execute("select * from berth3") 
        for x in cur: 
            print(x) 
        cur.execute("select * from meals") 
        for x in cur: 
            print(x) 
        cur.execute("select * from payment") 
        for x in cur: 
            print(x) 
        cur.execute("delete from berth3") 
        cur.execute("delete from meals") 
        cur.execute("delete from payment") 
        cur.execute("delete from table2") 
        cur.execute("delete from table3") 
        cur.execute("delete from table4") 
    elif a=='N' or a=='n': 
        print("Booking cancelled") 
        cur.execute("delete from berth3") 
        cur.execute("delete from meals") 
        cur.execute("delete from payment") 
        cur.execute("delete from table2")  
        cur.execute("delete from table3") 
        cur.execute("delete from table4") 
    else: 
        print("Invalid choice") 



CREATE() 
LOCATION() 
DATE() 
SEARCH() 
BERTH() 
MEALS() 
PAYMENT() 
CONFIRM() 
d.commit() 
cur.close() 
d.close()
