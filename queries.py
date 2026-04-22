import sqlite3

conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor() # Create a cursor object to execute SQL queries

# Query A get every column of every product
print("Query A")
rows = cursor.execute("SELECT * FROM products").fetchall()
for row in rows:
    print(row)
print()


# Query B get the name and price of every product
print("Query B")
rows = cursor.execute("SELECT name, price FROM products").fetchall()
for row in rows:
    print(row)
print()

# Query C get the product with id 3
print("Query C")
rows = cursor.execute("SELECT * FROM products WHERE id = 3").fetchall()
for row in rows:
    print(row)
print()

# Query D get all products whose name contains the word "sheet"
print("Query D")
rows = cursor.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall()
for row in rows:
    print(row)
print()

# Query E get all products ordered by price from highest to lowest
print("Query E")
rows = cursor.execute("SELECT * FROM products ORDER BY price DESC").fetchall()
for row in rows:
    print(row)
print()

# Query F get the two most expensive products
print("Query F")
rows = cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2").fetchall()
for row in rows:
    print(row)
print()

# Query G update the price of the product with id 1 to 38000 and then retrieve that product to confirm the update
print("Query G")
cursor.execute("UPDATE products SET price = 38000 WHERE id = 1")
conn.commit()

rows = cursor.execute("SELECT * FROM products WHERE id = 1").fetchall()
for row in rows:
    print(row)
print()