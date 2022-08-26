# GROCERY SHOP MANAGEMENT SYSTEM
# Version 1.0
# Mukund Sarda & Kartik Singh (12-H)
# St. Mark's Sr. Sec. Public School, Meera Bagh


import pymysql


def userid():
    print()
    
    a=input("Are you an existing user:")
    
    if a=='Y' or a=='y' or a=='Yes' or a=='YES' or a=='yes':
       existinguser()
       
       
    elif a=='N' or a=='n' or a=='No' or a=='NO' or a=='no':
        h=input("Enter the product key:")
        
        if h=="MSKS2021":
            print("Access Granted")
            
            i=input("Enter the new User ID :")
            j=input("Enter the new Password :")
            
            k="INSERT INTO Users(User_Id,Password) VALUES('%s','%s')"%(i,j)
            cur.execute(k)
            db.commit()
            
            print("New User Created")
            
            existinguser()
            
        else:
            print("Access Denied")
            print("Incorrect Product Key")
            
        
    else:
        print("Invalid Input")
    
    return


def existinguser():
    print()
    
    b=input("Enter User ID:")
    c=input("Enter Password:")

    try:
        d="SELECT User_Id FROM Users WHERE Password='%s'"%(c)
        cur.execute(d)
        e=cur.fetchall()
        h=e[0][0]
        i=h
    
        f="SELECT Password FROM Users WHERE User_Id='%s'"%(b)
        cur.execute(f)
        g=cur.fetchall()
        j=g[0][0]
        k=j
    
    
        if b==i and c==k:
            print("Successfully Connected")
            print()
        
            final_1()
                
    except:
        print("User ID or Password must be incorrect.")
        
    
    return


def categories():
    print()
    
    print("1. Bakery")
    print("2. Dairy")
    print("3. Cereals_And_Spices")
    print("4. Beverages")
    print("5. Fruits_And_Vegetables")
    print("6. Bathroom_And_Toiletries")
    print("7. Snacks")
    
    return


def menu1():
    print()
    
    print("WHICH PRODUCT CATEGORY YOU WANT TO ACCESS:")
    categories()
    
    return


def menu2(k):
    print()
    
    print("THINGS TO DO:")
    print("1. Add Products To",k)
    print("2. Update Products In",k)
    print("3. To Check Which Product Have Less Quantity In",k)
    print("4. To View All Products Of",k)
    print("5. To Sell Products Of",k)
    print("6. To Manage Order List")
    print("7. To Manage Sales List")
    
    return


def add(k):
    print()
    
    a=input("Enter the Product Code:")
    b=input("Enter the Product Name:")
    c=int(input("Enter the Cost Price:"))
    f=int(input("Enter the Selling Price:"))
    d=int(input("Enter the Quantity:"))
    
    e="INSERT INTO "+k+"(Product_Code,Product_Name,Cost_Price,Quantity,Selling_Price) VALUES('%s','%s','%s','%s','%s')"%(a,b,c,d,f)
    cur.execute(e)
    db.commit()
    
    return


def add_final(k):
    print()
    
    ans='yes'
    
    while ans=='yes' or ans=='Yes' or ans=='Y' or ans=='y' or ans=='YES':
        add(k)
        print()
        ans=input("Do You Want To Add More Products (Yes/No):")
        
    return


def updatemenu():
    print()
    
    print("THINGS TO DO:")
    print("1. To Update The Cost Price")
    print("2. To Update The Selling Price")
    print("3. To Update The Quantity")
    print("4. To Delete A Product")
    
    return


def update_cost_price(k):
    print()
    
    a=input("Enter The Product Name For Which Cost Has To Be Updated:")
    b=int(input("Enter The Updated Cost:"))
    
    c="UPDATE "+k+" SET Cost_Price='%s' WHERE Product_Name='%s'"%(b,a)
    d=cur.execute(c)
    db.commit()
    
    return


