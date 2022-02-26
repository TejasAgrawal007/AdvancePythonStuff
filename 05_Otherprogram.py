# 1. Factorial Of Number

# n = int(input("Enter The Number: "))

# num = 1
# for i in range(1, n+1):
#     num = num * i
# print(f"The Factorial of {n} is ", num)


# 2.  Factorial Using Function

# def factorial(n):
#     num = 1
#     for i in range(1, n+1):
#         num = num * i
#     print(f"The Factorial of {n} is ", num)

# def main():
#     n = int(input("Enter The number: "))
#     factorial(n)


# if __name__ == "__main__":
#     main()


# 3. Prime Number

# def prime(n):
#     if n == 1:
#         return False

#     for i in range(2, n+1):
#         if n%i == 0:
#             return False
#         else:
#             return True

# def main():
#     n = int(input("Enter the prime number: "))
#     result = prime(n)

#     if result == True:
#         print("The Number is Prime")
#     else:
#         print("The Number is not a prime")


# if __name__ == "__main__":
#     main()


# 3. large Among n Digit

# arr = []

# num = int(input("Enter The Number: "))

# for i in range(num):
#     numbers = int(input("Enter The Numbers: "))
#     arr.append(numbers)

# print("The Maximum Number is ", max(arr))
# print("The Minimum Number is ", min(arr))


# 4. Swap The Two Numbers

# a = int(input("Enter The First Number: "))
# b = int(input("Enter The Second Number: "))

# temp = a
# a = b 
# b = temp

# a, b = b ,a 

# Without Using Third Varriable
# a = a + b
# b = a - b
# a = a - b


# print("After Swapping The Numbers are: a = ", a  , "b = ", b)




# Fibonacci Series

# --> 1 + 1 = 2 + 1 = 3 + 2 = 5...

# a = 0
# b = 1
# n = int(input("Enter The Numbers: "))
# print(" ", a , " ", b, end="")
# for i in range(n):
#     c = a + b
#     a = b
#     b = c
#     print(" ", c, end="")
    


                                           


    
