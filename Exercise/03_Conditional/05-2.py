value = int(input("Masukkan nilai yang akan dikonversi: "))
origin = input("Masukkan satuan asal: ")
target = input("Masukkan satuan konversi: ")
result = 0.0

if origin == "kilometer":
    if target == "kilometer":
        result = value * 1
    elif target == "meter":
        result = value * 1000
    elif target == "centimeter":
        result = value * 100000
    elif target == "milimeter":
        result = value * 1000000
    else:
        print("Satuan konversi tidak diketahui")
        quit()
elif origin == "meter":
    if target == "kilometer":
        result = value / 1000
    elif target == "meter":
        result = value * 1
    elif target == "centimeter":
        result = value * 100
    elif target == "milimeter":
        result = value * 1000
    else:
        print("Satuan konversi tidak diketahui")
        quit()
elif origin == "centimeter":
    if target == "kilometer":
        result = value / 100000
    elif target == "meter":
        result = value / 100
    elif target == "centimeter":
        result = value * 1
    elif target == "milimeter":
        result = value * 10
    else:
        print("Satuan konversi tidak diketahui")
        quit()
elif origin == "milimeter":
    if target == "kilometer":
        result = value / 1000000
    elif target == "meter":
        result = value / 1000
    elif target == "centimeter":
        result = value / 10
    elif target == "milimeter":
        result = value * 1
    else:
        print("Satuan konversi tidak diketahui")
        exit()
else:
    print("Satuan asal tidak diketahui")
    exit()

    print("Hasil konversi %s %s adalah %s %s" %
          (value, origin, result, target))
