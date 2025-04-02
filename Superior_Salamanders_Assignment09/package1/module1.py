#module1.py

import pyodbc
import random

def connect_to_server():

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                          'Database=IS4010;'
                          'uid=IS4010Login;'
                          'pwd=P@ssword2;')
    return conn
    cursor = conn.cursor()
    #1.Submit this query and store the results in a data structure:
    def get_product_data():
        conn = connect_to_server()
        cursor = conn.cursor()

    cursor.execute('SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct')
    for row in cursor:


