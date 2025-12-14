while True:
    a,b=map(int,input().split())
    if a<=0 or b<=0:
        break
    if(a>b):
        # swap a and b sp b become greater
        temp=a
        a=b #(a=b)
        b=temp #(b=a)

    #fntn to calculate sum
    def sum(a,b):
      sum=0
      for j in range(a,b+1):
            sum +=j
      return sum
    
    #loop to print numbers and sum   
    for i in range(a,b+1):
        print(i,end=" ")
    print(f"sum ={sum(a,b)}")


