import os
import pyodbc
import pandas as pd
import config
import numpy as np
import sys
sys.path.insert(0, 'C:\\Users\\ayany\\Desktop\\BI project 2')
import utils
def connect_db_create_cursor(database_conf_name):
    # Call to read the configuration file
    db_conf = utils.get_sql_config(config.sql_server_config, database_conf_name)
    # Create a connection string for SQL Server
    db_conn_str = 'Driver={};Server={};Database={};Trusted_Connection={};'.format(*db_conf)
    # Connect to the server and to the desired database
    db_conn = pyodbc.connect(db_conn_str)
    # Create a Cursor class instance for executing T-SQL statements
    db_cursor = db_conn.cursor()
    return db_cursor


def load_query(query_name):
    sql_script = None  # Initialize sql_script to None
    for script in os.listdir(config.input_dir):
        if query_name in script:
            with open(os.path.join(config.input_dir, script), 'r') as script_file:
                sql_script = script_file.read()
            break
    if sql_script is None:
        raise FileNotFoundError(f"No SQL script found for {query_name}")
    return sql_script

def insert_into_Categories(cursor, table_name, db, schema, source_data):
    # Read the excel table
    df = pd.read_excel(source_data, sheet_name = table_name)

    insert_into_table_script = load_query('insert_into_{}'.format(table_name)).format(db=db, schema=schema)

    # Populate a table in sql server
    for index, row in df.iterrows():
        cursor.execute(insert_into_table_script, row['CategoryID'], row['CategoryName'], row['Description'])
        cursor.commit()

    print(f"{len(df)} rows have been inserted into the {db}.{schema}.{table_name} table")

def insert_into_Customers(cursor, table_name, db, schema, source_data):
    # Read the excel table
    df = pd.read_excel(source_data, sheet_name = table_name, header=0)
    df = df.where(pd.notna(df), None)

    insert_into_table_script = load_query('insert_into_{}'.format(table_name)).format(db=db, schema=schema)

    # Populate a table in sql server
    for index, row in df.iterrows():
        cursor.execute(insert_into_table_script, row['CustomerID'], row['CompanyName'], row['ContactName'], row['ContactTitle'], row['Address'], row['City'], row['Region'], row['PostalCode'],  row['Country'], row['Phone'], row['Fax'])
        cursor.commit()

    print(f"{len(df)} rows have been inserted into the {db}.{schema}.{table_name} table")

def insert_into_Employees(cursor, table_name, db, schema, source_data):
    # Read the excel table
    df = pd.read_excel(source_data, sheet_name = table_name, header=0)
    df['ReportsTo'] = pd.to_numeric(df['ReportsTo'], errors='coerce')
    df.replace({np.nan: None}, inplace=True)

    insert_into_table_script = load_query('insert_into_{}'.format(table_name)).format(db=db, schema=schema)

    # Populate a table in sql server
    for index, row in df.iterrows():
        cursor.execute(insert_into_table_script, row["EmployeeID"], row["LastName"], row["FirstName"], row["Title"], row["TitleOfCourtesy"], row["BirthDate"], row["HireDate"], row["Address"], row["City"], row["Region"], row["PostalCode"], row["Country"], row["HomePhone"], row["Extension"], row["Notes"], row["ReportsTo"], row["PhotoPath"])
        cursor.commit()

    print(f"{len(df)} rows have been inserted into the {db}.{schema}.{table_name} table")

def insert_into_Suppliers(cursor, table_name, db, schema, source_data):
    # Read the excel table
    df = pd.read_excel(source_data, sheet_name = table_name, header=0)
    df = df.where(pd.notna(df), None)
    insert_into_table_script = load_query('insert_into_{}'.format(table_name)).format(db=db, schema=schema)

    # Populate a table in sql server
    for index, row in df.iterrows():
        cursor.execute(insert_into_table_script, row["SupplierID"], row["CompanyName"], row["ContactName"], row["ContactTitle"], row["Address"], row["City"], row["Region"], row["PostalCode"], row["Country"], row["Phone"], row["Fax"], row["HomePage"])
        cursor.commit()

    print(f"{len(df)} rows have been inserted into the {db}.{schema}.{table_name} table")

