def sort(list):
    temp=0
    for i in range(0,len(list)):
        for j in range(i,len(list)):
            if list[i]>list[j]:
               temp=list[i]
               list[i]=list[j]
               list[j]=temp 

n = int(input("nhap vao so phan tu cua list: "))
list1 =[]
for i in range(0,n):
    list1.append(int(input("Nhap vao phan tu thu %d: " %(i+1))))
sort(list1)
print("list sau khi sap xep:")
print(list1)