from datetime import datetime
from .Connection import conn
import sqlite3


class Database:
    def __init__(self):
        conn.cur.execute("DROP TABLE IF EXISTS apps")
        conn.cur.execute("DROP TABLE IF EXISTS time_calculation")
        conn.cur.execute(
            """
                        CREATE TABLE IF NOT EXISTS apps (
                        id INT ,
                        time TEXT NOT NULL,
                        title TEXT NOT NULL,
                        date TEXT NOT NULL,
                        PRIMARY KEY (id)
                        )
                        """
        )
        conn.cur.execute(
            """
                        CREATE TABLE IF NOT EXISTS time_calculation (
                        id INT,
                        time TEXT NOT NULL,
                        title TEXT NOT NULL,
                        PRIMARY KEY (id)
                        )
                        """
        )

    def insert_session_info(self, time: str, title: str):
        """Insert time and title into apps tabel"""
        try:
            conn.cur.execute(
                "INSERT INTO apps(time, title) VALUES(?, ?)", [time, title]
            )
            conn.conn.commit()
            print("inserted successfully")
        except sqlite3.Error as e:
            print("Error while inserting", e)

    def insert_time_calculation_session_info(self, time: datetime, title: str):
        """Insert time calculation data into time_calculation tabel"""
        try:
            conn.cur.execute(
                "INSERT INTO time_calculation(time, title) VALUES(?, ?)", [time, title]
            )
            conn.conn.commit()
            print("inserted successfully)")
        except sqlite3.Error as e:
            print(e)

    def calculate_time_difference(self):
        """Calculate the time difference, after process change"""
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
            raise print(f"Error at class: Db method: calculate_time_difference -> {e}")
    def insert_session_time():
        pass


Db = Database()


# Db.insert_session_info(datetime(2025, 7, 14, 9, 30, 0), "Maincraft")
# Db.insert_session_info(datetime.now(), "Maincraft")

# total_duration = Db.calculate_time_difference()

# print(f"total_duration: {total_duration}")


