n=int(input("Enter the count of fibonnaci numbers you want "))
first=0
second=1
for i in range(n):
    print(first)
    temp=first
    first=second
    second=temp+second
    