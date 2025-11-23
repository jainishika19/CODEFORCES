a = float(input())

# convert to int if it has no decimal part
a = int(a) if a.is_integer() else a
if(a>=0 and a<=25):
    print("Interval [0,25]")
elif(a>25 and a<=50):
    print("Interval (25,50]")
elif(a>50 and a<=75):
    print("Interval (50,75]")
elif(a>75 and a<=100):
    print("Interval (75,100]")
else:
    print("Out of Intervals")