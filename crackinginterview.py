# Created by Huimin on 11/1/2021

# Question 1 - Missing number
""" 
myList = list(range(1, 101))
myList.pop(39)

def findMissing(ls, n):
    sum1 = n * (n+1) / 2
    sum2 = sum(ls)
    return int(sum1 - sum2)

print(findMissing(myList, 100))

# Find all pairs of integers whose sum is equal to a given number.
# Instead of given solution, ask questions firstly.
# Do you want....
# pairs to be distinct numbers? 
# repetive paris if there are any
# reversive pairs
#
# Is the input array...
# all positive numbers?
# size?

# why? to show you have not marked the answer and secondly demo that you have ability to thingk

def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):  # no report of issues? no, when j in range(6, 6), it is empty.
            if nums[i] == nums[j]:
                continue
            if nums[i] + nums[j] == target:
                print(i, j)


# Whether an array contains a numer?
# want to T/F output? array size? 

def search(arr, number):
    # Linear search: in operator
    # Sorted search
    for i in range(len(arr)):
        if arr[i] == number:
            print(i)
        else:
            print("No such numebr....")

# Find max product of two number in an array where all ele are pos
# output the product only? number distinct? array size?

def findMaxProduct(arr):
    maxProduct = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] * arr[j] > maxProduct:
                maxProduct = arr[i] * arr[j]
                pairs = str(arr[i]) + ',' + str(arr[j])
    print(maxProduct)
    print(pairs)

# Determine if a list has all unique elements
# output T/F array? array size?

def isElementsUnique(arr):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j == i:
                continue
            elif arr[i] == arr[j]:
                result.append(False)
                break
        if len(result) < i + 1:
            result.append(True)
        
    print(result)

myList = [1, 2, 3, 8, 4, 5, 9]
isElementsUnique(myList)        

# a better alg
def isAllElementsUnique(ls): 
    newList = []
    for i in ls:
        if i in newList:
            return False
        else:
            newList.append(i)
    return True

print(isAllElementsUnique(myList)) """

# determin if a list is a permutation of another list.

# same elements, diff orders? 
# all same elemets, permutation?

def isPermutation(list1, list2):
    if len(list1) == len(list2):
        for i in list1:
            if i not in list2:
                return False
        
        for i in list2:
            if i not in list1:
                return False
        return True
    else:
        return False

list1 = [1, 2, 3]
list2 = [3, 2, 1, 3]

print(isPermutation(list1, list2))

# better alg

def isPermuation2(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False
        
# Rotatate matrix by 90 degree
# clock-wise?

