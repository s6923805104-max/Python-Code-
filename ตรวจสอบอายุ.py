# ข้อ 3 ตรวจสอบอายุ
age = int(input("รับค่าอายุ: "))

if age >= 10:
    print("3 ช้อนชา")
elif age >= 6:
    print("2 ช้อนชา")
elif age >= 2:
    print("1 ช้อนชา")
else:
    print("ห้ามรับประทาน")
