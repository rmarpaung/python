grade = int(input("Masukkan nilai: "))

if grade >= 86 and grade <= 100:
    print("Nilai A")
elif grade >= 76 and grade <= 85:
    print("Nilai B")
elif grade >= 66 and grade <= 75:
    print("Nilai C")
elif grade >= 56 and grade <= 65:
    print("Nilai D")
elif grade >= 0 and grade <= 55:
    print("Nilai E")
else:
    print("Nilai tidak diketahui")