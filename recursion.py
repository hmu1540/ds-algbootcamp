""" import sys
sys.setrecursionlimit(10000) # increase stack mem """

def factorial(n):
    """ print(n) """
    assert n >= 0 and int(n) == n, 'The number must be non-negative interger only!' # Throw an exception if n doesn't satisfy the condition.
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


# Created by Huimin Mu on 10/30/2021

def fibonacci(n):
    assert n >=0 and int(n) == n, 'Fibanacci numer cannot be negative number or non-integer!'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

""" print(fibonacci(1)) """

# Find the sume of digits of a positive integer number using recursion.

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number has to be a non-negative integer only!'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n / 10))

""" print(sumOfDigits(-11)) """

# Calculate power of a number using recursion

def power(base, exp):
    assert exp >=0 and int(exp) == exp, 'The exponent must be positive interger only!'
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

""" print(power(-1, 2))
print(power(3.2, 2))
print(power(2, -1))
print(power(2, 1.1)) """

#print(power(2, 1.1))

# Find GCD of two numbers using recursion.
# GCD: The largest positive number that divides numbers without a reaminder

def gcd(x, y):
    assert int(x) == x and int(y) == y, 'The numbers must be integer only!'
    if x < 0:
        x *= -1
    if y < 0:
        y *= -1
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

""" print(gcd(48, -18))
print(gcd(48, 18.5)) """

def decimalToBinary(n):
    assert n >= 0 and int(n) == n, 'The number must be non-negative integer number only!'
    if n == 0:
        return 0
    else:
        return n % 2 + decimalToBinary(n / 2) * 10


#decimalToBinary(-10)

""" SOLUTIONS PART 2 """

""" POWER SOLUTION
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)
FACTORIAL SOLUTION
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)
PRODUCT OF ARRAY SOLUTION
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])
RECURSIVE RANGE SOLUTION
def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)
FIBONACCI SOLUTION
def fib(num):
    if (num < 2):
        return num
    return fib(num - 1) + fib(num - 2) """

""" SOLUTIONS PART 2 """

""" REVERSE SOLUTION
def reverse(strng):
    if len(strng) <= 1:
      return strng
    return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])
IS PALINDROME SOLUTION
def isPalindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    return isPalindrome(strng[1:-1])
SOME RECURSIVE SOLUTION
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True
 
def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
FLATTEN SOLUTION
def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr
 """

def nestedEvenSum(obj, sum=0):
    # TODO
    if len(list(obj.values())) <= 1:
        if type(list(obj.values())[0]) is not dict:
            if type(list(obj.values())[0]) is int:
                if list(obj.values())[0] % 2 == 0:
                    sum += list(obj.values())[0]
                    return sum
        else:
            sum = nestedEvenSum(list(obj.values())[0], sum)
    else:
        for item in obj.items():
            sum = nestedEvenSum(dict((item,)), sum)
    return sum

# nestedEvenSum Solution

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

print(nestedEvenSum(obj1))