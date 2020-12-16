import sqlite3


class DbFilms:
    def __init__(self):
        self.conn = sqlite3.connect('DataBase.bd')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS Films(id integer primary key, Title text, Genre text, Age text, Description 
            text, Visual text)''')
        self.conn.commit()

    def insert_data(self, Title, Genre, Age, Description, Visual):
        self.c.execute(
            '''INSERT INTO Films(Title, Genre, Age, Description, Visual)
            VALUES (?, ?, ?, ?, ?)''',
            (Title, Genre, Age, Description, Visual)
        )
        self.conn.commit()


class DbSessions:
    def __init__(self):
        self.conn = sqlite3.connect('DataBase.bd')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS Sessions(id integer primary key, Title text, Date text, Time text, 
            Tickets text, Tickets_sold_out text)''')
        self.conn.commit()

    def insert_data(self, Title, Date, Time, Tickets, Tickets_sold_out):
        self.c.execute(
            '''INSERT INTO Sessions(Title, Date, Time, Tickets, Tickets_sold_out)
            VALUES (?, ?, ?, ?, ?)''',
            (Title, Date, Time, Tickets, Tickets_sold_out)
        )
        self.conn.commit()

class DbHall:
    def __init__(self):
        self.conn = sqlite3.connect('DataBase.bd')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS Hall(id integer primary key, Title text, FirstColumn text, SecondColumn text, 
            ThirdColumn text, FourthColumn text)''')
        self.conn.commit()

    def insert_data(self, Title, FirstColumn, SecondColumn, ThirdColumn, FourthColumn):
        self.c.execute(
            '''INSERT INTO Hall( Title, FirstColumn, SecondColumn, ThirdColumn, FourthColumn)
            VALUES (?, ?, ?, ?, ?)''',
            (Title, FirstColumn, SecondColumn, ThirdColumn, FourthColumn)
        )
        self.conn.commit()
