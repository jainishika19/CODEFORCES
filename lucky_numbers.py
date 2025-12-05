a,b=map(int,input().split())
lucky_num=[]
for num in range(a,b+1):
    s=str(num)
    if all(ch in '47' for ch in s):
        lucky_num.append(num)
if(len(lucky_num)==0):
    print(-1)
else:
    # for num in lucky_num:
    #     print(num,end=" ") #also by this
    print(*lucky_num) #by asterik lucky_num-it prints 
    # #only elements not list
