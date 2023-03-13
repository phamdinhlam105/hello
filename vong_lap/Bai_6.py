n=int(input("nhap vao so n: "))
flag=1
if n<2:
    flag=0
else:
    for i in range(2,n):
        if n%i ==0:
            flag=0
            break
if flag==0:
    print("%d ko phai la so nguyen to" %n)
else:
    print("%d la so nguyen to" %n)