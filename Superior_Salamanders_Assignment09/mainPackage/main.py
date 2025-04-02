#main.py

from package1.module1 import get_product_data, connect_to_server
from package2.module2 import get_manufacturer_name, get_brand_name
import random

if __name__ == "__main__":
    

    def get_items_sold(product_id):
        conn = connect_to_server()
        cursor = conn.cursor()
        query = """
            SELECT SUM(dbo.tTransactionDetail.QtyOfProduct)
            FROM dbo.tTransactionDetail
            INNER JOIN dbo.tTransaction
            ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
            WHERE dbo.tTransaction.TransactionTypeID = 1
            AND dbo.tTransactionDetail.ProductID = ?
        """
        cursor.execute(query, (product_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] if result and result[0] is not None else 0

    def main():
        products = get_product_data()
        if not products:
            print("No products found.")
            return

        product = random.choice(products)
        description = product['Description']
        product_id = product['ProductID']
        manufacturer = get_manufacturer_name(product['ManufacturerID'])
        brand = get_brand_name(product['BrandID'])
        items_sold = get_items_sold(product_id)

        print(f"The product '{description}' by {manufacturer} under the brand {brand} has sold {items_sold} items.")


