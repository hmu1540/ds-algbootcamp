# Calculate the averate temperature

numDays = int(input('How many days temperature?'))

""" total = 0

for i in range(1, numDays + 1):
    nextDay = input("Day " + str(i) + " 's high temp:")
    total += nextDay

avg = round(total / numDays, 2)
print("\nAverage = " + str(avg)
 """

total = 0
temp = []
for i in range(numDays):
    nextDay = int(input("Day " + str(i + 1) + " 's high temp:"))
    temp.append(nextDay)
    total += temp[i]

avg = round(total / numDays, 2)
print("\nAverage = " + str(avg))

above = 0

for i in temp:
    if i > avg:
        above += 1

print(str(above) + " day(s) above avarage temperature.")