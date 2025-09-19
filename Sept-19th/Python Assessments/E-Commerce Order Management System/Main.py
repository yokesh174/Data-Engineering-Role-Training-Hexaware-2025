from utils import load_products, save_products, load_orders, save_orders, sales_report, inventory_report


def main():
    products = load_products()
    orders = load_orders()

    while True:
        print("\n===== E-Commerce Management Menu =====")
        print("1. View Products")
        print("2. Place New Order")
        print("3. View All Orders")
        print("4. Generate Reports")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            for p in products.values():
                print(f"{p.id}: {p.name} - Rs.{p.price} (Stock: {p.stock})")

        elif choice == "2":
            name = input("Enter customer name: ")
            order_items = []
            while True:
                pid = int(input("Enter product id (0 to stop): "))
                if pid == 0:
                    break
                qty = int(input("Enter quantity: "))
                product = products.get(pid)
                if product and product.stock >= qty:
                    order_items.append({"product_id": pid, "qty": qty})
                    product.update_stock(qty)
                else:
                    print("Invalid product or not enough stock!")

            if order_items:
                new_order = {
                    "order_id": max(o["order_id"] for o in orders) + 1,
                    "customer": name,
                    "items": order_items
                }
                orders.append(new_order)
                save_orders(orders)
                save_products(products)
                print("Order placed successfully!")

        elif choice == "3":
            for order in orders:
                print(f"Order {order['order_id']} by {order['customer']}:")
                total = 0
                for item in order["items"]:
                    p = products[item["product_id"]]
                    cost = p.price * item["qty"]
                    print(f"  {p.name} x {item['qty']} = {cost}")
                    total += cost
                print(f"Total: {total}\n")

        elif choice == "4":
            sales_report(orders, products)
            inventory_report(products)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()
