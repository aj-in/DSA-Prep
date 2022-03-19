list1=[12, 15, 17, 19, 21, 24, 45, 67]
print(list1)
num_to_find=int(input("enter the number's index you want to find from above list/array "))



def binary_search(list1 , num_to_find ):
    left_index=0
    right_index=len(list1)-1    # we want index i.e len - 1 [cuz it starts from 0]
    mid_index=0
    
   
    
    
    while left_index < right_index : # this will be always true 
        
        mid_index = (left_index+right_index)//2   # this is inside while loop cuz we want it to be dynamic
        mid_number=list1[mid_index]
        
        if num_to_find == mid_number:
            return mid_index
            
        if num_to_find > mid_number :
            left_index = mid_index +1   # mid_index +1 cuz we know mid_index is not num_to_find so we skip the middle index
            
        else :
            
            right_index = mid_index -1
            
    return "nowhere in the list/array"
    
    
index=binary_search(list1,num_to_find)
print(f"num found at index {index}")





