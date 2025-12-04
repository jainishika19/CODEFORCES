n=int(input())
v=map(int,input().split())
even=0
odd=0
positive=0
negative=0
for i in v:
    if(i%2==0):
        even+=1
    if(i%2!=0):
        odd+=1
    if(i>0):
        positive+=1
    if(i<0):
        negative+=1
print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)