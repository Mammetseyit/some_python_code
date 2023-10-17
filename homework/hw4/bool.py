#Boolean1
# a=int(input("enter A: "))
# st=a>0
# print(f"{a} is a positive number - {st}")
#########################################
#Boolean2
# a=int(input("enter A: "))
# st=a%2==1
# print(f"{a} is an odd number - {st}")
######################################
#Boolean3
# a=int(input("enter A: "))
# st=a%2==0
# print(f"{a} is an even number - {st}")
#######################################
# #Boolean4
# a=int(input("enter A: "))
# b=int(input("enter B: "))

# st=(a>2 and b<=3)
# print(f"{a}>2 and {b} <=3 is - {st}")
################################
#Boolean5
# a=int(input("enter A: "))
# b=int(input("enter B: "))

# st=(a>=0 or b<-2)
# print(f"{a}>=0 or {b}<-2 is - {st}")
#######################################
#Boolean6
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))

# st=(a<b and b<c)
# print(f"{a}<{b}<{c} is - {st}")
#########################################
# # Boolean7
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))

# st=(a<b and b<c) or (c<b<a)
# print(f"{b} is between {a} and {c}    - {st}")
#########################################
#Boolean8
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# st=(a%2==1 and b%2==1)
# print(f"{a} and {b} are odd numbers - {st}")
###############################################
#Boolean9
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# st=(a%2==1 or b%2==1)
# print(f"At least one of {a} or {b} is an odd number - {st}")
################################################
#Boolean10
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# st=((a+b)%2==1)
# print(f"Exactly one of {a} and {b} is an odd number - {st}")

#############BY Allamyrat
# c=(a%2==1)
# d=(b%2==1)
# e=(c!=d)
# print("result",e)

#################################################
# Boolean11
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# st=((a+b)%2==0)
# print(f"{a} and {b} have equal parity - {st}")
############################################
#Boolean12
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))
# st=(a>0 and b>0 and c>0)
# print(f"All the numbers {a}, {b} and {c} are positive - {st}")
##############################################
#Boolean13
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))
# st=(a>0 or b>0 or c>0)
# print(f"At leat one of {a}, {b} and {c} is positive - {st}")
#################################################
#Boolean14
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))
# st=((a>0 and b<0 and c<0)or(a<0 and b>0 and c<0) or (a<0 and b<0 and c>0))
# print(f"Exactly one of {a}, {b} or {c} is positive - {st}")
#################################################
# #Boolean15
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))
# st=((a>0 and b>0 and c<0)or(a>0 and b<0 and c>0) or (a<0 and b>0 and c>0))
# print(f"Exactly two of {a}, {b} or {c} is positive - {st}")
#####################################################
# # #Boolean16
# a=int(input("enter A: "))
# st=(a<100 and a>9 and a%2==0)
# print(f"{a} is a two digit even number - {st}")
###################################################
#Boolean17
# a=int(input("enter A: "))
# st=(a<1000 and a>99 and a%2==1)
# print(f"{a} is a two digit odd number - {st}")
###################################################
#Boolean18
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))

# st=(a==b or b==c or a==c)
# print(f"Among {a}, {b} and {c} there is at least one pair of equal integers - {st}")

###################################################
#Boolean19
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))

# st=(a==-b or b==-c or a==-c)
# print(f"Among {a}, {b} and {c} there is at least one pair of opposite ones - {st}")
###################################################
#Boolean20
#onunden dagatmaly
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))

# st=(a!=b and b!=c and a!=c)
# print(f"All {a}, {b} and {c} are different integers - {st}")
###################################################
#Boolean21
#onunden dagytmaly
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))

# st=(a<b and b<c)
# print(f"All {a}, {b} and {c} are in ascending order - {st}")
###################################################
#Boolean22
#onunden dagatmaly
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))

# st=((a<b and b<c) or (a>b and b>c))
# print(f"All {a}, {b} and {c} are in ascending or decending order - {st}")
######################################################
#Boolean23
# a=int(input("enter A: "))
# a1=(a//1000)
# a2=(a%1000)//100
# a3=(a%100//10)
# a4=a%10

# st=(a1==a4 and a2==a3)

# print(f"The numbers are read equally from left to right vice versa - {st}")
########################################################
#Boolean24
# a=int(input("enter A: "))
# b=int(input("enter B: "))
# c=int(input("enter C: "))

# discr=b**2-4*a*c
# st=(discr>=0)

# print(f"The quaratic equation {a}x^2+{b}x+c with D={discr} has real roots - {st}")
#########################################################
#Boolean25
# x=int(input("enter X: "))
# y=int(input("enter Y: "))

# st=(x>=0 and y<=0) and (x!=0 or y!=0)

# print(f"({x},{y}) point is in the fourth coordinate quarter - {st}")
########################################################
#Boolean26
# x=int(input("enter X: "))
# y=int(input("enter Y: "))

# st=(x<=0 and y>=0) and (x!=0 or y!=0)

# print(f"({x},{y}) point is in the second coordinate quarter - {st}")
#############################################
#Boolean27
# x=int(input("enter X: "))
# y=int(input("enter Y: "))

# st=((x>=0 and y<=0) or (x<=0 and y<=0)) and (x!=0 or y!=0)

# print(f"({x},{y}) point is in the fourth or third coordinate quarter - {st}")
#############################################
#Boolean28
# x=int(input("enter X: "))
# y=int(input("enter Y: "))

# st=((x>=0 and y>=0) or (x<=0 and y<=0)) and (x!=0 or y!=0)

# print(f"({x},{y}) point is in the first or third coordinate quarter - {st}")
#############################################
#Boolean29
# x=int(input("enter X: "))
# y=int(input("enter Y: "))
# x1=int(input("enter X1: "))
# y1=int(input("enter Y1: "))
# x2=int(input("enter X2: "))
# y2=int(input("enter Y2: "))

# st=(x1<=x<=x2 and y1>y>y2)

# print(f"{x},{y} is within the rectangle {x1},{y1} - {x2},{y2}- {st}")
#################################################
#Boolean30
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# c=int(input("enter c: "))

# st=(a==b and b==c)
# print(f"Triangle with sides {a},{b},{c} is a equilateral triangle- {st}")
##############################################
# #Boolean34
# x=int(input("enter x: "))
# y=int(input("enter y: "))

# st=((x%2==0 and y%2==1) or (x%2==1 and y%2==0))
# print(f"{x}, {y} is white- {st}")

#########################################
# #Boolean35
# x1=int(input("enter x1: "))
# y1=int(input("enter y1: "))
# x2=int(input("enter x2: "))
# y2=int(input("enter y2: "))

# st1=((x1%2==0 and y1%2==1) or (x1%2==1 and y1%2==0)) 
# st2=((x2%2==0 and y2%2==1) or (x2%2==1 and y2%2==0))
# stresult=st1==st2
# print(f"Both same color- {stresult}")
