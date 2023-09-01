import sqlite3
import json

# JSON data
json_data = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
        "genres": ["Fiction", "Classics"]
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_year": 1960,
        "genres": ["Fiction", "Classics"]
    }
]

# Create an SQLite database
conn = sqlite3.connect('books.sqlite')
cursor = conn.cursor()

# Create the 'books' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        published_year INTEGER
    )
''')

# Create the 'genres' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS genres (
        id INTEGER PRIMARY KEY,
        book_id INTEGER,
        genre TEXT
    )
''')

# Insert data into 'books' and 'genres' tables
for book in json_data:
    cursor.execute('''
        INSERT INTO books (title, author, published_year)
        VALUES (?, ?, ?)
    ''', (book['title'], book['author'], book['published_year']))
    
    book_id = cursor.lastrowid  # Get the last inserted row's ID
    
    for genre in book['genres']:
        cursor.execute('''
            INSERT INTO genres (book_id, genre)
            VALUES (?, ?)
        ''', (book_id, genre))

# Commit changes and close the connection
conn.commit()
conn.close()
