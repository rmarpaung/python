value = int(input("Masukkan nilai yang akan dikonversi: "))
origin = input("Masukkan satuan asal: ")
target = input("Masukkan satuan konversi: ")

if origin == "celcius":
    if target == "celcius":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "reamur":
        result = value * 0.8
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "fahrenheit":
        result = value * 1.8 + 32
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "kelvin":
        result = value + 273.15
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
elif origin == "reamur":
    if target == "celcius":
        result = value / 0.8
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "reamur":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "fahrenheit":
        result = value * 2.25 + 32
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "kelvin":
        result = value / 0.8 + 273.15
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
elif origin == "fahrenheit":
    if target == "celcius":
        result = (value - 32)/1.8
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "reamur":
        result = (value - 32) / 2.25
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "fahrenheit":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "kelvin":
        result = (value + 459.67) / 1.8
        print("Hasil konversi %s %s adalah %.3f %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
elif origin == "kelvin":
    if target == "celcius":
        result = value - 273.15
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "reamur":
        result = (value - 273.15) * 0.8
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "fahrenheit":
        result = value * 1.8 - 459.67
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    elif target == "kelvin":
        result = value * 1
        print("Hasil konversi %s %s adalah %s %s" % (value, origin, result, target))
    else:
        print("Satuan konversi tidak diketahui")
else:
    print("Satuan asal tidak diketahui")
