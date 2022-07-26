def search(list1,num):
    for i in range (len(list1)):         #need a number that increments , thus for loop till the end of list [len(list1) -1 not used ,yea ik we 					
                                         #want index which is len-1 BUT range already skips the last element] 
        if list1[i]==num:    
            print(f" number found at index {i} ")
            break                                  # this breaks out of loop if num found ,  n doesnt execute else block
        
    else:
        print(" num not found in array/list")

list1=[23,3,11,24,63]

print(list1)

num = int(input("enter the number's index you want to find "))

search(list1 , num )



# simpler method

# list1=[23,3,11,24,63]

# num = 1

# for i in list1:
#     if num == i:
#         print(f"num found at {list1.index(i)} index" )           # list_name . index (index_no.)   # this returns the index val
#         break                              # this wont search for others if num found  ,does this break out of every indent?
    
# else:
#     print("num not found")         # why wont this be executed after every unsuccesfull attempt?
    
                      
    
    
 

    
