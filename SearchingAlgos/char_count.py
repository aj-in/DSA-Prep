text= "dsf"

char=str(input("Enter the char you want to find  "))

if char in text:

    print (f" the character {char} is present in text")
    print (f" then character occurs {text.count(char)} times")

else:

    print("value is absent")