n=int(input("Enter the count of fibonnaci numbers you want "))
first=0
second=1
for i in range(n):
    print(first)
    temp=first
    first=second
    second=temp+second
    
    
#     OR

def fib(n):
    
    
    if n==1:
        return 0
    if n==2:
        return 1
        
    if n>2:
        return fib(n-1)+fib(n-2)             // sum of last 2 num
        
for n in range(1,3):                 // change this value
    
    print(n , ":" ,fib(n))
