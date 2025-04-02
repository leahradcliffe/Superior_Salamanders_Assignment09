# File Name : module1.py
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

 
import pyodbc
import random

def connect_to_server():
    """Establish a connection to the SQL Server database."""
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
        'Database=GroceryStoreSimulator;'
        'uid=IS4010Login;'
        'pwd=P@ssword2;'
    )
    return conn

def get_product_data():
    """Fetch product data from the database and return it as a list of dictionaries."""
    conn = connect_to_server()
    cursor = conn.cursor()

    query = """
    SELECT ProductID, [UPC-A], Description, ManufacturerID, BrandID
    FROM dbo.tProduct
    """
    cursor.execute(query)
    results = cursor.fetchall()

    # Convert to a list of dictionaries for easier access
    products = []
    for row in results:
        products.append({
            'ProductID': row.ProductID,
            'UPC-A': row[1],  # Assuming the second column is UPC-A
            'Description': row.Description,
            'ManufacturerID': row.ManufacturerID,
            'BrandID': row.BrandID
        })

    cursor.close()
    conn.close()

    return products

def select_random_product(products):
    """Randomly select one product and return relevant information."""
    selected_product = random.choice(products)

    product_id = selected_product['ProductID']
    description = selected_product['Description']
    manufacturer_id = selected_product['ManufacturerID']
    brand_id = selected_product['BrandID']

    return product_id, description, manufacturer_id, brand_id
    