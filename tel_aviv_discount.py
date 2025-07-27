citizen = input("you are Tel Aviv citizen? (Y/N)")
if citizen == "Y" or citizen == "N":
    if (citizen == "Y"):
        age = int(input("please enter your age:"))
        if (age > 65):
            print("you deserve discount")
        else:
            print("you are too young for discount")
    else:
        print("discount Tel aviv citizens only!!")
else:
    print("wrong error!!!!\n only Y/N values")
# if(citizen=="Y"):
#     age = int(input("please enter your age:"))
#     if(age>65):
#         print("you deserve discount")
#     else:
#         print("you are too young for discount")
# else:
#     print("discount Tel aviv citizens only!!")
