# 1. Marks
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
#     if password == "siya":
#         message = 'Login Successful !!\n Wolcome To System.'
#     if password != "siya":
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
#     n = int(input("Enter The Number of Terms: "))
#     total = summation(n)
#     print("Sum of First", n , "Positive Integer: ", total)


# if __name__ == "__main__":
#     main()





# Program to Compute  Percentage

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
