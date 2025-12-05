# password=int(input())
# if(password==1999):
#         print("Correct")
#         break
# else:
#     print("Wrong")

while True:#here we use infinite loop bcs the i/p contains many
    # lines,we dont know how many passwords will be enteres
    x=int(input())
    if x==1999:
        print("Correct")
        break #when we find correct pass.we terminate the program
    else:
        print("Wrong")