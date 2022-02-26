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


 