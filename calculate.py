f_num = int(input("Enter first number : "))
sec_num = int(input("Enter second number : "))
all_f_num = id(f_num)
print("Location of first number : " ,all_f_num)


hex_sec_num = hex(sec_num)
print("Location of second number : " ,hex_sec_num)

a1 =  f_num + sec_num
print("Answer of addition  = " , f_num + sec_num)

a2 =  f_num * sec_num
print("Answer of multiplication  = " , f_num * sec_num)


a3 = f_num - sec_num
a4 = f_num / sec_num
if f_num > sec_num : 
    print("Answer  of subtration = " ,f_num - sec_num)
    print("Answer of divsion  = " ,f_num / sec_num)

a5 = sec_num - f_num
a6 = sec_num / f_num
if f_num < sec_num :
    print("Answer of subtration = " ,sec_num - f_num)
    print("Answer of divsion = " ,sec_num / f_num)

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

