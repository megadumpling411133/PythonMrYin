Quantity = 13
ItemNumber = 15
Price = 13.99
TotalPrice = Price * Quantity
Br = "\n"
Template = "訂購了 產品編號 {} 價格 {} 數量 {} 總金額 {}"

print("Template: " + Template)
FormatStr = Template.format( ItemNumber, Price, Quantity, TotalPrice)

print("FormatStr: " + FormatStr)
FStr = f"OrderList ItemNumber: {ItemNumber} Price: {Price} Quantity: {Quantity} TotalPrice: {TotalPrice:.3f}"
#FStr = f("OrderList" + Br + "ItemNumber: {ItemNumber} Price: {Price} Quantity: {Quantity} TotalPrice: {TotalPrice:.3f}")
print("f-String: " + FStr)

