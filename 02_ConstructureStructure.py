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

# Note  --> Assert statement used to debug code and handle the Code.

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