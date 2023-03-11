import math
n=eval(input("Nhap vao so n: "))
if n*10%10!=0:
    print("n khong phai so nguyen")
else:
    print("n la so nguyen")
    if n%2==0:
        if n>=0:
            print("n la so chan duong")
        else:
            print("n la so chan")
    else:
        if n<0:
            print("n la so le am")
        else:
            print("n la so le")
    if n>0:
        if int(math.sqrt(n))**2==n:
            print("n la so chinh phuong")
        else:
         print("n khong phai la so chinh phuong")