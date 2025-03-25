drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice"]
prices = [2000, 3000, 4900]
amounts = [0] * len(drinks)
total_price = 0

# drinks = ["Ice Americano", "Cafe Latte"]
# prices = [2000, 3000]
# amounts = [0, 0]
# total_price = 0

DISCOUNT_THRESHOLD = 10000
DISCOUNT_RATE = 0.1

def apply_discount(price: int):

#if문이 필요함
    if price >= DISCOUNT_THRESHOLD:
        discount=price*DISCOUNT_RATE
        return price-discount
    return price

def order_process(idx: int):
    """
    Functions that address the beverage order display function, the total cumulative amount calculation function, and the beverage order quantity processing function
    :param idx: list's index number
    """
    global total_price
    print(f"{drinks[idx]} ordered. Price : {prices[idx]}won")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1


menu_lists = "".join([f"{k+1}) {drinks[k]} {prices[k]}won  " for k in range(len(drinks))])
menu_lists = menu_lists + f"{len(drinks)+1}) Exit : "

while True:


print("Product  Price  Amount  Subtotal")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]}")


discount_price=apply_discount(total_price)
discount_amount=original_price-discount_price #할인받은금액이 나옴
print(f"Original total price : {total_price}won") #원래 가격 출력
if discount_amount>0: #할인을 받았다면면
    print(f"Discount_amount : {discount_amount}") #얼마 할인 받았는지 출력
    print(f"Total price after discount: {discount_mount}won") #얼마 할인 받았는지 출력
else:
    print("The discount has not been applied.") 
    print(f"Total price after discount: {total_price}won") 

print(f"Total price : {total_price}")