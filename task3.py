import math
r=5
pi=math.pi
print("volume of sphere")
print(4/3*pi*r**3)

t = total_books = 60
p = price_of_book = 24.95
d = discount_of_book = 40/100*p
c = actual_price_of_book = p-d
s1 = shipping_cost_of_first_book = 3
s = shipping_cost_of_addtional_book = 0.75
T = total_wholesale_cost_for_books = c*60 + s1 + (t-1)*0.75
print("total wholesale cost of books")
print(T)


