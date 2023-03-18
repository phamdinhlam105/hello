def inchuoi(so):
    if so<10:
        print(so,end='')
    else:
        inchuoi(int(so/10))
        temp=so%10
        print(",%d"%temp,end='')
        
        
chuoi= ''
n=int(input("Nhap vao so can tinh giai thua:"))
temp=1
if(n>=0):
    for i in range(2,n+1):
        temp*=i
    inchuoi(temp)
else:
    print("ko tinh duoc giai thua so am")

