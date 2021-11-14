# Created by Huimin on 10/31/2021

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [ 15, 18, 14, 9]])
print(twoDArray)
""" def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverseTDArray(twoDArray)     

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index ' + str(i) + " " + str(j)

    return "The ele is not found."
print(searchTDArray(twoDArray, 655))
"""   

newTDArr = np.delete(twoDArray, 0, axis=1)
print(newTDArr)