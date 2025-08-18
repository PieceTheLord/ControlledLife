from datetime import datetime
import sqlite3
import threading

class Database:
    def __init__(self):
        # DO NOT DROP TABLES HERE IN PRODUCTION
        # This is only for development/testing
        # self.conn.execute.execute("DROP TABLE IF EXISTS apps")
        # self.conn.execute.execute("DROP TABLE IF EXISTS time_calculation")
        self.conn = sqlite3.connect("apps.db")
        self.cur = self.conn.cursor()
        # Database dev mode updating
        try:
            self.cur.execute(
                """
                CREATE TABLE IF NOT EXISTS apps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time TEXT NOT NULL,
                title TEXT NOT NULL,
                date TEXT NOT NULL
                )
                """
            )
            self.cur.execute(
                """
                CREATE TABLE IF NOT EXISTS time_calculation (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time TEXT NOT NULL,
                title TEXT NOT NULL
                )
                """
            )
            self.conn.commit()  # Commit the table creation
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def insert_session_info(self, time: str, title: str):
        """Insert time and title into apps table"""
        try:
            self.cur.execute(
                "INSERT INTO apps(time, title, date) VALUES(?, ?, ?)",
                [time, title, datetime.now().strftime("%Y-%m-%d")],
            )
            self.conn.commit()  # Commit the insertion
            print("inserted successfully")
        except sqlite3.Error as e:
            print("Error while inserting", e)

    def insert_time_calculation_session_info(self, time: datetime, title: str):
        """Insert time calculation data into time_calculation table"""
        try:
            self.cur.execute(
                "INSERT INTO time_calculation(time, title) VALUES(?, ?)", [time, title]
            )
            self.conn.commit()  # Commit the insertion
            print("inserted successfully)")
        except sqlite3.Error as e:
            print("Error in insert_time_calculation_session_info method, Db.py ->", e)

    def calculate_time_difference(self):
        """Calculate the time difference, after process change"""
        try:

            self.cur.execute(
                "SELECT time FROM time_calculation ORDER BY time"
            )  # Ensure times are ordered
            times = self.cur.fetchall()
            if not times or len(times) < 2:
                return None
            return datetime.fromisoformat(times[-1][0]) - datetime.fromisoformat(
                times[0][0]
            )
        except sqlite3.Error as e:
            print(f"Error at class: Db method: calculate_time_difference -> {e}")
            return None  # Added return None in case of exception

    def insert_session_time():
        """#TODO: Implement this method or remove"""
        pass

    def get_all_session_info(self):
        """Retrieve all session info from time_calculation table"""

        try:
            self.cur.execute("SELECT * FROM time_calculation")
            return self.cur.fetchall()
        except sqlite3.Error as e:
            print("Error at retirieve_all_session_info method, in Db.py ->", e)


Db = Database()