def insert_into_Shippers(cursor, table_name, db, schema, source_data):
    # Read the excel table
    df = pd.read_excel(source_data, sheet_name = table_name, header=0)
    df = df.where(pd.notna(df), None)
    insert_into_table_script = load_query('insert_into_{}'.format(table_name)).format(db=db, schema=schema)

    # Populate a table in sql server
    for index, row in df.iterrows():
        cursor.execute(insert_into_table_script, row["ShipperID"], row["CompanyName"], row["Phone"])
        cursor.commit()

    print(f"{len(df)} rows have been inserted into the {db}.{schema}.{table_name} table")

def insert_into_Region(cursor, table_name, db, schema, source_data):
    # Read the excel table
    df = pd.read_excel(source_data, sheet_name = table_name, header=0)
    df = df.where(pd.notna(df), None)
    insert_into_table_script = load_query('insert_into_{}'.format(table_name)).format(db=db, schema=schema)

    # Populate a table in sql server
    for index, row in df.iterrows():
        cursor.execute(insert_into_table_script, row["RegionID"], row["RegionDescription"])
        cursor.commit()

    print(f"{len(df)} rows have been inserted into the {db}.{schema}.{table_name} table")

def insert_into_Products(cursor, table_name, db, schema, source_data):
    # Read the excel table
    df = pd.read_excel(source_data, sheet_name = table_name, header=0)
    df = df.where(pd.notna(df), None)
    insert_into_table_script = load_query('insert_into_{}'.format(table_name)).format(db=db, schema=schema)

    # Populate a table in sql server
    for index, row in df.iterrows():
        cursor.execute(insert_into_table_script, row["ProductID"], row["ProductName"], row["SupplierID"], row["CategoryID"], row["QuantityPerUnit"], row["UnitPrice"], row["UnitsInStock"], row["UnitsOnOrder"], row["ReorderLevel"], row["Discontinued"])
        cursor.commit()

    print(f"{len(df)} rows have been inserted into the {db}.{schema}.{table_name} table")

def insert_into_Territories(cursor, table_name, db, schema, source_data):
    # Read the excel table
    df = pd.read_excel(source_data, sheet_name = table_name, header=0)
    df = df.where(pd.notna(df), None)
    insert_into_table_script = load_query('insert_into_{}'.format(table_name)).format(db=db, schema=schema)

    # Populate a table in sql server
    for index, row in df.iterrows():
        cursor.execute(insert_into_table_script, row["TerritoryID"], row["TerritoryDescription"], row["RegionID"])
        cursor.commit()

    print(f"{len(df)} rows have been inserted into the {db}.{schema}.{table_name} table")

def insert_into_Orders(cursor, table_name, db, schema, source_data):
    # Read the excel table
    df = pd.read_excel(source_data, sheet_name = table_name, header=0)
    df = df.where(pd.notna(df), None)
    insert_into_table_script = load_query('insert_into_{}'.format(table_name)).format(db=db, schema=schema)

    # Populate a table in sql server
    for index, row in df.iterrows():
        cursor.execute(insert_into_table_script, row["OrderID"], row["CustomerID"], row["EmployeeID"], row["OrderDate"], row["RequiredDate"], row["ShippedDate"], row["ShipVia"], row["Freight"], row["ShipName"], row["ShipAddress"], row["ShipCity"], row["ShipRegion"], row["ShipPostalCode"], row["ShipCountry"], row["TerritoryID"])
        cursor.commit()

    print(f"{len(df)} rows have been inserted into the {db}.{schema}.{table_name} table")

def insert_into_OrderDetails(cursor, table_name, db, schema, source_data):
    # Read the excel table
    df = pd.read_excel(source_data, sheet_name = table_name, header=0)
    df = df.where(pd.notna(df), None)
    insert_into_table_script = load_query('insert_into_{}'.format(table_name)).format(db=db, schema=schema)

    # Populate a table in sql server
    for index, row in df.iterrows():
        cursor.execute(insert_into_table_script, row["OrderID"], row["ProductID"], row["UnitPrice"], row["Quantity"], row["Discount"])
        cursor.commit()

    print(f"{len(df)} rows have been inserted into the {db}.{schema}.{table_name} table")