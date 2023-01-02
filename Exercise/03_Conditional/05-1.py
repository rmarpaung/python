value = int(input("Masukkan nilai yang akan dikonversi: "))
origin = input("Masukkan satuan asal: ")
target = input("Masukkan satuan konversi: ")

if origin == "kilometer":
    if target == "kilometer":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "meter":
        result = value * 1000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "centimeter":
        result = value * 100000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "milimeter":
        result = value * 1000000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
elif origin == "meter":
    if target == "kilometer":
        result = value / 1000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "meter":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "centimeter":
        result = value * 100
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "milimeter":
        result = value * 1000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
elif origin == "centimeter":
    if target == "kilometer":
        result = value / 100000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "meter":
        result = value / 100
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "centimeter":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "milimeter":
        result = value * 10
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
elif origin == "milimeter":
    if target == "kilometer":
        result = value / 1000000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "meter":
        result = value / 1000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "centimeter":
        result = value / 10
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "milimeter":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
else:
    print("Satuan asal tidak diketahui")