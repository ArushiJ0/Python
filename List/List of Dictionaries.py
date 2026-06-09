List = [{"name" : "A" , "score" : 30 },{ "name" : "B" ,"score": 79 },
        {"name" :"C" ,"score" : 66 },{"name ": "D", "score": 80}]
print(sorted(List,key = lambda x : x['score'], reverse = True))

