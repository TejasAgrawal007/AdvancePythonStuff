# a = "Hey You are The Best programmer!."


# ***----Basic Of String----***
# 1. Len
# print(len(a))

# 2. Index
# index = len(a) - 1
# print(index)

# 3. ConCanite a String
# str = 'Computer ' + 'Science'
# print(str)

# 4. * Operator Use
# str = 'Hi' * 3
# print(str)


# 5. Max
# key = max('AT', 'AB', 'AC')
# print(key)

# 6. Min
# key = min('Tejas', 'Suraj', 'Akash')
# print(key)


# ***----Sclicing in String----***

from itertools import count


message = "Hey We are The Best programmer"


# 1. Baisc Of Sclicing
# print(message[0:19])

# 2. Negative Sclicing
# print(message[-19:-10])

# 3. Advance Sclicing
# a)  print(message[:19])
# b)print(message[:])

# 4. Merge The String Using Advance process
# a = message[:5] + message[5:]
# print(a)

# a = message[:15] + message[15:]
# print(a)

# 5. Skip 2nd Char in a String
# print(message[0:len(message):2])


# ***----MemBerShip  in String----***

# 1. In Use
# h = "hello"
# print(h in "hello")


# 2 . Printing a pattern
# helloSpace = ""
# for ch in 'hello':
#     helloSpace = helloSpace + ch + ' '
#     print(helloSpace)


# helloSpace = ""
# for ch in 'hello':
#     helloSpace = helloSpace + ch + ' '
# print(helloSpace)


# 1. Program To Find Number of matched Characters in two String.

# str1 = "Tejas"
# str2 = "Siya"

# def Matched(str1, str2):

#     temp1 = str1.lower()
#     temp2 = str2.lower()


#     count = 0
#     for ch1 in temp1:
#         for ch2 in temp2:
#             if ch1 == ch2:
#                 count += 1
#     return count


# print(Matched('Tejas ', 'Tejas'))
