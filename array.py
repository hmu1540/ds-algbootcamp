# Created by Huimin on 10/31/2021

from array import *

arr1 = array('i', [1,2,3,4,5,6])


arr2 = array('d', [1.1, 1.2, 1.3, 1.4, 1.5])


arr1.insert(2, 0)
#print(arr1)

""" def traverseArr(arr):
    for i in arr:
        print(i)

traverseArr(arr1) """

""" def accessElement(arr, index):
    if index >= len(arr):
        print('There is no element in this index.')
    else:
        print(arr[index])

accessElement(arr1, 7) """

""" def searchArr(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return  "The element does not exist in this array."

print(searchArr(arr1, 7)) """

""" arr1.remove(4)
print(arr1) """


# Create an array and traverse

my_array = array('i', [1,2,3,4,5])

""" for i in my_array:
    print(i)

# Access individual elements thr indexes
print('Step 2')
print(my_array[3])

# Appedn any value ot the array using append() method

print('Step 3')
my_array.append(6)
print(my_array)
 
# Insert value in an arr using insert()

print('Step 4')
my_array.insert(0, 0)
print(my_array) 

# Extend phtyon array using extend()
print('Step 5')
"""
my_array1 = array('i', [10, 11, 12])
my_array.extend(my_array1)



# Add items from list into array using fromlist()
tempList = [20, 21, 22]
my_array.fromlist(tempList)
print(my_array)

# Remove any array element using remove()

my_array.remove(11)
print(my_array)


# Remove last elem using pop()
my_array.pop()
print(my_array)


# Fetch any element thr its index using index()
print(my_array.index(21))

# Reverse a python array using reverse()

my_array.reverse()
print(my_array)


# Get array buffer information thr buffer_info
print(my_array.buffer_info())

# Check for numebr of occurences of an element using count()
my_array.append(11)
my_array.append(11)
print(my_array.count(11))


# Conver aarray to string using tostring()
strTemp = my_array.tostring()
print(strTemp)
ints = array('i')
ints.fromstring(strTemp)
print(ints)

# Convert array to lsit using tolist()

print(my_array.tolist())

# Append a string to char arr using fromsting()

# slice
print(my_array[1:4])
