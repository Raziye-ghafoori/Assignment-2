import random

choos=["✋","✊","✌"]
conter_computer=0
conter_user =0
while True :
    user=input("enter your chooses:")
    computer=random.choice(choos)
    print("Computer:",computer)
    if computer == "✋":
        if user == "✊":
            conter_computer+=1
        elif user== "✌":
            conter_user+=1
    elif computer == "✊":
        if user == "✌":
            conter_computer+=1
        elif user== "✋":
            conter_user+=1
    elif computer == "✌":
        if user == "✋":
            conter_computer+=1
        elif user== "✊":
            conter_user+=1
    if conter_computer == 5 or conter_user == 5:
        break

if conter_user== 5:
    print ("👏👏 YOU WIN 👏👏")  
else:
    print("😈SORRY YOU LOST😈")

