import random

countH=0
countT=0

for n in range(0,10):
    num =random.randint(0,1)
    if num==0:
        print("H")
        countH+=1
    else:
        print("T")
        countT+=1
print(countH,countT)   
     