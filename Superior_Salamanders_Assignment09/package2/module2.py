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

