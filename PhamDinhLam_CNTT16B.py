
tamgiac=['*']
for i in range(0,4):
    print(tamgiac)
    tamgiac.append('*')
    
Ten=['Nguyen Van A', 'Nguyen Van B', 'Nguyen Van C']
Toan=['7.4','6.5','7.0']
Ly=['6.5','5.0','7.3']
Hoa=['7.0','5.5','6.0']

hoten=input("nhap ten hoc sinh : ")
if Ten.count(hoten)==0:
    print("Ten hoc sinh khong ton tai")
else:
    stt=Ten.index(hoten)
    print("Diem trung binh cua hoc sinh %s:" %hoten)
    print("Toan: %s\tLy: %s\t Hoa: %s"%(Toan[stt],Ly[stt],Hoa[stt]))
Traicay=['Apple','Banana','Cherry','Dragonfruit','Kiwi','Melon','Mango']
Giatien=['20.000','30.000','60.000','40.000','70.000','45.000','50.000']
for i in range(Traicay.index('Cherry'),Traicay.index('Melon')+1):
    print("%s: %s" %(Traicay[i],Giatien[i]))
Traicay.pop()
Traicay.insert(Traicay.index('Kiwi'),'Coconut')
Traicay.insert(Traicay.index('Kiwi'),'Pineapple')