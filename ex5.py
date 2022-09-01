user1 = input("Enter Usrename: ", )
pass1 = input("Enter Password: ", )
counter=1
while counter < 3:
    if user1 == 'python' and pass1 == 'rules':
         print("welcom")
         break
    else:
        user1 = input("Enter Usrename: ", )
        pass1 = input("Enter Password: ", )
     counter = counter + 1
print("access denied")





