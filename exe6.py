#Price Per Square inch is calculated by dividing the price (P) of the pizza by its area
def price(v1,v2):
    #Aria=v1*v1*3.14
    #price_per_squar=v2*Aria
    return v1*v1*3.14*v2






diameter=float(input("THE DIAMETER OF FIRST PIZZA:",))
pizza_price=float(input("THE PRICE OF PIZZA:",))
pizza1 = price(diameter, pizza_price)
print("-------------------------------------------------")
diameter = float(input("THE DIAMETER OF SECOND PIZZA:", ))
pizza_price = float(input("THE PRICE OF PIZZA:", ))
pizza2=price(diameter,pizza_price)
print("-------------------------------------------------")
if pizza1<pizza2:
    print("Pizza 1 has low price")
elif pizza1>pizza2:
    print("Pizaa 2 has low price")
else:
    print("both of them are same")