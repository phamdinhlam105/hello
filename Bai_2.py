a = eval(input("Nhap vao so thu nhat: "))
b = eval(input("Nhap vao so thu 2: "))
c = eval(input("Nhap vao so thu 3: "))

max = a
if max<b:
    max=b;
elif max<c:
    max=c
print ("So lon nhat trong 3 so la %i" %(max))