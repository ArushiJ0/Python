#Check if array is sorted
arr = [ 7, 6 , 5 , 2 , 1 , 3,8]
for i in range (len(arr) -1 ):
    if arr[i] > arr[i+1] :
        print("The array is not sorted")
        break 
    else:
      print("Array is sorted")
        
    
    
