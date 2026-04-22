import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

def search_product_safe(name):
    # Validation
    if not isinstance(name, str):
        print("Error: name must be a string")
        return None
    if len(name) < 2:
        print("Error: name must be at least 2 characters")
        return None
    if "<" in name or ">" in name or ";" in name:
        print("Error: name contains invalid characters")
        return None

    query = "SELECT * FROM products WHERE name LIKE ?"
    rows = conn.execute(query, (f"%{name}%",)).fetchall()
    return rows

def login_safe(username, password):
    # Validation
    if not isinstance(username, str):
        print("Error: username must be a string")
        return None
    if username.strip() == "":
        print("Error: username cannot be empty")
        return None
    if " " in username:
        print("Error: username must not contain spaces")
        return None

    if not isinstance(password, str):
        print("Error: password must be a string")
        return None
    if len(password) < 6:
        print("Error: password must be at least 6 characters")
        return None

    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    row = conn.execute(query, (username, password)).fetchone()
    return row

# Required test cases
print("Test 1:", search_product_safe('cement'))
print("Test 2:", search_product_safe(''))
print("Test 3:", search_product_safe('<script>'))
print("Test 4:", login_safe('admin', 'admin123'))
print("Test 5:", login_safe('admin', 'ab'))
print("Test 6:", login_safe('ad min', 'pass123'))
