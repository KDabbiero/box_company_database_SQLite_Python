# Overview

The software that I wrote creates and interacts with a database file using the SQLite library in Python. I already had a good understanding of SQL and wanted to learn how to write a program using Python that interacted with a database. The database consists of four tables and is a model for a box company. The program allows the user to view, insert, delete, and update data in the database. 

[Software Demo Video](https://youtu.be/vnbSrJhEGUQ)

# Entity Relationship Diagram

![ERD](bai_db_diagram.jpg)

# Relational Database

The relational database that I am using is a model database for an industrial box company. It consists of four tables; location, product_dims, product, and invoice. 

The location table contains the location_id, address_1, address_2, city, state, zip_code columns. The product_dims table contains the product_dims_id, product_type_id, box_length, box_width, box_height, box_wall_type, and foam_measurements columns. The product table contains the product_id, product_dims_id, product_type_id, and product_quantity columns with product_dims_id being a foreign key referencing the product_dims_id primary key column in the product_dims table. The invoice table contains the invoice_id, price, product_id, and delivery_date columns with the product_id being a foreign key referencing the product_id primary key in the product table. 
# Development Environment


GitHub
VSCode

Python 3.9

SQLite3
# Useful Websites

* [SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-python/create-tables/)
* [Python](https://docs.python.org/3.8/library/sqlite3.html#controlling-transactions)

# Future Work

* Create a view for a delivery form that joins the location and invoice tables.
* Clean up the way that I did the delete portion by using more concatenation instead of more functions.
* Add a product_type table that I decided to leave out for the sake of brevity.
