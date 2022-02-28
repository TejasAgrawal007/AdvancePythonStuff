# Note  --> Assert statement used to debug code and handle  the Condition Code.

# 1. Program to Compute Factorial Of a Number. (Iterative Method)
# def factorial(n):

#     fact = 1
#     assert n >= 0
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact

# def main():
#     n = int(input("Enter The Number: "))
#     fact = factorial(n)
#     print("Factorial of", n, "is", fact)


# if __name__ == "__main__":
#     main()


'''
from math import factorial

n = 4 * 3 * 2 * 1
n = 3 * 2 * 1
n = 2 * 1 
n = 1  

n * factorial(n - 1)
'''


# Program to Compute a Factorial of a Number using (Recursive method)

# def factorial(n):

#     assert n >= 0
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def main():
#     n = int(input("Enter The Number: "))
#     fact = factorial(n)
#     print("Factorial of", n, "is", fact)


# if __name__ == "__main__":
#     main()


# program to Determine nth Fibonacci Terms

# def fibonacci(n):

#     assert n > 0
#     secondLast = 0
#     last = 1
#     if n == 1:
#         return secondLast
#     elif n == 2:
#         return last
#     for i in range(3, n + 1):
#         result = secondLast + last
#         secondLast  = last
#         last = result
#     return result

# def main():
#     n = int(input("Enter the Value of n: "))
#     result = fibonacci(n)
#     print(n, "th fibonacci Term", "is", result)

# if __name__ == "__main__":
#     main()


#  Fibonacci Terms

# fibo(n-1) + fibo(n-2)

# def fibo(n):

#     assert n > 0
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)


# def main():
#     n = int(input("Enter The Number: "))
#     result = fibo(n)
#     print("The Finonacci Terms of ",n, "is", result)

# if __name__ == "__main__":
#     main()


# Program to determine the length of the string.
# formula  - 1 + length(str1[1:])

# def length(str1):

#     if str1 == "":
#         return 0
#     else:
#         return 1 + length(str1[1:])

# def main():
#     str1 = input("Enter The String: ")
#     result = length(str1)
#     print("The Length of Your String is ", result)

# if __name__ == "__main__":
#     main()


# Program to reverse of a String.

# def reverse(str1):

#     if str1 == "":
#         return str1
#     else:
#         return str1[-1]+ reverse(str1[:-1])

# def main():
#     n = input("Enter Your String to Reverse: ")
#     result = reverse(n)
#     print("The Reverse string of", n , "is", result)

# if __name__ == "__main__":
#     main()


# Program to determine whether a String is a palindrome

# def isPalindrome(str1):

#     if str1 == "":
#         return True
#     else:
#         return str1[0] == str1[-1] and isPalindrome(str1[1:-1])


# def main():
#     n = input("Enter The String to Check Whether its is palindrome: ")
#     if(isPalindrome(n)):
#         print("The String is palindrome 😁")
#     else:
#         print("The String is Not palindrome 😒")


# if __name__ == "__main__":
#     main()


# Practice for Factorial

# def factorial(n):
#     fact = 1
#     assert n >= 0
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact


# def main():
#     n = int(input("Enter The Number: "))
#     fact =  factorial(n)
#     print("Factorial of", n ,"is", fact)

# if __name__ == "__main__":
#     main()

# from math import factorial


# def Factorial(n):

#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# def main():

#     n = int(input("Enter The Number: "))
#     result = Factorial(n)
#     print("The Factorial of ", n ,"is", result)

# if __name__ == "__main__":
#     main()


# Palindrome

# def isPalindrome(str1):

#     if str1 == "":
#         return True
#     else:
#         return str1[0] == str1[-1] and isPalindrome(str1[1:-1])


# def main():
#     str1 =  input("Enter Your String: ")
#     if(isPalindrome(str1)):
#         print("The String is palindrome 😁")
#     else:
#         print("The String is Not palindrome 😒")

# if __name__ == "__main__":
#     main()


# Program to Reverse a String

# def reverse(str1):

#     if str1 == "":
#         return str1
#     else:
#         return str1[-1] + reverse(str1[:-1])


