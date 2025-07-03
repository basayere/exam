temperature = int(input("อุณหภูมิ (หน่วย °C): "))

if temperature >= 0:
    if temperature >= 16:
        if temperature >= 31:
            if temperature >= 39:
                print("ร้อนมาก")
            else:
                print("ร้อน")
        else:
            print("ปกติ")
    else:
        print("หนาว")
else:
    print("หนาวจัด")