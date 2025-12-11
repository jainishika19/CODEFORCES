n=int(input())
original=n #1st we have tp store n in original because
# after loop n become zero 
reverse=0
while n!=0:
    last_digit=n%10
    reverse=reverse*10+last_digit
    n=n//10

print(reverse)
if(reverse==original):
    print("YES")
else:
    print("NO")

