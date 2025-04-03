# File Name : module3.py
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

from package1.module1 import connect_to_server

def get_number_of_items_sold(product_id):
    conn = connect_to_server()
    cursor = conn.cursor()

    query = f"""
    SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
    FROM dbo.tTransactionDetail
    INNER JOIN dbo.tTransaction 
    ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID 
    WHERE dbo.tTransaction.TransactionTypeID = 1 
    AND dbo.tTransactionDetail.ProductID = {product_id}
    """
    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result[0] if result and result[0] is not None else 0

def print_product_sales_statement(product_id, description, manufacturer_name, brand_name):
    number_of_items_sold = get_number_of_items_sold(product_id)
    sentence = f"The product '{description}' from {manufacturer_name} under the brand {brand_name} has been sold {number_of_items_sold} times."
    print(sentence)

