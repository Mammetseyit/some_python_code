# txt=str(input("Enter your text: "))
# txt_length=len(txt)
# txt2=[]

# count=0


# for i in range(txt_length):
#     txt2.append(txt[i])
#     if txt2[i]=="0" or txt2[i]=="1" or txt2[i]=="2" or txt2[i]=="3" or txt2[i]=="4" or txt2[i]=="5" \
#         or txt2[i]=="6" or txt2[i]=="7" or txt2[i]=="8" or txt2[i]=="9":
#         count+=1    
    
# print("Number of integers you have entered in your text:", count)
# print("Number of characters (including 'spaces') other than integers you have entered in your text: ", txt_length-count)


# #men aslynda stringi integere convert etjekdim, edip bilmedim.
# temp=int(txt2[0])
  

################################################

print("\n")
print("This program will count even and odd numbers you have entered\n")

n=int(input("How many numbers you wanna enter:"))
print("\n")
numbers=[]
count_even=0

for i in range(n):
    numbers.append(int(input(f"Enter number #{i+1}: ")))
    if numbers[i]%2==0:
        count_even+=1

print("\n")
print("Even numbers you have entered: ", count_even)
print("Odd numbers you have entered: ", n-count_even)

