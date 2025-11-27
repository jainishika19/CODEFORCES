# a=input()
# ascii=ord(a) #ord finds ascii values
# if(ascii>=65 and ascii<=90):
#     print("ALPHA")
#     print("IS CAPITAL")
# elif(ascii>=97 and ascii<=122):
#     print("ALPHA")
#     print("IS SMALL")
# elif(ascii>=48 and ascii<=57):
#     print("IS DIGIT")



# by direct short(2nd mehtod)
a=input()
ascii=ord(a) #ord finds ascii values
if(ascii>=48 and ascii<=57):
    print("IS DIGIT")
else:
    print("ALPHA")
    if(ascii>=65 and ascii<=90):
        print("IS CAPITAL")
    else:
        print("IS SMALL")
        
# # 3rd method()
# x = input().strip()#here strip() fntn --if we enter input by giving some spaces
# like "   a   " then it automatic take as "a" ,by this no error come 
# if x.isdigit():
#     print("IS DIGIT")
# else:
#     print("ALPHA")
#     if x.isupper():
#         print("IS CAPITAL")
#     else:
#         print("IS SMALL")