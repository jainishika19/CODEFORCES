a=input()
ascii=ord(a)
if(ascii>=97 and ascii<122):
    char=chr(ascii+1)

    print(char)
elif(ascii==122):
    print(chr(97))
