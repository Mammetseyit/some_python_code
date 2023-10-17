#Integer1
# l=int(input("enter distance L in centimeters: "))
# m=l//1000
# print(f"It is {m} full meters")
############################
#Integer2
# m=int(input("enter weight M in kilograms: "))
# t=m//1000
# print(f"It is {t} full tons")
##########################################
#Integer3
# b=int(input("enter file size in bytes: "))
# k=b//1024
# print(f"It is {k} full Kbytes")
######################################
#Integer4
# a=int(input("A: "))
# b=int(input("B: "))
# c=a//b
# print(f"You can place {c} Bs in an A without overlap")
##############################
#Integer5
# a=int(input("A: "))
# b=int(input("B: "))
# c=a%b
# print(f"Length ramaining after placing B into A is: {c}")
##################################
#Integer6
# a=int(input("Enter a two digit number: "))
# a1=a//10
# a2=a%10
# print(f"Tens digit is: {a1}")
# print(f"Ones digit is: {a2}")
######################################
#Integer7
# a=int(input("Enter a two digit number: "))
# a1=a//10
# a2=a%10
# sum=a1+a2
# product=a1*a2
# print(f"Sum of digits is: {sum}")
# print(f"Product of digits is: {product}")
###################################
#Integer8
# a=int(input("Enter a two digit number: "))
# a1=a//10
# a2=a%10
# result=a2*10+a1
# print(f"Result with exchanged digits is: {result}")
####################################
# Integer9
# a=int(input("Enter a three digit number: "))
# a1=a//100
# print(f"A undreds digit is: {a1}")
###################################
#Integer10
# a=int(input("Enter a three digit number: "))
# a1=a%10
# a2=(a%100)//10
# print(f"Ones digit is: {a1}")
# print(f"Tens digit is: {a2}")
#######################################
#Integer11
# a=int(input("Enter a three digit number: "))
# a1=a%10
# a2=(a%100)//10
# a3=a//100
# sum=a1+a2+a3
# product=a1*a2*a3
# print(f"Ones digit is: {a1}")
# print(f"Tens digit is: {a2}")
# print(f"Hundreds digit is: {a3}")
# print(f"Sum of digit is: {sum}")
# print(f"Product of digit is: {product}")
#####################################
#Integer24 ##If Jan1 was Monday
#day=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# k=int(input("Enter K-th day of a year(range 1-365): "))
# a1=k%7
# print(f"The K-th day was the {a1} day of the week")
#print("")
# ###################################
#Integer25 ##If Jan1 was Thursday
# k=int(input("Enter K-th day of a year(range 1-365): "))
# a1=k%7
# print(f"The K-th day was the {a1+3} day of the week")
########################################
# Integer28 ##If Jan1 was Nth day
# k=int(input("Enter K-th day of a year(range 1-365): "))
# n=int(input("Enter Jan 1 as n-th day of a wek (range 1-7): "))
# a1=(k+n-1)%7
# print(f"The K-th day was the {a1} day of the week")
#########################################
# #Integer29 #edip bilmedim
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# req=a*b
# placed_sqr=req//(c*c)
# area_left=req%(c*c)
# print(f"{placed_sqr} can be placed in a A*B reqtangle")
# print(f"{area_left} are is left empty")

#######################

# #Integer29 #edip bilmedim
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
numb_sqr=int(int(a/c)*int((b/c)))
unused_prt= int(int(a*b)-int(numb_sqr*pow(c,2)))
print("Sqrs in a reqtangle", numb_sqr)
print("Unused part", unused_prt)

#####################
# Integer30
# year=int(input("Enter year AD: "))
# cent=year//100+1
# print(f"Its {cent} century")