def intersected(List1, List2):
    new_list =[num for num in List1 if num in List2]
    return new_list

List1 =[1,2,3,4]
List2 =[4,5,6,3,8]
List3 = intersected(List1, List2)
print(List3)
