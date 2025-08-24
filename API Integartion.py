"""
Level 2
Task 3: API Integration
Write a python Script that interacts with an API to retrieve and display data.
"""

import requests

def fetch_products():
    url = "https://dummyjson.com/products"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes
        data = response.json()

        products = data.get('products', [])
        if not products:
            print("No products found.")
            return

        print("Product List:")
        for product in products:
            print(f"ID: {product.get('id')}, Title: {product.get('title')}, Price: ${product.get('price')}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching products: {e}")

if __name__ == "__main__":
    fetch_products()
