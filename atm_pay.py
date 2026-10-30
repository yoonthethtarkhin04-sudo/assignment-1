print ("        Deposit && Withdrawal System        ")
print("         ----------------------------        ")


have_amount = int (input("Enter you have balance amount : "))

print ("Your balance amount is ",have_amount)

print("  ")
print ("  Services")


print (''' 
           1.Cash in
           2.Cash out
           3.Transfer
           4.Internet services
           5.Top up
        ''')

choose = int (input ("Please select one service you would like to use (1-5) : "))

if choose == 1:
    add_amount = int (input("Enter amount you want to add  : "))
    
    
    
    password = 2113         
    passcode = int (input("Enter your password with 4 numbers : "))
    
    if password == passcode :                   #check password
        print ("Successful.")
        add = have_amount + add_amount
        print ("Total Balance : ",add)
    else :
     for passcode in range(4):
        print ("Wrong password.Try again.")
        passcode = int (input("Enter your password with 4 numbers : "))
        if password == passcode:
            print("Successful.")
            add = have_amount + add_amount
            print ("Total Balance : ",add)
        
     else : 
        print ("Full limit.Please try again another day.")
        
        
    
    
    
    

elif choose == 2:
    pay_amount = int (input("Enter amount you want to withdraw : " )) #check pay amount
    while have_amount < pay_amount:
        print("Your balance is insufficient.Please enter again.")
        pay_amount = int (input("Enter amount you want to withdraw : " ))
    print("Successful.")
    
    
    
    
    password = 2113         
    passcode = int (input("Enter your password with 4 numbers : "))
    
    if password == passcode :                   #check password
        print ("Successful.")
        pay = have_amount - pay_amount
        print ("Total Balance : ",pay)
    else :
     for passcode in range(4):
        print ("Wrong password.Try again.")
        passcode = int (input("Enter your password with 4 numbers : "))
        if password == passcode:
            print("Successful.")
            pay = have_amount - pay_amount
            print ("Total Balance : ",pay)
        
     else : 
        print ("Full limit.Please try again another day.")
        
    
    
    
    
    
elif choose == 3:
    phone_number = input ("Enter phone number you want to transfer (start with 09) :  ")
    count = len(phone_number)
    while   count != 11 and '0123456789' not in phone_number :      #check phone number length
        print("Wrong phone number.Enter next again.")
        phone_number = input ("Enter phone number you want to transfer (start with 09) :   ")
        count = len(phone_number)
    print("Your number is true.")
    
    
    
    
    
    pay = int (input ("Enter amount of transfer : "))
    while have_amount < pay:
        print("Your balance is insufficient.Please enter again.")       #check pay amount
        pay = int (input ("Enter amount of transfer : "))
    print("Successful.")
    
    
    
    password = 2113         
    passcode = int (input("Enter your password with 4 numbers : "))
    
    if password == passcode :                   #check password
        print ("Successful.")
        Total = have_amount - pay
        print("Total balance : ",Total)
    else :
     for passcode in range(4):
        print ("Wrong password.Try again.")
        passcode = int (input("Enter your password with 4 numbers : "))
        if password == passcode:
            print("Successful.")
            Total = have_amount - pay
            print("Total balance : ",Total)
        
     else : 
        print ("Full limit.Please try again another day.")
        
       
        
        
        
        
        
        
