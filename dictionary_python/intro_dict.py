# introduction to dictionary 

# dictionary is a collection of key-value pairs

my_dict = {'key1' : 'value1' , 'key2':'value2' , 'key3' : 'value3'}
print(my_dict)

print(my_dict['key1'])
my_dict['key4'] = 'value4'
print(my_dict)


# travesing through dictionary
# we can use for loop to traverse through dictionary
for itm in my_dict:
    print(itm,my_dict[itm])

# searching in the dictonary
def search_in_dict(searchValue):
    for key, value in my_dict.items():
        if value == searchValue:
            print('found !!!')
            return
    print('not found!!!')
    return
search_in_dict('value1')

# delete/ remove method in dictionay 
del my_dict['key1']
print(my_dict)
del_item = my_dict.pop('key2')
print('item deleted ',del_item)


