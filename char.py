a=input()
ascii=ord(a)

if(ascii>=65 and ascii<=90):
    print(chr(ascii+32))
elif(ascii>=97 and ascii<=122):
    print(chr(ascii-32))

# uppercase asciii range= 65 to 90
# lowercase asciii range= 97 to 122
# to convert from upppercase to lower ->ascii+32
# to convert from lowercase to upper ->ascii-32

