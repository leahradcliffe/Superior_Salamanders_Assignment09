# File Name : module2.py
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



def get_manufacturer_name(manufacturer_id):
    """
    Function to get the manufacturer name using the manufacturer ID
    """
    conn = connect_to_server()
    cursor = conn.cursor()
    query = f"""
    SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}
    """
    cursor.execute(query)
    result = cursor.fetchone()
    manufacturer_name = result[0] if result else "Unknown Manufacturer"
    cursor.close()
    conn.close()
    return manufacturer_name
def get_brand_name(brand_id):
    """
    Function to get the brand name using the brand ID
    """
    conn = connect_to_server()
    cursor = conn.cursor()
    query = f"""
    SELECT Brand FROM tBrand WHERE BrandID = {brand_id}
    """
    cursor.execute(query)
    result = cursor.fetchone()
    brand_name = result[0] if result else "Unknown Brand"
    cursor.close()
    conn.close()
    return brand_name

