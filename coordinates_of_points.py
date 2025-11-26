a, b = map(float, input().split())

# convert to int if it has no decimal part
a = int(a) if a.is_integer() else a
b = int(b) if b.is_integer() else b

if(a==0 and b==0):
    print("Origem")
elif(a>0 and b>0):
    print("Q1")
elif(a<0 and b>0):
    print("Q2")
elif(a<0 and b<0):
    print("Q3")
elif(a>0 and b<0):
    print("Q4")
elif(b==0):
    print("Eixo X")
elif(a==0):
    print("Eixo Y")



