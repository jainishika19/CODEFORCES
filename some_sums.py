n,a,b=map(int,input().split())
s=[]
for i in range(1,n+1):
        list=str(i)
        total=sum(int(ch) for ch in list)
        # fd=i//10
        # sum=ld+fd #not by this bcs if we take no. of more than 2 digit
        # then this not works as there are not 2 digits and we calculate only 2 digits
        if a<=total<=b:
            s.append(i)
# print(s)
sum=0
for j in s:
      sum+=j
print(sum)
      