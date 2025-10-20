goods = input("Введите цену товара: ")
sales = input("Введите скидку товара: ")

goodsInt= int(goods)
salesInt = int(sales)

print("Итоговая цена товара: ", (goodsInt * salesInt)/ 100)

# цена - %
# 15   - 100 %
# x    - 60 %