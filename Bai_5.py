print("Bien luan phuong trinh bac nhat : ax+b=0")
a= float(input("Nhap vao so a: "))
b= float(input("Nhap vao so b: "))
if a==0:
    if b==0:
        print("phuong trinh vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
else:
    print("phuong trinh co 1 nghiem la %.2f"%(float(-b/a)))