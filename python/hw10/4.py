import random

list1 = []
for i in range(10):
    list1.append(random.randint(0, 100))
print(list1)


def maxim(list1):
    if len(list1) == 2:

        if list1[0] > list1[1]:

            return list1[0]

        else:

            return list1[1]

    if list1[0] > maxim(list1[1:]):

        return list1[0]

    else:

        return maxim(list1[1:])


print(maxim(list1))
