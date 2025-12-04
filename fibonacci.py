n=int(input())
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
#    ''' for n=1  a =0 (a,b=0,1)
       
#        for n=2  a =b=1 
#        and b=(a+b)=0+1=1
        
#     '''


