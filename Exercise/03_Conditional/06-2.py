value = int(input("Masukkan nilai yang akan dikonversi: "))
origin = input("Masukkan satuan asal: ")
target = input("Masukkan satuan konversi: ")

if origin == "celcius":
    if target == "celcius":
        result = value * 1
    elif target == "reamur":
        result = value * 0.8
    elif target == "fahrenheit":
        result = value * 1.8 + 32
    elif target == "kelvin":
        result = value + 273.15
    else:
        print("Satuan konversi tidak diketahui")
        quit()
elif origin == "reamur":
    if target == "celcius":
        result = value / 0.8
    elif target == "reamur":
        result = value * 1
    elif target == "fahrenheit":
        result = value * 2.25 + 32
    elif target == "kelvin":
        result = value / 0.8 + 273.15
    else:
        print("Satuan konversi tidak diketahui")
        quit()
elif origin == "fahrenheit":
    if target == "celcius":
        result = (value - 32)/1.8
    elif target == "reamur":
        result = (value - 32) / 2.25
    elif target == "fahrenheit":
        result = value * 1
    elif target == "kelvin":
        result = (value + 459.67) / 1.8
    else:
        print("Satuan konversi tidak diketahui")
        quit()
elif origin == "kelvin":
    if target == "celcius":
        result = value - 273.15
    elif target == "reamur":
        result = (value - 273.15) * 0.8
    elif target == "fahrenheit":
        result = value * 1.8 - 459.67
    elif target == "kelvin":
        result = value * 1
    else:
        print("Satuan konversi tidak diketahui")
        quit()
else:
    print("Satuan asal tidak diketahui")
    exit()

print("Hasil konversi %s%s %s adalah %s%s %s" % (value, '\u00B0', origin, result, '\u00B0', target))