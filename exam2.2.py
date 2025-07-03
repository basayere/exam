grade = int(input("คะแนน (0-100): "))

if grade >= 50:
    if grade >= 60:
        if grade >= 70:
            if grade >= 80:
                print("เกรด A")
            else:
                print("เกรด B")
        else:
            print("เกรด C")
    else:
        print("เกรด D")
else:
    print("เกรด F")