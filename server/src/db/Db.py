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
            #! Remove table drop in prod!!!
            self.conn.execute("DROP TABLE IF EXISTS apps")
            self.conn.commit()
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS apps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                spentTime REAL NOT NULL,
                endTime TEXT NOT NULL,
                startTime TEXT NOT NULL,
                mainTitle TEXT NOT NULL,
                subtitle1 TEXT NOT NULL,
                subtitle2 TEXT NOT NULL
                )
                """
            )
            self.conn.commit()  # Commit the table creation
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def insert_session_info(
        self,
        spentTime: timedelta,
        startTime: datetime,
        endTime: datetime,
        mainTitle: str,
        subtitle1: str,
        subtitle2: str,
    ):
        """Insert time and title into apps table"""
        try:
            self.cur.execute(
                "INSERT INTO apps(spentTime, startTime, endTime, mainTitle, subtitle1, subtitle2) VALUES(?, ?, ?, ?, ?, ?)",
                [spentTime, startTime, endTime, mainTitle, subtitle1, subtitle2],
            )
            self.conn.commit()  # Commit the insertion
            print("inserted successfully")
        except sqlite3.Error as e:
            print("Error while inserting", e)

    def get_all_session_info(self) -> list[tuple[str, str, str, str, str, str]]:
        """Retrieve all session info from time_calculation table"""

        try:
            self.cur.execute("SELECT * FROM apps ORDER BY mainTitle DESC")
            return self.cur.fetchall()
        except sqlite3.Error as e:
            print("Error at retirieve_all_session_info method, in Db.py ->", e)

    def get_session_info_by_id(self, params: list = None):
        """Retrieve session info by id"""

        if params is not None:
            try:
                self.cur.execute("SELECT * FROM apps WHERE id = ?", params)
                return self.cur.fetchall()
            except sqlite3.Error as e:
                print(e)
        else:
            raise Exception("No parameters provided")


Db = Database()
