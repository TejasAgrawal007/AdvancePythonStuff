# Example Class Person


# from itertools import count


# class Person:
#     def __init__(self, name, DOB, address):
#         self.name = name
#         self.DOB = DOB
#         self.address = address
#         # Person.count += 1

#     def getName(self):
#         print(f"The name of The person is {self.name}")
 
#     def getDob(self):
#         print(f"The name of The person is {self.DOB}")

#     def getAddress(self):
#         print(f"The name of The person is {self.address}")



# p1 = Person("Siya", "03-12-2001", "Nagpur")
# p1.getName()
# p1.getDob()
# p1.getAddress()



# Unka Vala Person Code...


# from email.headerregistry import Address


# class Person():
#     count = 0
#     def __init__(self,name, DOB, address):
#         self.name = name
#         self.DOB = DOB
#         self.address = address
#         Person.count += 1

# # Func for Printing the Value
#     def getName(self):
#         return self.name

#     def getDOB(self):
#         return self.DOB

#     def getAddress(self):
#         return self.address

# # Func for Updating the Value

#     def setName(self, name):
#         self.name = name

#     def setDOB(self,DOB):
#         return self.DOB

#     def setAddress(self, address):
#         return self.address


#     def getCount(self):
#         print("Person Count!!!")
#         return Person.count

    
#     def __str__(self):
#         # return 'Name:' + self.name + '\nDOB is' + str(self.DOB) + '\nAddress is ' + self.address
#         return f"The Name is {self.name} and his DOB is {self.DOB} as his address is {self.address}"

#     # Disctrutor in Python
#     def __del__(self):
#         print("Deleted !!!")
#         Person.count -= 1



# p1 = Person('Siya', '03-12-2001', 'Nagpur')
# p2 = Person('Tejas', '04-06-2001', 'Nagpur')
# print(p1)
# print(p2)



# Class Date (**Incomplate**)

# from collections import defaultdict
# from email.policy import default
# import sys
# from turtle import st
# class MyDate:
    
#     def __init__(self,day = 1, month = 1, year = 2001):

#         if not(type(day) == int and type(month) == int and type(year) == int):
#             print("Invalid Data provided for date")
#             sys.exit()
        
#         if month > 0 and month <= 12:
#             self.month = month
#         else:
#             print("Invalid Vale for The Month. ")
#             sys.exit()

        
#         if year > 1900:
#             self.year = year
#         else:
#             print("Invalid value for the year. Year Should Be Greater than 1900. ")
#             sys.exit()
#         self.day = self.checkDay(day) # valid Date


#     def __str__(self):
#         if self.day <= 9:
#             day = '0' + str(self.day)
#         else:
#             day = str(self.day)

#             if self.month <= 9:
#                 month = '0' + str(self.month)
#             else:
#                 month = str(self.month)
#             return day + ' - '+ month +  ' - ' + str(self.year)

# def main():
#     today = MyDate(4,6,2001)
#     print(today)
#     defaultdate = MyDate()
#     print(defaultdate)


# if __name__ == '__main__':
#     main()


