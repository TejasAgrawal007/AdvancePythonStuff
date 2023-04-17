# 1. Makrs
# def moderate(marks, passMakrs):
#     if marks == passMakrs - 1 or marks == passMakrs -2 :
#         marks = passMakrs

# def main():
#     passMarks = 40
#     marks = input("Enter Makrs: ")
#     intMarks = int(marks)
#     moderateMarks = moderate(intMarks, passMarks)
#     print("Moderated marks: ", moderateMarks)

# if __name__ == "__main__":
#     main()


# 2. authenticateUser System Program

# def authenticateUser(password):
#     if password == "Tejas":
#         message = 'Login Successful !!\n Wolcome To System.'
#     if password != "Tejas":
#         message = "Password mismatch !! \n"
#     return message


# def main():
#     print("\n LOGIN SYSTEM")
#     print("====================")
#     password =  input("Enter Password\t")
#     message = authenticateUser(password)
#     print(message)

# if __name__ == "__main__":
#     main()


# assignGrade Program.

# Note  --> Assert statement used to debug code and handle  the Condition Code.

# def assignGrade(marks):
#     assert marks >= 0 and marks <= 100
#     if marks >= 90:
#         grade = "A"

#     elif marks >= 70:
#         grade =  "B"

#     elif marks >= 50:
#         grade =  "C"

#     elif marks >= 40:
#         grade =  "D"
#     else:
#         grade = "F"
#     return grade


# def main():
#     marks = float(input("Enter You marks: "))
#     print("Marks: ", marks, "\nGrade: ", assignGrade(marks))


# if __name__ == "__main__":
#     main()

# program to find the Maximum Three Numbers

# from numpy import maximum


# def maximum3(n1,n2,n3):
#     if n1 > n2:
#         if n1 > n3:
#             maxNumber = n1
#         else:
#             maxNumber = n3
#     elif n2 > n3:
#         maxNumber = n2
#     else:
#         maxNumber = n3
#     return maxNumber


# def main():
#     n1 = int(input("Enter First Number: "))
#     n2 = int(input("Enter Secound Number: "))
#     n3 = int(input("Enter Third Number: "))
#     maximum = maximum3(n1, n2, n3)
#     print("Maximum Number is: ", maximum)


# if __name__ == "__main__":
#     main()


# Program To Find Some Of First N Positive Number.

# def summation(n):
#     total = 0
#     for count in range(1, n + 1):
#         total += count
#     return total


# def main():
#     n = int(input("Enter The Number of Turms: "))
#     total = summation(n)
#     print("Sum of First", n , "Positive Integer: ", total)


# if __name__ == "__main__":
#     main()


# Program to Compute a Percentage

# def main():
#     n = int(input("Enter The Total Subject: "))
#     totalMarks = 0
#     print("Enter The Marks: ")
#     for i in range(1, n + 1):
#         marks = float(input("Subject " + str(i) + " : "))
#         assert marks >= 0 and marks <= 100
#         totalMarks += marks
#     percentag = totalMarks / n
#     print("Your Percentage is ", percentag)


# if __name__ == "__main__":
#     main()


# Loop for printing a Multiplactin table.


# from numpy import product


# num = int(input("Enter The Number: "))
# for i in range(1, 11):
#     product = num * i
#     print(f"The Number is {i} X {num} = {i*num}")

# def printTable(num, i = 10):
#         for i in range(1, 11):
#             product = num * i
#             print(f"The Number is {i} X {num} = {i*num}")


# def main():
#     num = int(input("Enter The Number: "))
#     printTable(num)

# if __name__ == "__main__":
#     main()


# program to Compute Sum of Numbers


# from numpy import number


# def main():
#     total  = 0
#     number = input("Enter a Number: ")
#     while number != "":
#         total += int(number)
#         number = input("Enter a Number: ")
#     print("Sum of the Number is = ", total)


# if __name__ == "__main__":
#     main()


# Program to Chech the Number is Prime or Not

# from unittest import result


# def prime(n):
#     if n == 1:
#         return False

#     for i in range(2, n):
#         if(n%i == 0):
#             return False
#         else:
#             return True


# def main():
#     n = int(input("Enter The Number: "))
#     result = prime(n)
#     if result ==  True:
#         print("the Number is Prime")
#     else:
#         print("The Number is not Prime")


# if __name__ == "__main__":
#     main()


# Write a Program To Print The RightAngleTriangele

# def rightAngleTriangele(n):
#     for i in range(1, n+1):
#         print(" * " * i)

# def main():
#     n = int(input("Enter The Number: "))
#     rightAngleTriangele(n)

# if __name__ == "__main__":
#     main()

# Inverted triangle

# def InvertedTriangle(n):
#     spaces = 0
#     star = 2 * n - 1
#     for i in range(1, n + 1):
#         print(" " * spaces, "*" * star)
#         spaces += 1
#         star -= 2

# def main():
#     n = int(input("Enter The Number of Rows: "))
#     InvertedTriangle(n)


# if __name__ == "__main__":
#     main()



# Compute Selling price

# def discount(price):
#     pass


# def selling(price):
#     dicountPrice = discount(price)
#     if dicountPrice == None:
#         return price
#     else:
#         return dicountPrice

# def main():
#     price = float(input("Enter The Number: "))
#     print("The Selling price is ", selling(price))
    


# if __name__ == "__main__":
#     main()
