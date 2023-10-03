import psycopg2



def create_table():
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ") #establishing connection
    cur = conn.cursor() # creating cursor

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # execute sql commands

    cur.execute("INSERT INTO store VALUES ('Wine Glass', 2, 110)")
    conn.commit() # commit the connection
    conn.close() # close the connection

def insert(item, qty, price):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ") #establishing connection
    cur = conn.cursor() # creating cursor

    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, qty, price))
    conn.commit() # commit the connection
    conn.close() # close the connection

def view():
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ") #establishing connection
    cur = conn.cursor() # creating cursor

    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close() # close the connection
    return rows

def delete(item):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ") #establishing connection
    cur = conn.cursor() # creating cursor

    cur.execute("DELETE FROM store WHERE item = %s",(item,))
    conn.commit()
    conn.close() # close the connection

def update(item, quantity, price):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ") #establishing connection
    cur = conn.cursor() # creating cursor

    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s",(quantity,price,item))
    conn.commit()
    conn.close() # close the connection

create_table()
insert("Water Glass", 2, 20)
delete("Wine Glass")
# print(view())
update("Wine Glass", 3, 65)
print(view())