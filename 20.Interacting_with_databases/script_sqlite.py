import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db") #establishing connection
    cur = conn.cursor() # creating cursor

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # execute sql commands

    cur.execute("INSERT INTO store VALUES ('Wine Glass', 2, 110)")
    conn.commit() # commit the connection
    conn.close() # close the connection

def insert(item, qty, price):
    conn = sqlite3.connect("lite.db") #establishing connection
    cur = conn.cursor() # creating cursor

    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, qty, price))
    conn.commit() # commit the connection
    conn.close() # close the connection

def view():
    conn = sqlite3.connect("lite.db") #establishing connection
    cur = conn.cursor() # creating cursor

    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close() # close the connection
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db") #establishing connection
    cur = conn.cursor() # creating cursor

    cur.execute("DELETE FROM store WHERE item = ?",(item,))
    conn.commit()
    conn.close() # close the connection

def update(item, quantity, price):
    conn = sqlite3.connect("lite.db") #establishing connection
    cur = conn.cursor() # creating cursor

    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?",(quantity,price,item))
    conn.commit()
    conn.close() # close the connection

create_table()
insert("Water Glass", 2, 20)
delete("Water Glass")
print(view())
update("Wine Glass", 3, 65)
print(view())