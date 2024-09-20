import sqlite3

def database_connection():
  conn = None
  try:
    conn = sqlite3.connect('apps.db')
    print("Connected successfully")
  except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")

  return conn
    
conn = database_connection()

conn.execute('''
             DROP TABLE IF EXISTS apps;
             ''')

conn.execute('''
             CREATE TABLE  apps (
             id int Primary Key,
             time text,
             window_title text
             )
             ''')

if conn:
  conn.close()
