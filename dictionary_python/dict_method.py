#dictionary methods in python
my_dict = {'name':'anish prakash', 'age':'25','address':'bihar','education':'graducation'}
#1. clear() method 
# my_dict.clear()
print(my_dict)




#2. copy() method
my_dict_copy = my_dict.copy()
print(my_dict_copy)


#3. fromkeys() method
my_dict_fromkeys = dict.fromkeys(['name','age','address','education'],'nan')
print(my_dict_fromkeys)


#4. get() method
print(my_dict.get('name1','N/A'))


#5. items() method
print(my_dict.items())

#6. keys() method
#7. pop() method
#8. popitem() method
#9. setdefault() method
#10. update() method
#11. values() method