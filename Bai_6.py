import math
print("Bien luan phuong trinh bac 2: ax2+bx+c=0")
a= eval(input("Nhap vao so a: "))
b= eval(input("Nhap vao so b: "))
c= eval(input("Nhap vao so c: "))
if a==0:
    if b==0:
        if c==0:
            print("phuong trinh vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        print("phuong trinh co 1 nghiem: %.2f" %(float(-c/b)))
else:
    delta = b*b-4*a*c
    if delta<0:
        print("phuong trinh vo nghiem")
    elif delta==0:
        print("phuong trinh co nghiem kep: %.2f" %(float(-b/(2*a))))
    else:
        print("phuong trinh co 2 nghiem la : %.2f va %.2f" %(float((-b+math.sqrt(delta))/(2*a)), float((-b-math.sqrt(delta))/(2*a))))
