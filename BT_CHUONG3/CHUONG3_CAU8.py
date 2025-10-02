import math

def tinh_toan(a, b, pheptoan):
    if pheptoan == "+":
        return a + b
    elif pheptoan == "-":
        return a - b
    elif pheptoan == "*":
        return a * b
    elif pheptoan == "/":
        if b != 0:
            return a / b
        else:
            return "Lỗi: chia cho 0"
    else:
        return "Phép toán không hợp lệ"

print("\nCâu 8:")
print("5 + 3 =", tinh_toan(5,3,"+"))
print("10 - 2 =", tinh_toan(10,2,"-"))
print("4 * 6 =", tinh_toan(4,6,"*"))
print("8 / 2 =", tinh_toan(8,2,"/"))