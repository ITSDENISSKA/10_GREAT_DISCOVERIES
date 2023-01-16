import sqlite3


class DataBase:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    # Создание таблиц базы данных.
    def create_database(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                                            user_id INTEGER PRIMARY KEY
                                                AUTOINCREMENT
                                                NOT NULL
                                                UNIQUE,
                                            nickname STRING UNIQUE NOT NULL,
                                            count_of_incorrect_answers INTEGER NOT NULL,
                                            time INTEGER NOT NULL,
                                            passed INTEGER NOT NULL 
                                            );""")

        except sqlite3.Error as error:
            return error

    def get_user_id_by_nickname(self, nickname):
        try:
            user_id = self.cursor.execute("SELECT user_id FROM users WHERE nickname = ?",
                                          (nickname,)).fetchall()
            return user_id
        except sqlite3.Error as error:
            return error

    def add_nickname(self, nickname):
        try:
            user_id = self.get_user_id_by_nickname(nickname)
            if not user_id:
                self.cursor.execute(
                    "INSERT INTO users (nickname, count_of_incorrect_answers, time, passed) VALUES (?, ?, ?, ?)",
                    (nickname, 0, 0, 0))
                self.connection.commit()
                return True
        except sqlite3.Error as error:
            return error

    def increment_count_of_incorrect_answers_by_nickname(self, nickname):
        try:
            count_of_incorrect_answers = \
                self.cursor.execute("SELECT count_of_incorrect_answers FROM users WHERE nickname = ?",
                                    (nickname,)).fetchone()[0]
            count_of_incorrect_answers += 1
            self.cursor.execute("UPDATE users SET count_of_incorrect_answers = ? WHERE nickname = ?",
                                (count_of_incorrect_answers, nickname))
            self.connection.commit()

        except sqlite3.Error as error:
            return error


    def update_time_by_nickname(self, nickname, time):
        try:
            self.cursor.execute("UPDATE users SET time = ? WHERE nickname = ?", (time, nickname))
            self.connection.commit()
        except sqlite3.Error as error:
            return error


    def get_statistic(self):
        try:
            statistic = self.cursor.execute(
                "SELECT nickname, time, count_of_incorrect_answers, passed FROM users ORDER BY time ASC").fetchall()
            return statistic
        except sqlite3.Error as error:
            return error


    def get_count_of_incorrect_answers_by_nickname(self, nickname):
        try:
            count_of_incorrect_answers = self.cursor.execute(
                "SELECT count_of_incorrect_answers FROM users WHERE nickname = ?", (nickname,)).fetchone()
            return count_of_incorrect_answers[0]

        except sqlite3.Error as error:
            return error


    def set_passed_game_by_nickname(self, nickname):
        try:
            self.cursor.execute("UPDATE users SET passed = 1 WHERE nickname = ?", (nickname,))
            self.connection.commit()
        except sqlite3.Error as error:
            return error


    def get_time_by_nickname(self, nickname):
        time = self.cursor.execute("SELECT time FROM users WHERE nickname = ?", (nickname,)).fetchone()
        return time[0]
