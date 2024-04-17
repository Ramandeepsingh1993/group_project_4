import pandas as pd  
import sqlite3

conn = sqlite3.connect('food.db')  # Connect to SQLite database
cursor = conn.cursor()


df = pd.read_csv("onlinefoods.csv")

# Insert Data into SQLite Database

df.to_sql('food', conn, if_exists='append', index=False)

# Commit the transaction
conn.commit()

cursor.execute('''SELECT * FROM food''')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)


#Convert SQLite data to Pandas DataFrame
df = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])



#View Data
print(df)