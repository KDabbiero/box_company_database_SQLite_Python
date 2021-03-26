import sqlite3
from sqlite3 import Error

# Creates the connection to the database.
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect('bai.db')
        return conn
    # If connection fails then an error message is printed.
    except Error as e:
        print(e)
    return conn

# Create the tables.
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# Functions for the manual inserts.
def insert_into_location_table(conn, insert_into_locations_sql):
    try:
        c = conn.cursor()
        c.executemany('INSERT INTO location VALUES (?, ?, ?, ?, ?, ?)', insert_into_locations_sql)
        conn.commit()
    except Error as e:
        print(e)

# Manual.
def insert_into_product_dims_table(conn, insert_into_product_dims_sql):
    try:
        c = conn.cursor()
        c.executemany('INSERT INTO product_dims (product_dims_id, product_type_id, box_length, box_width, box_height, box_wall_type, foam_measurements) VALUES (?, ?, ?, ?, ?, ?, ?) ', insert_into_product_dims_sql)
        conn.commit()
    except Error as e:
        print(e)

# Manual.
def insert_into_product_table(conn, insert_into_product_sql):
    try:
        c = conn.cursor()
        c.executemany('INSERT INTO product (product_id, product_type_id, product_dims_id, product_quantity) VALUES (?, ?, ?, ?)', insert_into_product_sql)
        conn.commit()
    except Error as e:
        print(e)

# Manual.
def insert_into_invoice_table(conn, insert_into_invoice_sql):
    try:
        c = conn.cursor()
        c.executemany('INSERT INTO invoice (invoice_id, price, product_id, delivery_date) VALUES (?, ?, ?, ?)', insert_into_invoice_sql)
        conn.commit()
    except Error as e:
        print(e)

# Prompt the user for what table they want to view.
def get_select_statement():
    table = input("What table contents would you like to view? \nlocation \nproduct_dims \nproduct \ninvoice \ninvoice-product>>>")
    if table == 'location':
        select_statement_sql = 'SELECT * FROM location'
    elif table == 'product_dims':
        select_statement_sql = 'SELECT * FROM product_dims'
    elif table == 'product':
        select_statement_sql = 'SELECT * FROM product'
    elif table == 'invoice':
        select_statement_sql = 'SELECT * FROM invoice'
    elif table == 'invoice-product':
        select_statement_sql = 'SELECT i.invoice_id, i.price, i.delivery_date FROM invoice i JOIN product p ON i.product_id = p.product_id'
    else:
        print("Invalid input.")
    return select_statement_sql

# Execute the select statement.
def execute_select(conn, select_statement_sql):
    try:
        c = conn.cursor()
        c.execute(select_statement_sql)
        print(c.fetchall())
    except Error as e:
        print(e)

# Get user inserts and perform the insert.
def user_insert_statement(conn):
    table = input("What table would you like to insert data into? \nlocation \nproduct_dims \nproduct \ninvoice \n>>>")
    if table == 'location':
        location_id = int(input("Enter location_id: "))
        address_1 = str(input("Enter address_1: "))
        address_2 = str(input("Enter address_2: "))
        city = str(input("Enter city: "))
        state = str(input("Enter state: "))
        zip_code = str(input("Enter zip code: "))
        try:
            c = conn.cursor()
            c.execute('INSERT INTO location VALUES (?, ?, ?, ?, ?, ?)', (location_id, address_1, address_2, city, state, zip_code))
            conn.commit()
            print('Insert successfully completed!')
        except Error as e:
            print(e)
    elif table == 'product_dims':
        product_dims_id = int(input("Enter product_dims_id: "))
        product_type_id = str(input("Enter product_type_id: "))
        box_length = int(input("Enter box_length: "))
        box_width = int(input("Enter box_width: "))
        box_height = int(input("Enter box_height: "))
        box_wall_type = str(input("Enter box_wall_type: "))
        foam_measurements = int(input("Enter foam_measurements: "))
        try:
            c = conn.cursor()
            c.execute('INSERT INTO product_dims VALUES (?, ?, ?, ?, ?, ?, ?)',(product_dims_id, product_type_id, box_length, box_width, box_height, box_wall_type, foam_measurements))
            conn.commit()
            print('Insert successfully completed!')
        except Error as e:
            print(e)
    elif table == 'product':
        product_id = int(input("Enter product_id: "))
        product_type_id = str(input("Enter product_type_id: "))
        product_dims_id = int(input("Enter product_dims_id: "))
        product_quantity = int(input("Enter product_quantity: "))
        try:
            c = conn.cursor()
            c.execute('INSERT INTO product VALUES (?, ?, ?, ?)', (product_id, product_type_id, product_dims_id, product_quantity))
            conn.commit()
            print('Insert successfully completed!')
        except Error as e:
            print(e)
    elif table == 'invoice':
        invoice_id = int(input("Enter invoice_id: "))
        price = float(input("Enter price: "))
        product_id = int(input("Enter product_id: "))
        delivery_date = str(input("Enter date as YYYY-MM-DD: "))
        try:
            c = conn.cursor()
            c.execute('INSERT INTO invoice VALUES (?, ?, ?, ?)', (invoice_id, price, product_id, delivery_date))
            print('Insert successfully completed!')
        except Error as e:
            print(e)
    else:
        print("Invalid input.")

