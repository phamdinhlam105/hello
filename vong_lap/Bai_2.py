n = int(input("Nhap vao vi tru phan tu trong day so 50, 51, 53, 56, 60: "))
s=50
for i in range(0,n):
   s += (i+1)
print("phan tu thu %d la : %d" %(n, s))
