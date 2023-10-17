#if1
# a=int(input("Enter integer value: "))

# if a>0:
#     a+=1
# print("The result is: ", a)

################################

# #if5
# a=int(input("Enter integer a: "))
# b=int(input("Enter integer b: "))
# c=int(input("Enter integer c: "))

# positive=0
# negative=0

# if a>0:
#     positive+=1
# elif a<0:
#     negative+=1
# if b>0:
#     positive+=1
# elif b<0:
#     negative+=1
# if c>0:
#     positive+=1
# elif c<0:
#     negative+=1


# print("The number of positives you have entered: ", positive)
# print("The number of negative you have entered: ", negative)
################################################################
#if6

# a=int(input("Enter a: "))
# b=int(input("Enter b: "))

# if a>b:
#     print("The bigger one is: ", a)
# elif a<b:
#     print("The bigger one is: ", b)
# else:
#     print("Both numbers are equal")

################################################################
#if16
# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# c=int(input("Enter c: "))

# if a<=b:
#     if b<=c:
#         a+=a
#         b+=b
#         c+=c
# else:
#     a=-a
#     b=-b
#     c=-c
# print(f"a={a},b={b},c={c}")

################################################################
#if19
# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# c=int(input("Enter c: "))
# d=int(input("Enter d: "))

# if a!=b and a!=c and a!=d:
#     print("The first value differs from others.")
# if b!=a and b!=c and b!=d:
#     print("The second value differs from others.")
# if c!=a and c!=b and c!=d:
#     print("The third value differs from others.")
# if d!=a and d!=b and d!=c:
#     print("The fourth value differs from others.")

################################################################
#IF21

# x=int(input("Enter x: "))
# y=int(input("Enter y: "))

# if x==y==0:
#     print ("The function returns: 0")
# elif y==0:
#     print("The function returns: 1")
# elif x==0:
#     print("The function returns: 2")
# else:
#     print("The function returns: 3")



################################################################
#if23

# import math
# x=int(input("Enter x: "))
# func2=0

# if x>0:
#     func2=2*math.sin(x)
# else:
#     func2=6-x
# print("The function returns: ", func2)

################################################################

#if27

# x=float(input("Enter x: "))

# if x<0:
#     print("The function returns: ", 0)
# elif (x%2-1<0):
#     print("The function returns: ", 1)
# else:
#     print("The function returns: ", -1)

################################################################
#28
# year=int(input("Enter year: "))


# if year==1200 or year==2000:
#     print("The year has 366 days")

# elif year%4==0:
#     if year%100==0 and year%400!=0:
#         print("The year has 365 days")
#     else:#     print("The year has 365 days")
#         print("The year has 366 days")
# else:
#     print("The year has 365 days")
###########################################
#IF29




################################################################
#if9

# a=int(input("Enter a: "))
# b=int(input("Enter b: "))

# if a>b:
#     c=a
#     a=b
#     b=c
#     print(f"a={a} and b={b}")
# else:
#     print(f"a={a} and b={b}")

################################################################

#IF10

# a=int(input("Enter a: "))
# b=int(input("Enter b: "))

# if a!=b:
#     a=b=a+b
# else:
#     a=b=0
# print(f"a={a} and", f"b={b}")

#######################################
#IF12

# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# c=int(input("Enter c: "))

# if a>b>c:
#     print(c)
# elif a>c>b:
#     print(b)
# else:
#     print(a)

#case2

# k=int(input("Enter k: "))
# mark=["bad", "unsatisfactory","mediocre", "good", "excellent"]


# if 6>k>0:
#     k=k-1
#     result=mark[k]
#     print(result)
# else:
#     print("range is 1 to 5")

#case2 version 2

# mark={
#     1:"bad", 
#     2:"unsatisfactory", 
#     3:"medicore", 
#     4:"good",
#     5:"excellent",
# }

# k=int(input("Enter k: "))

# if 0<k<6:
#     print(mark[k])
# else:
#     print("range is 1 to 5")

###############################

#case5

# a=int(input("Enter a: "))
# b=int(input("Enter b: "))

# n=int(input("Enter N: "))

# if 0<n<5:
#     if n==1:
#         c=a+b
#     elif n==2:
#         c=a-b
#     elif n==3:
#         c=a*b
#     elif n==4:
#         c=a/b

#case16
digit1=["","one","two","three","four","five","six","seven","eight","nine"]
digit2=["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
digit10=["","","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

a=int(input("age: "))

if a==0:
    pass
    #    print(f"if is spelled as: ZERO")
elif 0<a<10:
    pass
    #    print(f"if is spelled as: {digit1[a]}")
elif 10<=a<20:
    pass
    #    print(f"if is spelled as: {digit2[a-10]}")
elif 20<=a<70:
    b=a//10
    print(f"if is spelled as: {digit10[b]} {digit1[a-b*10]} years")
else:
    print("Error in range")