# Prompt the user for the table to have rows deleted from.
def get_table_delete():
    table = input("What table would you like to delete data from? \nlocation \nproduct_dims \nproduct \ninvoice \n>>>")
    return table

# Delete from location.
def user_delete_location_statement(conn, table):
    column = input('What field would you like to filter and have deleted? \nlocation_id \naddress_1 \naddress_2 \ncity \nstate \nzip_code\n>>>')
    if column == 'location_id':
        value = input('Enter location_id: ')
        sql = 'DELETE FROM location WHERE location_id = ?'
    elif column == 'address_1':
        value = str(input('Enter address_1: '))
        sql = 'DELETE FROM location WHERE address_1 = ?'
    elif column == 'address_2':
        value = str(input('Enter address_2: '))
        sql = 'DELETE FROM location WHERE address_2 = ?'
    elif column == 'city':
        value = str(input('Enter city: '))
        sql = 'DELETE FROM location WHERE city = ?'
    elif column == 'state':
        value = str(input('Enter state: '))
        sql = 'DELETE FROM location WHERE state = ?'
    elif column == 'zip_code':
        value = str(input('Enter zip_code: '))
        sql = 'DELETE FROM location WHERE zip_code = ?'
    try:
        c = conn.cursor()
        c.execute(sql, (value,))
        conn.commit()
        print('Successfully deleted row!')
    except Error as e:
        print(e)

# Delete from product_dims.
def user_delete_product_dims_statement(conn, tab):
    column = input('What field would you like to filter and have deleted? \nproduct_dims_id \nproduct_type_id \nbox_length \nbox_width \nbox_height \nbox_wall_type \nfoam_measurements\n>>>')
    if column == 'product_dims_id':
        value = int(input('Enter product_dims_id: '))
        sql = 'DELETE FROM product_dims WHERE product_dims_id = ?'
    elif column == 'product_type_id':
        value = str(input('Enter product_type_id: '))
        sql = 'DELETE FROM product_dims WHERE product_type_id = ?'
    elif column == 'box_length':
        value = int(input('Enter box_length: '))
        sql = 'DELETE FROM product_dims WHERE box_length = ?'
    elif column == 'box_width':
        value = int(input('Enter box_width: '))
        sql = 'DELETE FROM product_dims WHERE box_width = ?'
    elif column == 'box_height':
        value = int(input('Enter box_height: '))
        sql = 'DELETE FROM product_dims WHERE box_height = ?'
    elif column == 'box_wall_type':
        value = str(input('Enter box_wall_type: '))
        sql = 'DELETE FROM product_dims WHERE box_wall_type = ?'
    elif column == 'foam_measurement':
        value = int(input('Enter foam_measurement: '))
        sql = 'DELETE FROM product_dims WHERE foam_measurements = ?'
    try:
        c = conn.cursor()
        c.execute(sql, (value,))
        conn.commit()
        print('Successfully deleted row!')
    except Error as e:
        print(e)

# Delete from product.
def user_delete_product_statement(conn, tab):
    column = input('What field would you like to filter and have deleted? \nproduct_id \nproduct_type_id \nproduct_dims_id \nproduct_quantity\n>>>')
    if column == 'product_id':
        value = int(input('Enter product_id: '))
        sql = 'DELETE FROM product WHERE product_id = ?'
    elif column == 'product_type_id':
        value = str(input('Enter product_type_id: '))
        sql = 'DELETE FROM product WHERE product_type_id = ?'
    elif column == 'product_dims_id':
        value = int(input('Enter product_dims_id: '))
        sql = 'DELETE FROM product WHERE product_dims_id = ?'
    elif column == 'product_quantity':
        value = int(input('Enter product_quantity: '))
        sql = 'DELETE FROM product WHERE product_quantity = ?'
    try:
        c = conn.cursor()
        c.execute(sql, (value,))
        conn.commit()
        print('Successfully deleted row!')
    except Error as e:
        print(e)

