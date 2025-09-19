import csv
import json
from product import Product

#CSV Handling
def load_products(filename="products.csv"):
    products = {}
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            p = Product(row["id"], row["name"], row["category"], row["price"], row["stock"])
            products[int(row["id"])] = p
    return products


def save_products(products, filename="products.csv"):
    with open(filename, "w", newline="") as f:
        fieldnames = ["id", "name", "category", "price", "stock"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in products.values():
            writer.writerow({
                "id": p.id,
                "name": p.name,
                "category": p.category,
                "price": p.price,
                "stock": p.stock
            })


#JSON Handling
def load_orders(filename="orders.json"):
    with open(filename, "r") as f:
        return json.load(f)


def save_orders(orders, filename="orders.json"):
    with open(filename, "w") as f:
        json.dump(orders, f, indent=2)


#Reports
def sales_report(orders, products):
    total_revenue = 0
    revenue_by_category = {}
    customer_spending = {}

    for order in orders:
        cust = order["customer"]
        total = 0
        for item in order["items"]:
            pid = item["product_id"]
            qty = item["qty"]
            product = products[pid]
            revenue = product.price * qty
            total += revenue
            total_revenue += revenue

            revenue_by_category[product.category] = revenue_by_category.get(product.category, 0) + revenue

        customer_spending[cust] = customer_spending.get(cust, 0) + total

    top_customer = max(customer_spending, key=customer_spending.get)

    print("\n--- Sales Report ---")
    print(f"Total Revenue: {total_revenue}")
    print("Revenue by Category:", revenue_by_category)
    print(f"Top Customer: {top_customer} - {customer_spending[top_customer]}")


def inventory_report(products):
    low_stock = [p.name for p in products.values() if p.stock < 5]

    avg_by_category = {}
    category_count = {}
    for p in products.values():
        avg_by_category[p.category] = avg_by_category.get(p.category, 0) + p.price
        category_count[p.category] = category_count.get(p.category, 0) + 1

    for cat in avg_by_category:
        avg_by_category[cat] /= category_count[cat]

    print("\n--- Inventory Report ---")
    print("Low Stock Products:", low_stock)
    print("Average Price by Category:", avg_by_category)