def update_selling_price(k):
    print()
    
    a=input("Enter The Product Name For Which Selling Price Has To Be Updated:")
    b=int(input("Enter The Updated Cost:"))
    
    c="UPDATE "+k+" SET Selling_Price='%s' WHERE Product_Name='%s'"%(b,a)
    d=cur.execute(c)
    db.commit()
    
    return


def update_quantity(k):
    print()
    
    a=input("Enter The Product Name For Which Quantity Has To Be Updated:")
    b=int(input("Enter The Updated Quantity:"))
    
    c="UPDATE "+k+" SET Quantity='%s' WHERE Product_Name='%s'"%(b,a)
    d=cur.execute(c)
    db.commit()
    
    return


def delete_product(k):
    print()
    
    a=input("Enter The Product Name Which Has To Be Deleted:")
    
    b="DELETE FROM "+k+" WHERE Product_Name='%s'"%(a)
    c=cur.execute(b)
    db.commit()
    
    return


def less_quantity(k):
    print()
    
    a=int(input("Enter The Minimum Quantity:"))
    
    print("The "+k+" Products Whose Quantity Is Less Than",a,"Are:")
    b="SELECT * FROM "+k+" WHERE Quantity<'%s'"%(a)
    c=cur.execute(b)
    d=cur.fetchall()
    
    for i in d:
        print(i)
        
    return


def less_quan_order(k):
    print()
    
    a=input("Do You Want To Place Order Of These Products:")
    
    if a=='Y' or a=='y' or a=='Yes' or a=='YES' or a=='yes':
        order_add_final(k)
        
    elif a=='N' or a=='n' or a=='No' or a=='NO' or a=='no':
        print()
    
    else:
        print("Incorrect Input")
    
    return


def view_all(k):
    print()
    
    a="SELECT * FROM "+k
    b=cur.execute(a)
    c=cur.fetchall()
    
    for i in c:
        print(i)
        
    return


def order_menu():
    print()
    
    print("THINGS TO DO:")
    print("1. Add Order To Order List")
    print("2. To Update The Quantity Of A Order")
    print("3. To Delete A Order")
    print("4. To View Complete Order List")
    
    return


def order_add(k):
    print()
    
    a=input("Enter The Name Of The Product To Be Ordered:")
    b=int(input("Enter The Quantity:"))
    
    d="SELECT Product_Code FROM "+k+" WHERE Product_Name='%s'"%(a)
    cur.execute(d)
    e=cur.fetchall()
    f=e[0][0]
    g=f
    
    h="SELECT Cost_Price FROM "+k+" WHERE Product_Name='%s'"%(a)
    cur.execute(h)
    i=cur.fetchall()
    j=i[0][0]
    l=j
    
    m=b*l
    
    n="INSERT INTO Orders(Product_Category,Product_Name,Quantity,Product_Code,Cost_Price,Amount) VALUES('%s','%s','%s','%s','%s','%s')"%(k,a,b,g,l,m)
    cur.execute(n)
    db.commit()
    
    return


def order_add_final(k):
    print()
    
    ans='yes'
    
    while ans=='yes' or ans=='Yes' or ans=='Y' or ans=='y' or ans=='YES':
        order_add(k)
        print()
        ans=input("Do You Want To Add More Products (Yes/No):")
        
    return


def order_update_quantity():
    print()
    
    a=input("Enter The Name Of The Product Whose Quantity Has To Be Updated:")
    b=int(input("Enter The Updated Quantity:"))
    
    c="UPDATE Orders SET Quantity='%s' WHERE Product_Name='%s'"%(b,a)
    d=cur.execute(c)
    db.commit()
    
    h="SELECT Cost_Price FROM Orders WHERE Product_Name='%s'"%(a)
    cur.execute(h)
    i=cur.fetchall()
    j=i[0][0]
    l=j
    
    m=b*l
    
    e="UPDATE Orders SET Amount='%s' WHERE Product_Name='%s'"%(m,a)
    cur.execute(e)
    db.commit()
    
    return


def order_delete():
    print()
    
    a=input("Enter The Name Of The Product Whose Order Is To Be Deleted:")
    
    b="DELETE FROM Orders WHERE Product_Name='%s'"%(a)
    c=cur.execute(b)
    db.commit()
    
    return


