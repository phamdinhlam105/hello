print("Cac so chia het cho 7 nhung khong chia het cho 5 trong doan 2000 va 3200: ")
for i in range(2000,3201):
    if (i%7==0) & (i%5!=0):
        print( "%d, "%i ,end='')
