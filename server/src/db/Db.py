from datetime import datetime, timedelta
import sqlite3
import threading


class Database:
    def __init__(self):
        # DO NOT DROP TABLES HERE IN PRODUCTION
        # This is only for development/testing
        self.conn = sqlite3.connect("apps.db")
        self.cur = self.conn.cursor()
        # Database dev mode updating
        try:
            self.conn.execute("DROP TABLE IF EXISTS apps")
            self.conn.commit()
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS apps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                spentTime TEXT NOT NULL,
                endTime TEXT NOT NULL,
                startTime TEXT NOT NULL,
                title TEXT NOT NULL
                )
                """
            )
            self.conn.commit()  # Commit the table creation
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def insert_session_info(
        self, spentTime: timedelta, startTime: datetime, endTime: datetime, title: str
    ):
        """Insert time and title into apps table"""
        try:
            self.cur.execute(
                "INSERT INTO apps(spentTime, startTime, endTime, title) VALUES(?, ?, ?, ?)",
                [spentTime, startTime, endTime, title],
            )
            self.conn.commit()  # Commit the insertion
            print("inserted successfully")
        except sqlite3.Error as e:
            print("Error while inserting", e)

    def insert_session_time():
        """#TODO: Implement this method or remove"""
        pass

    def get_all_session_info(self):
        """Retrieve all session info from time_calculation table"""

        try:
            self.cur.execute("SELECT title FROM apps ORDER BY title DESC")
            return self.cur.fetchall()
        except sqlite3.Error as e:
            print("Error at retirieve_all_session_info method, in Db.py ->", e)


Db = Database()