import sqlite3


class DataBase:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    # Создание таблиц базы данных.
    def create_database(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users 
                                            (
                                            user_id INTEGER PRIMARY KEY
                                                AUTOINCREMENT
                                                NOT NULL
                                                UNIQUE,
                                            nickname STRING UNIQUE NOT NULL,
                                            attempts INTEGER NOT NULL,
                                            time INTEGER NOT NULL
                                            );""")

        except sqlite3.Error as error:
            return error

    def get_id_by_nickname(self, nickname):
        try:
            user_id = self.cursor.execute("SELECT user_id FROM users WHERE nickname = ?",
                                          (nickname,)).fetchall()
            return user_id
        except sqlite3.Error as error:
            return error

    def add_nickname(self, nickname):
        try:
            user_id = self.get_id_by_nickname(nickname)
            if not user_id:
                self.cursor.execute(
                    "INSERT INTO users (nickname, attempts, time) VALUES (?, ?, ?)",
                    (nickname, 1, 0))
                self.connection.commit()
                return True
        except sqlite3.Error as error:
            return error

    def increment_attempts(self, nickname):
        try:
            attempts = self.cursor.execute("SELECT attempts FROM users WHERE nickname = ?",
                                           (nickname,)).fetchall()
            if attempts:
                attempts += 1
                self.cursor.execute("UPDATE users SET attempts = ? WHERE nickname = ?",
                                    (attempts, nickname))
                self.connection.commit()
        except sqlite3.Error as error:
            return error

    def update_time(self, nickname, time):
        try:
            time_data = self.cursor.execute("SELECT time FROM users WHERE nickname = ?",
                                            (nickname,)).fetchall()
            if time_data:
                self.cursor.execute("UPDATE users SET time = ? WHERE nickname = ?", (time, nickname))
                self.connection.commit()
        except sqlite3.Error as error:
            return error
