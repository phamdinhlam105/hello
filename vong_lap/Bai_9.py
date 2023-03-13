n=int(input("Nhap vao so n: "))
print("{",end='')
for i in range(1,n):
    print("%d:%d, " %(i,i*i), end='')
print("%d:%d}" %(n,n*n))