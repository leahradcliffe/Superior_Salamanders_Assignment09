
# File Name : main.py
# Student Name: Uruz B, Leah R, Justin G
# email:  bidiwaur@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: April 2, 2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Group project connecting to SQL database

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant:

from package1.module1 import get_product_data
from package2.module2 import get_manufacturer_name, get_brand_name
from package3.module3 import print_product_sales_statement

import random

def main():
    products = get_product_data()
    if not products:
        return

    product = random.choice(products)

    description = product['Description']
    product_id = product['ProductID']
    manufacturer_id = product['ManufacturerID']
    brand_id = product['BrandID']

    manufacturer = get_manufacturer_name(manufacturer_id)
    brand = get_brand_name(brand_id)

    print(f"The product {description} (ProductID: {product_id}) is manufactured by {manufacturer} "
          f"(ManufacturerID: {manufacturer_id}) under the brand {brand} (BrandID: {brand_id}).")

    print_product_sales_statement(product_id, description, manufacturer, brand)

if __name__ == "__main__":
    main()
