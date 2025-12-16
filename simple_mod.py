n=int(input())
for i,j in range(n+1):
    if (i**2+j**2)%n==0:
        print(i,j)

        # how to iterate 2 numbers