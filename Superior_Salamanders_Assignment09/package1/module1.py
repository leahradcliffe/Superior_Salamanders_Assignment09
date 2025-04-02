#Assignment 09
# module1.py
#vsjhlbdv 
import pyodbc
import random

def connect_to_server():
    """Establish a connection to the SQL Server database."""
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
        'Database=IS4010;'
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

