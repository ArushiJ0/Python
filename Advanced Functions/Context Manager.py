def context_manager (List,filename):
    try:
        with open(filename,'w') as f:
            for x in List:
                f.write(f'{x}')
    except IOError:
        print("Error has occurred",IOError)

List = [1,2,3,4,5,6]
context_manager(List,'List.txt')    
