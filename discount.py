user=int(input("quantity of goods bought"))
unit_cost=100* user
discount = (unit_cost) * 10 // 100
total = unit_cost - discount
print(unit_cost)
if unit_cost>1000:
    print("you have qualified for a dicount")
    print(total)
    print(discount)

else:
    print("spend >1000 to get discount")

