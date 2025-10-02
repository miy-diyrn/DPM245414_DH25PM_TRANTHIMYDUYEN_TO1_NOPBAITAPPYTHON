import math

def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi",
                 "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    if n < 10:
        return don_vi[n]
    else:
        chuc = n // 10
        dv = n % 10
        if dv == 0:
            return hang_chuc[chuc]
        else:
            return hang_chuc[chuc] + " " + don_vi[dv]
print("Câu 6:")
print("n=35:", doc_so(35))
print("n=5:", doc_so(5))
print("n=40:", doc_so(40))
