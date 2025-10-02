import math
try
print("chuong trinh dem so ngay trong thang")
month=int(input("nhap vao 1 thang:"))
if month in(1,3,5,7,8,10,12):
    print("thang",month,"co 31ngay")
elif month in(4,6,9,11):
    print("thang",month"co 30 ngay")
elif month=2:
    year=int(input("moi ban nhap vao nam: "))
    id(year%4==0 and year%100!=0)or year%400==0:
    print("thang",month,"co 29 ngay")
    else:
    print("thang",month,"co 28 ngay")
else:
print("thang",month,"khong hop le")