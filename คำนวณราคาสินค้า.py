product = input("เลือกสินค้าปลายทาง: ")
price = float(input("ราคาสินค้า: "))
quantity = int(input("จำนวนสินค้า: "))

total = price * quantity

print("สินค้า =", product)
print("ยอดเงิน =", total)

while True:
    money = float(input("รับเงิน: "))

    if money >= total:
        change = money - total
        print("จ่ายบัตรโดยสาร")
        print("เงินทอน =", change)
        print("จบ")
        break
    else:
        print("จำนวนเงินไม่เพียงพอ กรุณารับเงินใหม่")
