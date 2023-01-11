import sqlite3


class DataBase:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    # Создание таблиц базы данных.
    def create_database(self) -> sqlite3.OperationalError:
        try:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users (\n"
                                "            user_id INTEGER PRIMARY KEY \n"
                                "                AUTOINCREMENT \n"
                                "                NOT NULL \n"
                                "                UNIQUE,\n"
                                "            nickname STRING UNIQUE NOT NULL,\n"
                                "            score INTEGER NOT NULL,\n"
                                "            time INTEGER NOT NULL,\n"
                                "            );")

        except sqlite3.Error as error:
            return error

        try:
            self.connection.close()
        except sqlite3.Error as error:
            return error
