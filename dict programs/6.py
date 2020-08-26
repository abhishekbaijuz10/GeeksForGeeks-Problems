from operator import itemgetter

my_list = [{ "name" : "Nandini", "age" : 20},  
{ "name" : "Manjeet", "age" : 20 }, 
{ "name" : "Nikhil" , "age" : 19 }] 

print(sorted(my_list, key = itemgetter('age',), reverse = True))

print(sorted(my_list, key = itemgetter('age', 'name')))

print(sorted(my_list, key = itemgetter('age')))