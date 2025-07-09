from datetime import datetime
from Connection import conn
import sqlite3


class Database:
    def __init__(self):
        conn.cur.execute("DROP TABLE IF EXISTS apps")
        conn.cur.execute("DROP TABLE IF EXISTS time_calculation")
        conn.cur.execute(
            """
                        CREATE TABLE IF NOT EXISTS apps (
                        id INT ,
                        time TEXT,
                        title TEXT,
                        PRIMARY KEY (id)
                        )
                        """
        )
        conn.cur.execute(
            """
                        CREATE TABLE IF NOT EXISTS time_calculation (
                        id INT ,
                        time TEXT,
                        title TEXT,
                        PRIMARY KEY (id)
                        )
                        """
        )

    def insert_session_info(self, time: str, title: str):
        try:
            conn.cur.execute(
                "INSERT INTO time_calculation(time, title) VALUES(?, ?)", [time, title]
            )
            conn.conn.commit()
            print("inserted successfully")
        except sqlite3.Error as e:
            print(e)

    def insert_time_calculation_session_info(self, time: datetime, title: str):
        try:
            conn.cur.execute(
                "INSERT INTO time_calculation(time, title) VALUES(?, ?)", [time, title]
            )
            conn.conn.commit()
            print("inserted successfully)")
        except sqlite3.Error as e:
            print(e)

    def get_total_time(self):
        try:
            conn.cur.execute(
                "SELECT time FROM time_calculation ORDER BY time"
            )  # Ensure times are ordered
            times = conn.cur.fetchall()
            if not times or len(times) < 2:
                return None
            return datetime.fromisoformat(times[-1][0]) - datetime.fromisoformat(
                times[0][0]
            )
        except sqlite3.Error as e:
            raise print(f"Error at class: Db method: get_total_time -> {e}")


Db = Database()


Db.insert_session_info(datetime(2025, 7, 9, 10, 30, 0), "Maincraft")
Db.insert_session_info(datetime.now(), "Maincraft")

total_duration = Db.get_total_time()

print(total_duration)

# Format the timedelta for human readability
if total_duration:
    formatted_duration = str(total_duration).split(".")[0]  # Show days and larger units
else:
    formatted_duration = str(total_duration)  # Show hours, minutes, seconds
