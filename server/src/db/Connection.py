import sqlite3 

class Connection:
  def __init__(self):
    self.conn = sqlite3.connect('apps.db')
    self.cur = self.conn.cursor()


conn = Connection()
