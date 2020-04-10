#ask for age 
age = input("how old are you: ")

if age:
    #18-21 you wear a wrist band 
    if int(age) >= 18 and int(age) < 21:
        print("you can enter but you need a wrist band")
    #21+ drink, normal entry 
    elif int(age) >= 21:
        print("you are good to enter and can drink")
    #too young, sorry
    else: 
        print("you are too young buddy!")
else: 
    print("please run the program again and enter an age or you will not be granted access")

