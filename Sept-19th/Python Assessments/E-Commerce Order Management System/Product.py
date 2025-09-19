class Product:
    def _init_(self, pid, name, category, price, stock):
        self.id = int(pid)
        self.name = name
        self.category = category
        self.price = float(price)
        self.stock = int(stock)

    def update_stock(self, qty):
        if qty <= self.stock:
            self.stock -= qty
        else:
            print(f"Not enough stock for {self.name}")
