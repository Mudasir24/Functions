# Defining a function to calculate the dicounted price if discount is 10%
def calculate_discount(original_price, discount_percentage):
    discount_amount = (discount_percentage / 100) * original_price
    discounted_price = original_price - discount_amount
    return discounted_price

# Defining original price and dicount percentage
original_price = 1000
discount_percentage = 10
final_price = int(calculate_discount(original_price, discount_percentage))

# printing the  final price after discount
print("The price after discount of 10 percent is Rs.",final_price)