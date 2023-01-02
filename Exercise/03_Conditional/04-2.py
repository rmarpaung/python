grade = int(input("Masukkan nilai: "))

if grade > 100:
    print("Nilai terlalu tinggi")
elif grade >= 86:
    print("Nilai A")
elif grade >= 76:
    print("Nilai B")
elif grade >= 66:
    print("Nilai C")
elif grade >= 56:
    print("Nilai D")
elif grade >= 0:
    print("Nilai E")
else:
    print("Nilai terlalu rendah")
