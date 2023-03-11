n=int(input("Nhap vao so can tinh giai thua:"))
temp=1
if(n>=0):
    for i in range(2,n+1):
        temp*=i
    print("Giai thua cua %d la: %d" %(n,temp))
else:
    print("ko tinh duoc giai thua so am")

