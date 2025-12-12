n=int(input())
prime=[]
for i in range(2,n+1):
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            is_prime=False
            break
    if is_prime:
        prime.append(str(i)) #['2','3','5','7']
# print(prime)
# print(' '.join(prime))#it remove string type and simple convert it into numbers
print(*prime) # only elements print one by one