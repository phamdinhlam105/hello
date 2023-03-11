n=int(input("Nhap vao so tuoi cua 1 nguoi: "))
if n<0:
    print("so tuoi khong hop le")
else:
    if n<=2:
        print("nguoi nay la tre so sinh")
    elif n<=10:
        print("nguoi nay la nhi dong")
    elif n<=17:
        print("nguoi nay la vi thanh nien")
    elif n<=39:
        print("nguoi nay la thanh nien")
    elif n<=50:
        print("nguoi nay la trung nien")
    else:
        print("nguoi nay la cao nien")