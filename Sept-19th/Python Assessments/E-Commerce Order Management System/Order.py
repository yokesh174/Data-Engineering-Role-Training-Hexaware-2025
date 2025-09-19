class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items  # list of (Product, qty)

    def get_total(self):
        return sum(prod.price * qty for prod, qty in self.items)
