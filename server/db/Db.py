import datetime
from .Connection import conn
import sqlite3

class Database:
    def __init__(self):
        conn.cur.execute('DROP TABLE IF EXISTS apps')
        conn.cur.execute('''
                        CREATE TABLE apps (
                        id INT AUTO_INCREMENT,
                        time DATETIME,
                        title TEXT,
                        PRIMARY KEY (id)
                        )
                        ''')

    def insert_session_info(self, time:str, title: str):
        try:
            conn.cur.execute('INSERT INTO apps(time, title) VALUES(?, ?)', [time, title])
            conn.conn.commit()
            print('inserted successfully')
        except sqlite3.Error as e:
            print(e)

    def insert_title_session_info(self, title:str):
        try:
            conn.cur.execute('INSERT INTO apps(title) VALUES(?)', [title])
            conn.conn.commit()
            print('inserted successfully)')
        except sqlite3.Error as e:
            print(e)

    def get_last_title(self): # retrieve last window title
        try:
            conn.cur.execute('SELECT * FROM apps LIMIT 1')
            data = conn.cur.fetchone()
            print(data)
            return data
        except sqlite3.Error as e:
            print(e)

    def get_total_time(self):
        pass

Db = Database()




# Db.insert_session_info(
#   datetime.datetime.now(),
#   'Maincraft'
# )
# Db.insert_session_info(
#   datetime.datetime.now(),
#   'Maincraft'
# )

# total_duration = Db.get_total_time()

# # Format the timedelta for human readability
# if total_duration:
#     formatted_duration = str(total_duration).split(".")[0]  # Show days and larger units
# else:
#     formatted_duration = str(total_duration)  # Show hours, minutes, seconds

# print(f"Total duration: {formatted_duration}")