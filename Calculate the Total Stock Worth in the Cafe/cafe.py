"""
Calculate the Total Stock Worth in the cafe
"""

# Store menu items sold in the cafe. 
menu = ["Tea", "Cappuccino", "Latte", "Americano", "Mocha", "Flat White", 
        "Hot Chocolate", "Croissant" ]
# Store the stock values for each item on the "menu" list.
stock = {"Tea" : 100, "Cappuccino" : 80 , "Latte" : 90, "Americano": 70, 
         "Mocha" : 60, "Flat White" : 50, "Hot Chocolate" : 40, 
         "Croissant" : 30}
# Store the prices for each item on the "menu" list.
price = {"Tea" : 2.00, "Cappuccino" : 2.75 , "Latte" : 2.70, "Americano": 2.40,
         "Mocha" : 2.90, "Flat White" : 2.80, "Hot Chocolate" : 2.95, 
         "Croissant" : 1.75}

def total_stock():
    """
    Function to calculate the total stock worth of the 
    available stock in the cafe.
    """
    total_stock_worth = 0
    for item in menu:
        # To get the stock quantity for the item.  
        stock_quantity = stock.get(item, 0) #Default to 0 if not found.  
        # To get the price for the item.
        items_price = price.get(item, 0) # Defaulting to 0 if not found. 
        # Calculating total stock worth.
        total_stock_worth += stock_quantity * items_price
    return total_stock_worth
    
# Calling the function "total_stock" to calculate the total stock worth.
total_stock_worth_in_cafe = total_stock()
# Output the results using f-strings 
print(f"Total stock worth in the cafe: {total_stock_worth_in_cafe} pounds")  