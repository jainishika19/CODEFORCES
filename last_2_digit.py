a,b,c,d=map(int,input().split())
result=a*b*c*d
last_2_digit=result%100
print(f"{last_2_digit:02d}")
# why 02d----
# if the last 2 digit is 05 then %100 gives 5 ,but we must print 05
# so 02d adds leading zero 
# if the no is 4000 and last 2 digit is 00 here then %100 gives 0 only 
# but we must print 00 so 02d print 00