def order_view_all():
    print()
    
    a="SELECT * FROM Orders"
    b=cur.execute(a)
    c=cur.fetchall()
    
    for i in c:
        print(i)
        
    return


def sales_menu():
    print()
    
    print("THINGS TO DO:")
    print("1. Add Record To Sales List")
    print("2. To Delete Sales Before A Particular Date")
    print("3. To View Complete Sales List")
    print("4. To View Total Profit Earned")
    
    return


def sales_add(k):
    print()
    
    a=input("Enter The Name Of The Product To Be Sold:")
    b=int(input("Enter The Quantity:"))
    
    d="SELECT Product_Code FROM "+k+" WHERE Product_Name='%s'"%(a)
    cur.execute(d)
    e=cur.fetchall()
    f=e[0][0]
    g=f
    
    h="SELECT Cost_Price FROM "+k+" WHERE Product_Name='%s'"%(a)
    cur.execute(h)
    i=cur.fetchall()
    j=i[0][0]
    l=j
    
    m="SELECT Selling_Price FROM "+k+" WHERE Product_Name='%s'"%(a)
    cur.execute(m)
    n=cur.fetchall()
    o=n[0][0]
    p=o
    
    q=p*b
    r=l*b
    s=q-r
    
    t="INSERT INTO Sales(Product_Category,Product_Name,Quantity,Product_Code,Selling_Price,Amount,Profit,Date) VALUES('%s','%s','%s','%s','%s','%s','%s',CURDATE())"%(k,a,b,g,p,q,s)
    cur.execute(t)
    db.commit()
    
    u="UPDATE "+k+" SET Quantity=Quantity-'%s' WHERE Product_Name='%s'"%(b,a)
    cur.execute(u)
    db.commit()
    
    return


def sales_add_final(k):
    print()
    
    ans='yes'
    
    while ans=='yes' or ans=='Yes' or ans=='Y' or ans=='y' or ans=='YES':
        sales_add(k)
        print()
        ans=input("Do You Want To Sell More Products (Yes/No):")
        
    return


def delete_sales():
    
    a=input("Enter The Year(YYYY):")
    b=input("Enter The Month(MM):")
    c=input("Enter The Date(DD):")
    
    d=a+b+c
    e=int(d)
    
    f="DELETE FROM Sales WHERE Date<'%s'"%(e)
    cur.execute(f)
    db.commit()
    
    return


def sales_view_all():
    print()
    
    a="SELECT * FROM Sales"
    b=cur.execute(a)
    c=cur.fetchall()
    
    for i in c:
        print(i)
        
    return


def sales_profit():
    print()
    
    a="SELECT SUM(Profit) FROM Sales"
    cur.execute(a)
    b=cur.fetchall()
    
    print("Total Profit Earned:")
    print(b[0][0])
    
    return


def end():
    print()
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Thank You For Using Our GROCERY SHOP MANAGEMENT SYSTEM")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    print()
    
    print("""BY:
Mukund Sarda
Kartik Singh
(XII-H)""")
    return


