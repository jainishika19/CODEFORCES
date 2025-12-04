n,k=map(int,input().split())
arr=list(map(int,input().split()))
ans=[]
for i in range(0,n,k):
     group=arr[i:i+k]
     ans.append(min(group))
print(*ans)