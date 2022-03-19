def search(list1,num):
    for i in range (len(list1)):         #need a number that increments , thus for loop till the end of list [len(list1) -1 not used ,yea ik we 					
                                         #want index which is len-1 BUT range already skips the last elment] 
        if list1[i]==num:    
            print(f" number found at index {i} ")
            break
        
    else:
        print(" num not found in array/list")

list1=[23,3,11,24,63]

print(list1)

num = int(input("enter the number's index you want to find "))

search(list1 , num )



