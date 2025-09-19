class Customer:
    def _init_(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
