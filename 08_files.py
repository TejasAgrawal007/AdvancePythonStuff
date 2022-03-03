'''
 Note: “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream.

 The dump() method of the pickle module in Python, converts a Python object hierarchy into a byte stream. This process is also called as serilaization.

 The converted byte stream can be written to a buffer or to a disk file.

The byte stream of 8a pickled Python object can converted back to a Python object using the pickle.load() method.
'''


# 1. program to read and write a structure to the file.

# import pickle
# def main():

#     f = open('files/file1', 'wb')
#     pickle.dump(['hello', 'world'],f)
#     pickle.dump({1:'one', 2:'two'},f)

#     f = open('files/file1', 'rb')
#     value1 = pickle.load(f)
#     value2 = pickle.load(f)

#     print(value1, value2)
#     f.close()

# if __name__ == '__main__':
#     main()


# program to open a Non-existent File.

# def main():
#     try:
#         f = open("files/siya.txt", "r")
#     # except IOError:
#     except Exception as e:
#         print("Problem With I/O Files...")
#     print("Program continue smoothly beuyond try...except Block")

# if __name__ == "__main__":
#     main()

# import sys

# from black import err
# def main():
#     try:
#         f = open("files/siya.txt", "r")
#     # except IOError:
#     except Exception as e:
#         print("Problem With I/O Files...\n", err)
#         print(sys.exc_info())
#     print("Program continue smoothly beuyond try...except Block")

# if __name__ == "__main__":
#     main()




# Program to Compute Price per unit weight of an Item.

# import sys
# def main():
#     price = input("Enter The Price of item Perched: ")
#     weight = input("Enter The Weight of items Perchased: ")
#     try:
#         if price  == "" : price = None
#         price = float(price)
        
#         if weight == "": price = None
#         weight = float(weight)

#         assert price >=0 and weight >= 0
#         result = price / weight

#     except(ValueError, TypeError, ZeroDivisionError):
#         print("INvalid Error Provided by User\n" + str(sys.exc_info()))

#     else:
#         print("Price per Unit Weight: ", result)


# if __name__ == "__main__":
#     main()


# To Illustrate a Final Keyword.

# def main():

#     marks = 110
#     try:
#         if marks < 0 or marks > 100:
#             raise valueError("Marks Out Of range.")
#     except:
#         pass

#     finally:
#         print("Bye")
#     print("program Continue After Handling Exception. ")

# if __name__ == "__main__":
#     main()


# Program to proudcing Marks

import sys
def main():
    try:
        f1 = open('files/studentmarks.txt', 'r')
        f2 = open('files/studentmarks.txt', 'w')
    except:
        pass


if __name__ == "__main__":
    main()
        