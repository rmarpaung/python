value = int(input("Masukkan nilai yang akan dikonversi: "))
origin = input("Masukkan satuan asal: ")
target = input("Masukkan satuan konversi: ")

if origin == "celcius":
    if target == "celcius":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "reamur":
        result = value * 1000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "fahrenheit":
        result = value * 100000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "kelvin":
        result = value * 1000000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
elif origin == "reamur":
    if target == "celcius":
        result = value / 1000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "reamur":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "fahrenheit":
        result = value * 100
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "kelvin":
        result = value * 1000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
elif origin == "fahrenheit":
    if target == "celcius":
        result = value / 100000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "reamur":
        result = value / 100
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "fahrenheit":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "kelvin":
        result = value * 10
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
elif origin == "kelvin":
    if target == "celcius":
        result = value / 1000000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "reamur":
        result = value / 1000
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "fahrenheit":
        result = value / 10
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "kelvin":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
else:
    print("Satuan asal tidak diketahui")