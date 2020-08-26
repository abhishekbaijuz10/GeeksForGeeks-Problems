my_list = [{ "name" : "Nandini", "age" : 20},  
{ "name" : "Manjeet", "age" : 20 }, 
{ "name" : "Nikhil" , "age" : 19 }] 

print(sorted(my_list, key = lambda i: (i['age'], i['name'])))
print(sorted(my_list, key = lambda i: (i['age'], i['name']), reverse = True))