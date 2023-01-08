import sqlite3


class DataBase:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    # Создание таблиц базы данных.
    def create_database(self) -> sqlite3.OperationalError:
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY 
                AUTOINCREMENT 
                NOT NULL 
                UNIQUE,
            nickname STRING UNIQUE NOT NULL,
            password STRING NOT NULL
            );""")

        except sqlite3.Error as error:
            return error

        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY 
                AUTOINCREMENT 
                NOT NULL 
                UNIQUE,
            score INTEGER NOT NULL,
            user_id INTEGER NOT NULL UNIQUE,
            FOREIGN KEY (user_id) REFERENCES users (id)
            );""")

        except sqlite3.Error as error:
            return error

        try:
            self.connection.close()
        except sqlite3.Error as error:
            return error