# def main():
#     n = input("Enter The String: ")
#     result = reverse(n)
#     print("Reverse of String ", n, "is", result)


# if __name__ == "__main__":
#     main()


# Program to Determine Length of The String.
# Formula---:) 1 + length(Str1[1:])

# from unittest import result
# def length(str1):

#     if str1 == "":
#          return 0
#     else:
#         return 1 + length(str1[1:])

# def main():
#     str1 = input("Enter Your String to get a len:  ")
#     result = length(str1)
#     print("The Length of ", str1 , "is", result)

# if __name__ == "__main__":
#     main()


#  Program To Falttern a list

# from unittest import result

# def flatten(lst1, lst2 = []):

#     for element in lst1:
#         if type(element)!= list:
#             lst2.append(element)
#         else:
#             flatten(element, lst2)
#     return lst2


# def main():
#     lst1 = eval(input("Enter The list: "))
#     result = flatten(lst1)
#     print("Flattern List: ", result)

# if __name__ == "__main__":
#     main()


# Program to create a Flatten of a List.

# from unittest import result


# def flatten(lst1, lst2 = []):

#     for element in lst1:
#         if type(element)!= list:
#             lst2.append(element)
#         else:
# flatten(element, lst2)
#     return lst2


# def main():
#     lst1 = eval(input("Enter a List: "))
#     result = flatten(lst1)
#     print("Flatten List: ", result)

# if __name__ == "__main__":
#     main()


#  Program to create a Copy  of a List.


# def copy(lst1, lst2 = []):

#     if lst1 == []:
#         return lst2
#     else:
#         lst2.append(lst1[0])
#         copy(lst1[1:], lst2)
#     return lst2

# def main():
#     lst1 = eval(input("Enter the list: "))
#     lst2 = copy(lst1)
#     print("Copy of lst1 is = ", lst2)

# if __name__ == "__main__":
#     main()


# Program to Create a Deep Copy of a List
'''
     In a Shallow copy operations the embeed object such as 
     nested list are not copid, instead they are shared betweeen the two List.
     If we wish to copy the entire list, including embedded object's shuch a 
     copy is called deep copy. 😄
'''


# def deepCopy(lst1,lst2 = []):

#     if lst1 == []:
#         pass
#     else:
#         if type(lst1[0]) != list:
#             lst2.append(lst1[0])
#         else:
#             lst2.append([])
#             deepCopy(lst1[0], lst2[-1])
#         deepCopy(lst1[1:], lst2)
#     return lst2

# def main():
#     lst1 = eval(input("Enter the list: "))
#     lst2 = deepCopy(lst1)
#     print("Copy of lst1 deepCopy is = ", lst2)

# if __name__ == "__main__":
#     main()


# function to check if two strings are
# anagram or not
# def check(s1, s2):

# 	# the sorted strings are checked
# 	if(sorted(s1)== sorted(s2)):
# 		print("The strings are anagrams.")
# 	else:
# 		print("The strings aren't anagrams.")

# # driver code
# s1 ="listen"
# s2 ="silent"
# check(s1, s2)


# Permutation

# def permute(lst1, lst2 = [], k = 0, pos = 0):

#      lst2.insert(pos, lst1[k])

#      if len(lst2) == len(lst1):
#           print(lst2)
#      else:
#           permute(lst1, lst2, k+1, 0)

#      lst2.remove(lst1[k])

#      if pos < k:
#           permute(lst1, lst2, k, pos+1)

# def main():
#      n = eval(input("Enter a list: "))
#      permute(n)


# if __name__ == "__main__":
#      main()


# Program  to solve the Tower of Honai

# from numpy import source


# def honai(n, source, spare, target):

#      if n == 1:
#           print("Move a Disk from", source, "to", target)
#      elif n == 0:
#           return
#      else:
#           honai(n-1, source,  target, spare)
#           print("Move a Disk from", source, "to", target)
#           honai(n-1, spare,  source, target)

# def main():
#      n = int(input("Enter The Number of Disk: "))
#      source = int(input("Enter The Source Pole "))
#      spare = int(input("Enter The spare Pole  "))
#      target = int(input("Enter The target Pole  "))
#      honai(n, source, spare, target)

# if __name__ == "__main__":
#      main()



