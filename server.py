from xmlrpc.server import SimpleXMLRPCServer

# Mock inventory database
inventory = {
    'product1': 10,
    'product2': 20,
    'product3': 0,  # Out of stock
}

def check_inventory(product_id):
    return inventory.get(product_id, 0)

def process_order(product_id, quantity):
    if inventory.get(product_id, 0) >= quantity:
        inventory[product_id] -= quantity
        return True, "Order processed successfully"
    else:
        return False, "Insufficient stock"

server = SimpleXMLRPCServer(('localhost', 8000))
print("Listening on port 8000...")
server.register_function(check_inventory, 'check_inventory')
server.register_function(process_order, 'process_order')

# Run the server's main loop
server.serve_forever()
