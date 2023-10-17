print("Welcome to the gift lottery! \nYour 'Gift' is for a Boy, Girl, or is it a punishment?: \n")

lottery={
    "Boy":{
        "opt1":"Ball",
        "opt2":"T-Shirt",
        "opt3":"Polo",
    },
    "Girl":{
        "opt1":"Doll",
        "opt2":"Dress",
        "opt3":"Bag",
    },
    "Punishment":{
        "opt1":"Punch",
        "opt2":"Kick",
        "opt3":"Bite"
    }
}

for i in lottery:
    print (i)

print("\n")
selected=input().capitalize()

# print(f"{selected}")

import random
r=random.randrange(0,2)

converted_items=list(lottery[selected].values())

#result=lottery[selected].items()

print(f"\nCongratulations! You get a {converted_items[r]}")