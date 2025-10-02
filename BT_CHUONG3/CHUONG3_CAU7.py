import datetime

def ngay_ke_tiep(ngay, thang, nam):
    d = datetime.date(nam, thang, ngay)
    tomorrow = d + datetime.timedelta(days=1)
    return tomorrow.strftime("%d/%m/%Y")

print("\nCâu 7:")
print("Sau ngày 28/2/2024:", ngay_ke_tiep(28,2,2024))  # năm nhuận
print("Sau ngày 31/12/2023:", ngay_ke_tiep(31,12,2023))