a=int(input("Give me number 1 : "))
b=int(input("Give me number 2 : "))
x=input("Give me your function (+,-,*,/) : ")


def add(a,b):
    print(a+b)
    
if x == "+":
    add(a,b)
    
def sub(a,b):
    if a > b :
        print (a-b)
    elif a < b :
        print (b-a)
if x == "-":
    sub(a,b)
    
def multi(a,b):
    print (a*b)
if x == "*":
    multi(a,b)
    
def dev(a,b):
    if a > b :
        print (a/b)
    elif a < b :
        print (b/a)
if x == "/":
    dev(a, b)
    

