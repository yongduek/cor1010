# random numbers!

import random
import numpy as np 
# pip install numpy
# pip3 install numpy for Mac

number = random.randint(1, 20)
print(number)

# generate 100 random numbers
# put them in a list
# print

listOfRandomNumbers = []
for i in range(100):
    n = random.randint(1, 20)
    listOfRandomNumbers.append(n)
#
print(listOfRandomNumbers)

list2 = [random.randint(1, 20) for i in range(100)]
print(list2)
print("length of list2 is",  len(list2))

# compute the sum of them
total = 0 # listOfRandomNumbers[0] + listOfRandomNumbers[1] + ... + listOfRandomNumbers[99]
for number in listOfRandomNumbers:
    total = total + number
#
totalsum = sum(listOfRandomNumbers)
print("total: ", total, totalsum)


# npnumber = np.random.