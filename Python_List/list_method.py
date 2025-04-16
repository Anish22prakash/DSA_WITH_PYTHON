import numpy as np

myIntegerList = [10, 20, 30, 40, 50, 60]
myStringList = ['anish', 'bam', 'baaish']

a = 'spam-spam-spam'
b = a.split("-")               # ['spam', 'spam', 'spam']
delimeter = '-'

print(delimeter.join(b))       # 'spam-spam-spam'

# list comprehension
updatedlist = [item*2 for item in myIntegerList]
print(updatedlist)

randomList = [-20,-90,-9,4,5,-5,89,23]
positiveList = [i for i in randomList if i > 0]
print(positiveList)
