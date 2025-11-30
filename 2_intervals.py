# a,b,c,d=(map(int,input().split()))
# print(f"{c} {b}" if(c>=a and c<=b) else "-1")
l1, r1, l2, r2 = map(int, input().split())
if max(l1, l2) <= min(r1, r2):
     print(max(l1, l2), min(r1, r2))
else:
     print(-1)