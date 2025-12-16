n=int(input())
for i in range(1,n+1):
    spaces=n-i
    print(spaces*" "+(2*i-1)*"*")
    
for j in range(n,0,-1):#from j=4 to 1 (-1 is interval)
    spaces=n-j
    print(spaces*" "+(2*j-1)*"*")
    
    