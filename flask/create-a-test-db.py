import sqlite3

# Connect to the SQLite database file (create it if it doesn't exist)
conn = sqlite3.connect('flask/db/name.db')
cursor = conn.cursor()

# Create a table to store the data if it doesn't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS EnrollmentData
                  (AgeGroup TEXT, Enrollment2020 INTEGER, Enrollment2021 INTEGER, Enrollment2022 INTEGER)''')

# Define the data to be inserted
data = [
    ('8-10', 25, 32, 34),
    ('11-13', 21, 27, 24),
    ('14-16', 22, 24, 25)
]

# Insert the data into the table
cursor.executemany('INSERT INTO EnrollmentData VALUES (?,?,?,?)', data)

# Commit the changes and close the connection
conn.commit()
conn.close()
