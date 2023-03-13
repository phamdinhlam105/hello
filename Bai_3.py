n= eval(input("nhap vao so thang "))
if n>12 | n<=0:
    print("%i khong phai la 1 thang" %n)
else:
    if n==1 |3 | 5 | 7 | 8 | 10 | 12:
        print("so ngay trong thang la 31")
    elif n==2:
        print("so ngay trong thang la 28")
    else:
        print("so ngay trong thang la 30")