# Delete from invoice.
def user_delete_invoice_statement(conn, table):
    column = input('What field would you like to filter and have deleted? \n1) invoice_id \n2) price \n3) product_id \n4) delivery_date \n>>>')
    if column == 'invoice_id':
        value = int(input('Enter invoice_id: '))
        sql = 'DELETE FROM invoice WHERE invoice_id = ?'
    elif column == 'price':
        value = float(input('Enter price ($): '))
        sql = 'DELETE FROM invoice WHERE price = ?'
    elif column == 'product_id':
        value = int(input('Enter product_id: '))
        sql = 'DELETE FROM invoice WHERE product_id = ?'       
    elif column == 'delivery_date':
        value = input('Enter delivery_date (YYYY-MM-DD): ')
        sql = 'DELETE FROM invoice WHERE delivery_date = ?'       
    else:
        print('Invalid input!')
    try:
        c = conn.cursor()
        c.execute(sql, (value,))
        print('Successfully deleted row!')
        conn.commit()
    except Error as e:
        print(e)

# Get the table to be updated from user.
def user_update_table():
    table = input('What table would you like to update? \nlocation \nproduct_dims \nproduct \ninvoice \n>>>')
    return table

# Get the column that will be updated from user. (Location)     
def user_update_location_column():
    column = input('What column would you like to update? \nlocation_id \naddress_1 \naddress_2 \ncity \nstate \nzip_code \n>>>')
    return column

def user_update_location_statement(conn, column):
    cond_column = input('Enter conditional column: \nlocation_id \naddress_1 \naddress_2 \ncity \nstate \nzip_code \n>>>')
    cond_value = input('Enter conditional value: ')
    column_update_val = input('Enter the new value: ')
    sql = 'UPDATE location SET '+column+' = ? WHERE '+cond_column+' = ?'
    try:
        c = conn.cursor()
        c.execute(sql, (column_update_val, cond_value))
        conn.commit()
    except Error as e:
        print(e)

# Get the column to be updated from the user. (product_dim)
def user_update_product_dims_column():
    column = input('What column would you like to update? \nproduct_dims_id \nproduct_type_id \nbox_length \nbox_width \nbox_height \nbox_wall_type \nfoam_measurements \n>>>')
    return column

# Execute the update on product_dims.
def user_update_product_dims_statement(conn, column):
    cond_column = input('Enter conditional column: \nproduct_dims_id \nproduct_type_id \nbox_length \nbox_width \nbox_height \nbox_wall_type \nfoam_measurements \n>>>')
    cond_value = input('Enter conditional value: ')
    column_update_val = input('Enter the new value: ')
    sql = 'UPDATE product_dims SET '+column+' = ? WHERE '+cond_column+' = ?'
    try:
        c = conn.cursor()
        c.execute(sql, (column_update_val, cond_value))
        conn.commit()
    except Error as e:
        print(e)

# Get the column to be updated. (product)
def user_update_product_column():
    column = input('What column would you like to update? \nproduct_id \nproduct_type_id \nproduct_dims_id \nproduct_quantity \n>>>')
    return column

# Execute the update on the product table. 
def user_update_product_statement(conn, column):
    cond_column = input('Enter conditional column: \nproduct_id \nproduct_type_id \nproduct_dims_id \nproduct_quantity \n>>>')
    cond_value = input('Enter conditional value: ')
    column_update_val = input('Enter the new value: ')
    sql = 'UPDATE product SET '+column+' = ? WHERE '+cond_column+' = ?'
    try:
        c = conn.cursor()
        c.execute(sql, (column_update_val, cond_value))
        conn.commit()
    except Error as e:
        print(e)

# Get the column to be updated from user. (invoice)
def user_update_invoice_column():
    column = input('What column would you like to update? \ninvoice_id \nprice \nproduct_id \ndelivery_date \n>>>')
    return column

# Execute the update on the invoice table. 
def user_update_invoice_statement(conn, column):
    cond_column = input('Enter conditional column: \ninvoice_id \nprice \nproduct_id \ndelivery_date \n>>>')
    cond_value = input('Enter conditional value: ')
    column_update_val = input('Enter the new value: ')
    sql = 'UPDATE invoice SET '+column+' = ? WHERE '+cond_column+' = ?'
    try:
        c = conn.cursor()
        c.execute(sql, (column_update_val, cond_value))
        conn.commit()
    except Error as e:
        print(e)

