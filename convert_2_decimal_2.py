t=int(input())
for i in range(t):
    n=int(input())
    binary=bin(n)[2:]
    #bin(n) returns string like--0b10 but we dont want 0b
    # so we use[:2] means string start from 2nd index
    # 0  1  2  3  
#    '0''b''1''0'
    b=str((binary))
    print(b)
    dec=""
    for i in b:
        if '1' in b:
            # dec.append("1")
            dec=dec+"1"
n=int(dec)
print(n)



            

    
