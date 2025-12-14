# t=int(input())
# for i in range(t):
#     a,b=map(int,input().split())
#     sum=0
#     for j in range(a,b+1):
#         sum+=j
#     print(sum)

# t=int(input())
# for i in range(t):
#     a,b=map(int,input().split())
#     if(a>b):
#         a,b=b,a
#     sum=((b-a+1)*(a+b))//2
#     print(sum)

def sum_upto(n):
    return n * (n + 1) // 2

T = int(input())
for _ in range(T):
    
    L, R = map(int, input().split())
    if(L>R):
        L,R=R,L

    ans = sum_upto(R) - sum_upto(L - 1)
    print(ans)