def main():
    database = r"C:\Users\katel\Desktop\CSE310\Mod5\bai.db"

    # Create the location table.
    sql_create_location_table = """ CREATE TABLE IF NOT EXISTS location (
        location_id integer NOT NULL,
        address_1 varchar(50) NOT NULL,
        address_2 varchar(50) NOT NULL,
        city varchar(50) NOT NULL,
        state char(2) NOT NULL,
        zip_code varchar(10) NOT NULL
    );"""

    # Create the locations inserts.
    locations = [(1, '123 West St.', 'Suite F', 'North Port', 'FL', '342000'), (2, '456 East St.', 'Suite E', 'Venice', 'FL', '342002')]

    # Create the product dimensions table.
    sql_create_product_dims_table = """ CREATE TABLE IF NOT EXISTS product_dims (
        product_dims_id integer NOT NULL,
        product_type_id integer NOT NULL,
        box_length integer,
        box_width integer,
        box_height integer,
        box_wall_type varchar(10),
        foam_measurements integer
    ); """

    # Create the product dimensions inserts.
    product_dims = [(1, 1, '20', '20', '20', '2', 'NULL'), (2, 2, 'NULL', 'NULL', 'NULL', 'NULL', '22')]

    # Create the product table.
    sql_create_product_table = """ CREATE TABLE IF NOT EXISTS product (
        product_id integer NOT NULL,
        product_type_id integer NOT NULL,
        product_dims_id integer NOT NULL,
        product_quantity integer NOT NULL,
        FOREIGN KEY (product_dims_id) REFERENCES product_dims (product_dims_id)
    ); """

    # Create the product inserts.
    product = [(1, 1, 1, '20'), (2, 2, 2, '50')]

    # Create the invoice table.
    sql_create_invoice_table = """ CREATE TABLE IF NOT EXISTS invoice (
        invoice_id integer NOT NULL,
        price decimal NOT NULL,
        product_id integer NOT NULL,
        delivery_date date NOT NULL,
        FOREIGN KEY (product_id) REFERENCES product (product_id)
    ); """

    # Create the invoice inserts.
    invoice = [(1, '20.30', 1, '2018-07-21'), (2, '50.56', 2, '2019-10-30')]

    # Establish the connection to the database.
    conn = create_connection(database)
    if conn is not None:
        # Create the tables.
        create_table(conn, sql_create_location_table)
        create_table(conn, sql_create_product_dims_table)
        create_table(conn, sql_create_product_table)
        create_table(conn, sql_create_invoice_table)  

        # Insert into the tables.
        insert_into_location_table(conn, locations)
        insert_into_product_dims_table(conn, product_dims)
        insert_into_product_table(conn, product)
        insert_into_invoice_table(conn, invoice)

        user_input = ''
        while user_input != 'Done':
            # Get input for what action to take.
            user_input = input('What action would you like to perform? \nView Table \nInsert Data \nDelete Data \nUpdate Data\nDone\n>>>')
            if user_input == 'View Table':
                # Set the select statement.
                select_statement_sql = get_select_statement()
                # Execute the select statement.
                execute_select(conn, select_statement_sql)
            elif user_input == 'Insert Data':
                user_insert_statement(conn)
            elif user_input == 'Delete Data':
                # Set the table for the delete statements. 
                table = get_table_delete()
                # Execute the delete statements.
                if table == 'location':
                    user_delete_location_statement(conn, table)
                elif table == 'product_dims':
                    user_delete_product_dims_statement(conn, table)
                elif table == 'product':
                    user_delete_product_statement(conn, table)
                elif table == 'invoice':
                    user_delete_invoice_statement(conn, table)
            elif user_input == 'Update Data':
                table = user_update_table()
                if table == 'location':
                    column = user_update_location_column()
                    user_update_location_statement(conn, column)
                elif table == 'product_dims':
                    column = user_update_product_dims_column()
                    user_update_product_dims_statement(conn, column)
                elif table == 'product':
                    column = user_update_product_column()
                    user_update_product_statement(conn, column)
                elif table == 'invoice':
                    column = user_update_invoice_column()
                    user_update_invoice_statement(conn, column)
    else:
        print("Error! Cannot create database connection.")

if __name__ == '__main__':
    main()

