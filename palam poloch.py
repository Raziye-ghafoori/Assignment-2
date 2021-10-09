import random

choos=["✋","🤚"]
c_u=0
c_c1=0
c_c2=0

while True :
    user=input("enter your chooses:")
    computer1=random.choice(choos)
    computer2=random.choice(choos)
    print("Computer1:",computer1)
    print("Computer2:",computer2)

    if computer1=="✋":
        if computer2 =="✋":
            if user=="🤚":
                c_u+=1
    elif computer1=="🤚":
        if computer2 =="🤚":
            if user=="✋":
                c_u+=1
    elif user=="✋":
        if computer2 =="✋":
            if computer1=="🤚":
                c_c1+=1
    elif user=="🤚":
        if computer2 =="🤚":
            if computer1=="✋":
                c_c1+=1
    elif user=="✋":
        if computer1 =="✋":
            if computer2=="🤚":
                c_c2+=1
    elif user=="🤚":
        if computer1 =="🤚":
            if computer2=="✋":
                c_c2+=1
    if c_c1 == 5 or c_u == 5 or c_c2 ==5:
        break
    
if c_u== 5:
    print ("👏👏 YOU WIN 👏👏")  
elif c_c1== 5:
    print("""😈SORRY YOU LOST😈
    computer1 win""")
else:
     print("""😈SORRY YOU LOST😈
    computer2 win""")
