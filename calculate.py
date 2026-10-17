f_num = int(input("Enter first number : "))
sec_num = int(input("Enter second number : "))
all_f_num = id(f_num)
print("Location of first number : " ,all_f_num)


hex_sec_num = hex(sec_num)
print("Location of second number : " ,hex_sec_num)

a1 =  f_num + sec_num
print("Answer of addition  = " , a1)

a2 =  f_num * sec_num
print("Answer of multiplication  = " , a2)


a3 = f_num - sec_num
a4 = f_num / sec_num
if f_num > sec_num : 
    print("Answer  of subtration = " ,a3)
    print("Answer of divsion  = " ,a4)

a5 = sec_num - f_num
a6 = sec_num / f_num
if f_num < sec_num :
    print("Answer of subtration = " ,a5)
    print("Answer of divsion = " ,a6)

hex_a1 = hex(a1)
print("Location of addition answer  : " ,hex_a1)


all_a2 = id(a2)
print("Location of multiplication answer : " ,all_a2)

hex_a3 = hex(a3)
print("Location of  subtration answer  : " ,hex_a3)

all_a4 = id(a4)
print("Location of divsion answer : " ,all_a4)


hex_a5 = hex(a5)
print("Location of  subtration answer  : " ,hex_a5)

all_a6 = id(a6)
print("Location of divsion answer : " ,all_a6)

