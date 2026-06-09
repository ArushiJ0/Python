##Write a function that rotates a list by n positions. Print the original and rotated lists.

def rotate(List,n):
    rotate_list = List[n:] +List[:n]
    return rotate_list

List =[1,2,3,4,5,6,7]
newList = rotate(List,3)
print(newList)
    