elif choose == 4 :
    print(" ")
    print(" ")
    print ("Internet Services Type")
    print ("......................")
    print(" ")
    print (''' 
                1.Power Fiber           2.Power Wireless
                3.Power Flexi Net      
            ''')
            
    
        
    
    phone_number = input ("Please enter Registered Mobile Number (start with 09) :  ")
    count = len(phone_number)
        
    while   count != 11 and '0123456789' not in phone_number :      #check phone number length
            print("Wrong phone number.Enter next again.")
            phone_number = input ("Enter phone number you want to transfer (start with 09) :   ")
            count = len(phone_number)
    print("Your number is true.")
            
        
    choose_internet_type = int (input ("Choose Internet Type : "))
    
        
    if choose_internet_type == 1:
        print(" ")
        print("Data Services Information")
        print(".........................")
        print(" ")
        print (''' 
                   1.150 GB for 30 days (35,999 Ks)
                   2.100 GB for 20 days (22,000 Ks)
                   3.100 GB for 30 days (29,999 Ks)
                   4.50 GB for  7 days (15,499 Ks)
                   5.80 GB for 30 days (18,999 Ks)
                   6.220 GB for 30 days (55,999 Ks)
                ''')
            
        choose_package_type = int (input ("Choose Package Type : "))
        
        if choose_package_type == 1:
             print ("Confirm")
             name = input ("Enter your name : ")
             print(" ")
             print("Bill Information ")
             print("................")
             print(" ")
             print("Name : ",name)
             print("Total : 35,999 Ks")
        elif choose_package_type == 2:
             print ("Confirm")
             name = input ("Enter your name : ")
             print(" ")
             print("Bill Information ")
             print("................")
             print(" ")
             print("Name : ",name)
             print("Total : 22,000 Ks")
        elif choose_package_type == 3:
             print ("Confirm")
             name = input ("Enter your name : ")
             print(" ")
             print("Bill Information ")
             print("................")
             print(" ")
             print("Name : ",name)
             print("Total : 29,999 Ks")
        elif choose_package_type == 4:
             print ("Confirm")
             name = input ("Enter your name : ")
             print(" ")
             print("Bill Information ")
             print("................")
             print(" ")
             print("Name : ",name)
             print("Total : 15,499 Ks")
        elif choose_package_type == 5:
             print ("Confirm")
             name = input ("Enter your name : ")
             print(" ")
             print("Bill Information ")
             print("................")
             print(" ")
             print("Name : ",name)
             print("Total : 18,999 Ks")
        elif choose_package_type == 6:
             print ("Confirm")
             name = input ("Enter your name : ")
             print(" ")
             print("Bill Information ")
             print("................")
             print(" ")
             print("Name : ",name)
             print("Total : 55,999 Ks")       
        
                
                
        if password == passcode :                   #check password
            print ("Successful.")
            
        else :
         for passcode in range(4):
            print ("Wrong password.Try again.")
            passcode = int (input("Enter your password with 4 numbers : "))
            if password == passcode:
                print("Successful.")
                
            
         else : 
            print ("Full limit.Please try again another day.")
            
    if choose_internet_type == 2:
        print(" ")
        print("Data Services Information")
        print(".........................")
        print(" ")
        print (''' 
                   1.1000 GB for 30 days (120,000 Ks)
                   2.1500 GB for 20 days (220,000 Ks)
                   3.1500 GB for 30 days (249,999 Ks)
                   4.999 GB for  7 days (99,499 Ks)
                   5.1800 GB for 30 days (559,999 Ks)
                   6.10000 GB for 30 days (990,000 Ks)
                ''')
        
        choose_package_type = int (input ("Choose Package Type : "))
        
        if choose_package_type == 1:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total : 120,000 Ks")
        elif choose_package_type == 2:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total : 220,000 Ks")
        elif choose_package_type == 3:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total : 249,999 Ks")
        elif choose_package_type == 4:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total : 99,499 Ks")
        elif choose_package_type == 5:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total : 559,999 Ks")
        elif choose_package_type == 6:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total : 990,000 Ks")
            
        else:
            print("Invalid number.Please try again.")
            choose_package_type = int (input ("Choose Package Type : "))
            
            
            
            
        password = 2113  
        print(" ")
        print(" ")
        passcode = int (input("Enter your password with 4 numbers : "))
        if password == passcode :                   #check password
            print ("Successful.")
        else :
         for passcode in range(4):
            print ("Wrong password.Try again.")
            passcode = int (input("Enter your password with 4 numbers : "))
            if password == passcode:
                print("Successful.")
            
         else : 
            print ("Full limit.Please try again another day.")
            
    elif choose_internet_type == 3:
        print(" ")
        print("Data Services Information")
        print(".........................")
        print(" ")
        print (''' 
                   1.55 GB for 30 days (15,999 Ks)
                   2.35 GB for 20 days (10,000 Ks)
                   3.35 GB for 30 days (11,000 Ks)
                   4.15 GB for  7 days (5,499 Ks)
                   5.150 GB for 30 days (29,999 Ks)
                   6.510 GB for 30 days (99,999 Ks)
                ''')
        
        choose_package_type = int (input ("Choose Package Type : "))
        
        if choose_package_type == 1:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total : 15,999 Ks")
        elif choose_package_type == 2:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total : 10,000 Ks")
        elif choose_package_type == 3:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total :11,000  Ks")
        elif choose_package_type == 4:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total : 5,499 Ks")
        elif choose_package_type == 5:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total : 29,999  Ks")
        elif choose_package_type == 6:
            print ("Confirm")
            name = input ("Enter your name : ")
            print(" ")
            print("Bill Information ")
            print("................")
            print(" ")
            print("Name : ",name)
            print("Total : 99,999 Ks")
        else:
            print("Invalid number.Please try again.")
            choose_package_type = int (input ("Choose Package Type : "))
            
            
            
        password = 2113  
        print(" ")
        print(" ")
        passcode = int (input("Enter your password with 4 numbers : "))
        if password == passcode :                   #check password
            print ("Successful.")
        else :
         for passcode in range(4):
            print ("Wrong password.Try again.")
            passcode = int (input("Enter your password with 4 numbers : "))
            if password == passcode:
                print("Successful.")
            
         else : 
            print ("Full limit.Please try again another day.")
            
            
    

        
elif choose == 5:
    phone_number = input ("Enter phone number you want to transfer (start with 09) :  ")
    count = len(phone_number)
    
    while   count != 11 and '0123456789' not in phone_number :      #check phone number length
        print("Wrong phone number.Enter next again.")
        phone_number = input ("Enter phone number you want to transfer (start with 09) :   ")
        count = len(phone_number)
    print("Your  number is true.")
    
    print ("  Amount of Bill")


    
    print (''' 
               1.1000           2.2000          3.3000          4.4000
               5.5000           6.10000         7.15000         8.20000
               9.25000         10.30000
               
            ''')
    
    int(input("Select Bill amount (1-10) : "))
    password = 2113  
    print(" ")
    print(" ")
    passcode = int (input("Enter your password with 4 numbers : "))
    if password == passcode :                   #check password
        print ("Successful.")
    else :
     for passcode in range(4):
        print ("Wrong password.Try again.")
        passcode = int (input("Enter your password with 4 numbers : "))
        if password == passcode:
            print("Successful.")
        
     else : 
        print ("Full limit.Please try again another day.")
        
    

