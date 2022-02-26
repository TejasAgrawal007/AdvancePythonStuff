a# # 1. List Passed As an arguments

# def updateList(a,i,values):

#     a[i] = values

# def main():

#     lst = [10,20,30,[40,50]]
#     updateList(lst, 3, 50)
#     print(lst)

# if __name__ == "__main__":
#     main()


# ***__ Union  __***

# def union(L1,L2):
#     return list(set(L1) | set(L2))

# def main():
#     L1 = {10,20,30}
#     L2 = {40,50,10}
#     print(union(L1,L2))

# if __name__ == '__main__':
#     main()

'''
NOTE ;- 
    1) Union - ( | )
    2) difference - ( - )
    3) intersection - ( & )
'''


# program to Construct Dictionary



# def buildInvDict(dist1):

#     invDict = {}
#     for key,value in dict1.items():
#         if value in invDict:
#             invDict[value].append(key)
#         else:
#             invDict[value] = [key]
#     invDict = {x:invDict[x] for x in invDict if len(invDict[x])> 1}
#     return invDict


# def main():
#     wordMeaning  = eval(input("Enter Word Meaning in Dictionary: "))
#     wordMeaning = buildInvDict(wordMeaning)
#     print("Inverted Dictionary:\n", wordMeaning)

# if __name__ == "__main__":
#     main()

