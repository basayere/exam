total = 0

n = int(input("กรอกตัวเลข (0 เพื่อหยุด): "))

while n != 0:
    total += n
    n = int(input("กรอกตัวเลข (0 เพื่อหยุด): "))

print("ผลรวม:", total)