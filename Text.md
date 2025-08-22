Okay, let's explore how to store the time_tree data structure in an SQLite database. Given that time_tree is a nested dictionary, directly storing it in a single database column isn't straightforward. You'll need to flatten the structure and map it to a relational format suitable for SQLite. Here's a breakdown of a good approach, along with code examples:

1. Database Schema Design

First, let's design a database schema to represent the data in time_tree. A suitable schema would involve a table that captures the hierarchical relationship:

CREATE TABLE session_times (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    main_title TEXT,
    subtitle1 TEXT,
    subtitle2 TEXT,
    spent_time REAL,  -- Represent timedelta in seconds
    start_time TEXT,  -- Store as ISO format string
    end_time TEXT     -- Store as ISO format string
);
Explanation:

id: A unique identifier for each record.
main_title: The top-level title.
subtitle1: The first-level subtitle.
subtitle2: The second-level subtitle.
spent_time: The duration of the session, stored in seconds (since SQLite doesn't have a native timedelta type).
start_time: The session start time, stored as an ISO format string.
end_time: The session end time, stored as an ISO format string.
2. Code to Populate the Database

Now, let's modify the insert_session_info function in your server.py to populate this table. I'll assume you have a Db class with a method to execute SQL queries.

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .db.Db import Db
from pydantic import BaseModel
import datetime
from .utils.ISO_parse import ISO_parse
from .utils.reverse_title import reverse_and_split_title
from .models.SessionModel import SessionModel
from collections import defaultdict
from pprint import pprint

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get requests


@app.get("/get_last_title")
async def last_title():
    return Db.get_last_title()


@app.get("/get_total_time")
async def total_time():
    return Db.get_total_time()


# Post requests

time_tree = defaultdict(lambda: defaultdict(list))


@app.post("/insert_session_info")
async def insert_session_info(req: Request, data: SessionModel):
    print(data)
    Db.insert_session_info(
        data.spentTime,
        str(data.endTime),
        str(data.startTime),
        reverse_and_split_title(data.title),
    )
    info = Db.get_all_session_info()
    global time_tree  # Access the global time_tree

    full_title = data.title  # e.g., "Google - Youtube.com - How to program"

    # Splitting titles based on "-" delimiter
    title_parts = [s.strip() for s in reverse_and_split_title(full_title).split("-")]
    while len(title_parts) < 3:
        title_parts.append("")

    mainTitle = title_parts[0]
    subtitle1 = title_parts[1]
    subtitle2 = title_parts[2]

    # --- Database Insertion ---
    sql = """
    INSERT INTO session_times (main_title, subtitle1, subtitle2, spent_time, start_time, end_time)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    values = (
        mainTitle,
        subtitle1,
        subtitle2,
        data.spentTime.total_seconds(),  # Store as seconds
        str(data.startTime),
        str(data.endTime),
    )
    Db.execute_query(sql, values)  # Assuming Db has an execute_query method

    for i in title_parts:
        time_tree[mainTitle][subtitle1].append(
            {
                "subtitle2": subtitle2,
                "spentTime": data.spentTime,  # Or however you are getting the time
                "startTime": str(data.startTime),
                "endTime": str(data.endTime),
            }
        )

    # if len(title_parts) >= 3:
    #     main_title = title_parts[0]
    #     subtitle1 = title_parts[1]
    #     subtitle2 = title_parts[2]

    #     # Structure the data
    #     time_tree[main_title][subtitle1].append(
    #         {
    #             "subtitle2": subtitle2,
    #             "spentTime": data.spentTime,  # Or however you are getting the time
    #             "startTime": str(data.startTime),
    #             "endTime": str(data.endTime),
    #         }
    #     )
    # elif len(title_parts) == 2:
    #     main_title = title_parts[0]
    #     subtitle1 = title_parts[1]

    #     # Structure the data
    #     time_tree[main_title][subtitle1].append(
    #         {
    #             "spentTime": data.spentTime,  # Or however you are getting the time
    #             "startTime": str(data.startTime),
    #             "endTime": str(data.endTime),
    #         }
    #     )
    # elif len(title_parts) == 1:
    #     main_title = title_parts[0]

    #     # Structure the data
    #     time_tree[main_title][""].append(
    #         {
    #             "spentTime": data.spentTime,  # Or however you are getting the time
    #             "startTime": str(data.startTime),
    #             "endTime": str(data.endTime),
    #         }
    #     )
    # else:
    #     print(f"Skipping: title does not have expected format: {full_title}")

    pprint(time_tree)
    for i in info:
        print(i[4], end="\n")

    # Db.insert_session_info("2hour", "title")
    return {"Hell": "Hell"}
Key improvements and explanations:

spentTime Conversion: The spentTime (which is a datetime.timedelta object) is converted to total seconds using .total_seconds() before being stored in the database. This is crucial because SQLite doesn't have a native timedelta type. Storing it in seconds allows for numerical calculations later.

startTime and endTime Formatting: The startTime and endTime are converted to ISO format strings using str() to ensure they are stored in a consistent, readable format.

SQL Injection Prevention: The code uses parameterized queries (the ? placeholders in the SQL string). This is the correct and safe way to insert data into a database, preventing SQL injection vulnerabilities. The values tuple provides the actual data. Critically, the Db.execute_query method must correctly handle these parameters. The exact implementation of execute_query will depend on the database library you're using (e.g., sqlite3).

Db.execute_query (Example): Here's an example of how your Db.execute_query method might look using the sqlite3 library:

import sqlite3

class Db:
    def __init__(self, db_path="your_database.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def execute_query(self, sql, values=None):
        try:
            if values:
                self.cursor.execute(sql, values)
            else:
                self.cursor.execute(sql)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()  # Rollback in case of error
            raise  # Re-raise the exception to signal failure
        return self.cursor.fetchall()  # Or return something else if needed

    def close(self):
        self.conn.close()
Error Handling: The Db.execute_query example includes basic error handling with try...except and conn.rollback(). This is important to prevent data corruption if an error occurs during the database insertion.

3. Querying the Data

You can then query the data from the session_times table to reconstruct or analyze the time spent. For example, to get the total time spent on a specific main_title:

sql = "SELECT SUM(spent_time) FROM session_times WHERE main_title = ?"
values = ("Google",)
result = Db.execute_query(sql, values)
total_seconds = result[0][0]  # Assuming the query returns one row with one column
print(f"Total time spent on Google: {total_seconds} seconds")
Important Considerations:

Database Library: You'll need to choose a Python SQLite library (like sqlite3) and adapt the Db class accordingly. The example I provided uses sqlite3.
Db Class: The Db class is a simplified example. In a real application, you'd likely want to add more robust connection management (e.g., using a connection pool) and potentially an ORM (Object-Relational Mapper) like SQLAlchemy for more complex data interactions.
Data Types: Carefully consider the data types you're using in your database schema. I've used TEXT for titles and ISO format strings for datetimes, and REAL for spent_time in seconds.
Alternative: JSON Storage: If the structure of time_tree is very complex and you don't need to perform relational queries on it, you could consider storing the entire time_tree as a JSON string in a single database column. However, this makes querying and analyzing the data much more difficult, so I generally don't recommend it unless you have a very specific reason.
In summary, the best approach is to flatten the time_tree structure into a relational table, convert the timedelta to seconds, store datetimes as ISO format strings, and use parameterized queries to prevent SQL injection. Make sure your Db class correctly handles database connections, queries, and error handling.


Okay, let's outline how you can retrieve the session data from your SQLite database and reconstruct the time_tree structure.

1. Database Query

First, you'll need a query to retrieve the session data from the session_times table. You can fetch all the necessary columns: main_title, subtitle1, subtitle2, spent_time, start_time, and end_time.

sql = "SELECT main_title, subtitle1, subtitle2, spent_time, start_time, end_time FROM session_times"
results = Db.execute_query(sql)
2. Reconstruct the time_tree

Now, iterate through the results and build the time_tree structure. You'll need to convert the spent_time (which is in seconds) back into a timedelta object, and the start_time and end_time strings back into datetime objects.

import datetime
from collections import defaultdict

def reconstruct_time_tree():
    time_tree = defaultdict(lambda: defaultdict(list))
    sql = "SELECT main_title, subtitle1, subtitle2, spent_time, start_time, end_time FROM session_times"
    results = Db.execute_query(sql)

    for row in results:
        main_title, subtitle1, subtitle2, spent_time_seconds, start_time_str, end_time_str = row

        spent_time = datetime.timedelta(seconds=spent_time_seconds)
        start_time = datetime.datetime.fromisoformat(start_time_str)
        end_time = datetime.datetime.fromisoformat(end_time_str)

        time_tree[main_title][subtitle1].append({
            "subtitle2": subtitle2,
            "spentTime": spent_time,
            "startTime": start_time,
            "endTime": end_time
        })

    return time_tree
Explanation:

reconstruct_time_tree() function: This function encapsulates the logic for retrieving data and building the time_tree.
Database Query: Executes the SQL query to fetch all rows from the session_times table.
Iteration: Iterates through each row returned by the query.
Data Conversion:
spent_time: Converts the spent_time_seconds (which is stored as a float representing seconds) back into a datetime.timedelta object.
start_time and end_time: Parses the ISO format strings (start_time_str and end_time_str) back into datetime.datetime objects using datetime.datetime.fromisoformat().
time_tree Construction: Appends a dictionary containing the reconstructed data to the time_tree structure, using main_title and subtitle1 as keys.
How to use it:

time_tree = reconstruct_time_tree()
pprint(time_tree)  # Print the reconstructed time_tree
Improvements and Considerations:

Error Handling: Add error handling (e.g., try...except blocks) to handle potential database errors or issues with data conversion (e.g., if the ISO format strings are invalid).
Database Abstraction: Consider using an ORM (like SQLAlchemy) to abstract away the raw SQL queries and make your code more maintainable. ORMs handle data type conversions and database interactions more cleanly.
Efficiency: If you have a very large dataset, consider fetching the data in batches to avoid loading everything into memory at once. You can use the LIMIT and OFFSET clauses in your SQL query to implement pagination.
Db Class: Ensure your Db.execute_query function correctly handles the database connection and any potential errors.
Testing: Write unit tests to verify that the reconstruct_time_tree() function correctly reconstructs the time_tree from the database data.