import sqlite3

class ProductDB:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL
            )
        """)

    def insert_product(self, id, name, price):
        self.cursor.execute("INSERT INTO products VALUES (?, ?, ?)", (id, name, price))
        self.conn.commit()

    def update_product(self, id, name, price):
        self.cursor.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (name, price, id))
        self.conn.commit()

    def delete_product(self, id):
        self.cursor.execute("DELETE FROM products WHERE id = ?", (id,))
        self.conn.commit()

    def select_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

# 샘플 데이터 생성
db = ProductDB('products.db')
for i in range(1, 11):
    db.insert_product(i, f'제품{i}', i * 10000)
