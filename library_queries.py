
import sqlite3

# Create the library database
conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Create the books table
cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price REAL,
    stock INTEGER
)
""")

# Insert sample books
cur.execute("DELETE FROM books")

books = [
    (1, "Data Science Basics", "Technology", 1450, 10),
    (2, "Clean Code", "Technology", 1200, 7),
    (3, "The Silent Patient", "Fiction", 1350, 2),
    (4, "Python Programming", "Technology", 950, 8),
    (5, "The Alchemist", "Fiction", 850, 3),
    (6, "Database Systems", "Education", 1100, 6),
    (7, "Pride and Prejudice", "Fiction", 750, 4),
    (8, "Artificial Intelligence", "Technology", 1800, 9)
]

cur.executemany(
    "INSERT INTO books VALUES (?, ?, ?, ?, ?)",
    books
)
conn.commit()

# Query 1: Books priced above Rs. 1000
print("Books above Rs.1000 (sorted):")
cur.execute("""
SELECT title, price
FROM books
WHERE price > 1000
ORDER BY price DESC
""")
for row in cur.fetchall():
    print(row)

# Query 2: Rename title using AS
print("\nBook titles with aliases:")
cur.execute("""
SELECT title AS book_title, price
FROM books
ORDER BY title
""")
for row in cur.fetchall():
    print(row)

# Query 3: Low-stock Fiction books
print("\nLow-stock Fiction books:")
cur.execute("""
SELECT title, genre, price, stock
FROM books
WHERE genre = 'Fiction' AND stock < 5
""")
for row in cur.fetchall():
    print(row)

conn.close()
print("\nDatabase queries completed.")