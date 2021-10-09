import math
from typing import Dict

while True:
    print("enter your choos:")
    print("""1. +
    2. *
    3. /
    4. -
    5. sin
    6. cos
    7. tan
    8. cot
    9. log
    10. ext
    """)
    vorodi=input()

    if vorodi== "+":
        a=int(input("enter frst number: "))
        b=int(input("enter secend number: "))
        c=a+b
        print(c)
    elif vorodi== "*":
        a=int(input("enter frst number: "))
        b=int(input("enter secend number: "))
        c=a*b
        print(c)
    elif vorodi== "-":
        a=int(input("enter frst number: "))
        b=int(input("enter secend number: "))
        c=a-b
        print(c)
    elif vorodi== "/":
        a=int(input("enter frst number: "))
        b=int(input("enter secend number: "))
        if b==0:
            print("we can\'t division")
        else:
            c=a/b
        print(c)
    elif vorodi== "sin":
        a=int(input("enter  number: "))
        c=math.sin(a)
        print(c)
    elif vorodi== "cos":
        a=int(input("enter  number: "))
        c=math.cos(a)
        print(c)
    elif vorodi== "tan":
        a=int(input("enter  number: "))
        if a==90:
            c="∞"
        else:
           c=math.tan(a)
        print(c)
    elif vorodi== "cot":
        a=int(input("enter  number: "))
        if math.tan(a)==0:
            c="∞"
        else:
            c=1/(math.tan(a))
        print(c)
    elif vorodi== "log":
        a=int(input("enter  number: "))
        c=math.log(a)
        print(c)
    elif vorodi=="ext":
        print("Good  by!!!👋")
        break
    else:
        print("eror!!!\nenter again!!")
    print("-------------------------")
        