def final_1():
    menu1()
    print()
    
    a=int(input("Enter Your Choice:"))
    
    if a==1:
        k="Bakery"
    elif a==2:
        k="Dairy"
    elif a==3:
        k="Cereals_And_Spices"
    elif a==4:
        k="Beverages"
    elif a==5:
        k="Fruits_And_Vegetables"
    elif a==6:
        k="Bathroom_And_Toiletries"
    elif a==7:
        k="Snacks"
    else:
        print("Incorrect Input")
    
    print()
    
    menu2(k)
    
    print()
    
    c=int(input("Enter Your Choice:"))
    
    if c==1:
        add_final(k)
        
        
    elif c==2:
        updatemenu()
        print()
        
        d=int(input("Enter Your Choice:"))
        
        if d==1:
            update_cost_price(k)
            
        elif d==2:
            update_selling_price(k)
            
        elif d==3:
            update_quantity(k)
            
        elif d==4:
            delete_product(k)
            
        else:
            ("Incorrect Input!")
            
        
    elif c==3:
        less_quantity(k)
        
        print()
        
        less_quan_order(k)
        
        
    elif c==4:
        view_all(k)
        
        
    elif c==5:
        sales_add_final(k)
        
        
    elif c==6:
        order_menu()
        print()
        
        e=int(input("Enter Your Choice:"))
        
        if e==1:
            order_add_final(k)
            
        elif e==2:
            order_update_quantity()
            
        elif e==3:
            order_delete()
            
        elif e==4:
            order_view_all()
            
        else:
            ("Incorrect Input!")
            
        
    elif c==7:
        sales_menu()
        print()
        
        f=int(input("Enter Your Choice:"))
        
        if f==1:
            sales_add_final(k)
            
        elif f==2:
            delete_sales()
            
        elif f==3:
            sales_view_all()
            
        elif f==4:
            sales_profit()
            
        else:
            ("Incorrect Input!")
            
        
    else:
        print("Incorrect Input!")
        
    
    return


def grocery_shop_management():
    z="yes"
    
    while z=="yes" or z=="Yes" or z=="Y" or z=="y" or z=="YES":
        userid()
        
        print()
        
        z=input("Do You Want To Run The Program Again (Yes/No):")
        
    else:
        end()
        
    return


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("WELCOME TO GROCERY SHOP MANAGEMENT SYSTEM")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print()

print("----------------------------")
print("PRODUCT CATEGORIES AVAILABLE")
print("----------------------------")

categories()

print()

x=input("Enter The Password Of Your Database:")

dr=pymysql.connect(host="localhost",user="root",password=x)
cr=dr.cursor()

cr.execute("CREATE DATABASE IF NOT EXISTS Grocery_Shop_Management")

db=pymysql.connect(host="localhost",user="root",password=x,db="Grocery_Shop_Management")
cur=db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Bakery(Product_Code VARCHAR(50),Product_Name VARCHAR(50),Cost_Price INT,Selling_Price INT,Quantity INT);")

cur.execute("CREATE TABLE IF NOT EXISTS Dairy(Product_Code VARCHAR(50),Product_Name VARCHAR(50),Cost_Price INT,Selling_Price INT,Quantity INT);")

cur.execute("CREATE TABLE IF NOT EXISTS Cereals_And_Spices(Product_Code VARCHAR(50),Product_Name VARCHAR(50),Cost_Price INT,Selling_Price INT,Quantity INT);")

cur.execute("CREATE TABLE IF NOT EXISTS Beverages(Product_Code VARCHAR(50),Product_Name VARCHAR(50),Cost_Price INT,Selling_Price INT,Quantity INT);")

cur.execute("CREATE TABLE IF NOT EXISTS Fruits_And_Vegetables(Product_Code VARCHAR(50),Product_Name VARCHAR(50),Cost_Price INT,Selling_Price INT,Quantity INT);")

cur.execute("CREATE TABLE IF NOT EXISTS Bathroom_And_Toiletries(Product_Code VARCHAR(50),Product_Name VARCHAR(50),Cost_Price INT,Selling_Price INT,Quantity INT);")

cur.execute("CREATE TABLE IF NOT EXISTS Snacks(Product_Code VARCHAR(50),Product_Name VARCHAR(50),Cost_Price INT,Selling_Price INT,Quantity INT);")

cur.execute("CREATE TABLE IF NOT EXISTS Orders(Product_Category VARCHAR(50),Product_Code VARCHAR(50),Product_Name VARCHAR(50),Quantity INT,Cost_Price INT,Amount INT);")

cur.execute("CREATE TABLE IF NOT EXISTS Sales(Product_Category VARCHAR(50),Product_Code VARCHAR(50),Product_Name VARCHAR(50),Date DATE,Quantity INT,Selling_Price INT,Amount INT,Profit INT);")

cur.execute("CREATE TABLE IF NOT EXISTS Users(User_Id VARCHAR(50),Password VARCHAR(50));")

print("! Database Created Successfully !")

        
grocery_shop_management()


db.commit()