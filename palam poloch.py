import random

choos=["β","π€"]
c_u=0
c_c1=0
c_c2=0

while True :
    user=input("enter your chooses:")
    computer1=random.choice(choos)
    computer2=random.choice(choos)
    print("Computer1:",computer1)
    print("Computer2:",computer2)

    if computer1=="β":
        if computer2 =="β":
            if user=="π€":
                c_u+=1
    elif computer1=="π€":
        if computer2 =="π€":
            if user=="β":
                c_u+=1
    elif user=="β":
        if computer2 =="β":
            if computer1=="π€":
                c_c1+=1
    elif user=="π€":
        if computer2 =="π€":
            if computer1=="β":
                c_c1+=1
    elif user=="β":
        if computer1 =="β":
            if computer2=="π€":
                c_c2+=1
    elif user=="π€":
        if computer1 =="π€":
            if computer2=="β":
                c_c2+=1
    if c_c1 == 5 or c_u == 5 or c_c2 ==5:
        break
    
if c_u== 5:
    print ("ππ YOU WIN ππ")  
elif c_c1== 5:
    print("""πSORRY YOU LOSTπ
    computer1 win""")
else:
     print("""πSORRY YOU LOSTπ
    computer2 win""")
