
inch=0
while inch >= 0:
    centimeter= inch*2.54
    print(f"{inch} inches is {centimeter} centimeters")
    inch=inch+1
    end=int(input("enter negative to end : "))
    if end < 0:
        break
