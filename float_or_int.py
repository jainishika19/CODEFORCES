
a=float(input())#a=34.98
if(a.is_integer()):#true if it is integer --here not
    print("int",int(a))
else:
    s=str(a)#now 34.98 treated as string
    integer,decimal=s.split(".") #is spllt as 34 and 98
    print("float",integer,"0."+decimal) #here str "0" + str "decimal"=0.98
    #concatenation of string is done here

