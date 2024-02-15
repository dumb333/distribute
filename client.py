import xmlrpc.client

# The client connecting to the RPC server
server = xmlrpc.client.ServerProxy('http://localhost:8000')

def view_product_details(product_id):
    stock = server.check_inventory(product_id)
    print(f"Product ID: {product_id}, Stock available: {stock}")

def add_to_cart(product_id, quantity):
    stock = server.check_inventory(product_id)
    if stock >= quantity:
        print(f"Added {quantity} of product ID {product_id} to cart.")
    else:
        print("Not enough stock to add to cart.")

def place_order(product_id, quantity):
    success, message = server.process_order(product_id, quantity)
    print(message)

# Example Usage:
view_product_details('product1')
add_to_cart('product1', 2)
place_order('product1', 2)
view_product_details('product1')  # Stock should now be reduced by 2
