import sqlite3
import os


class LoginDataBase:
    def __init__(self, name="login.db") -> None:
        database_folder = "databases"
        os.makedirs(database_folder, exist_ok=True)
        db_path = os.path.join(database_folder, name)
        self.name = db_path
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        if isinstance(exc_val, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def create_table_users(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS 'users'(
            'user_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'name' TEXT NOT NULL UNIQUE,
            'password_hash' TEXT NOT NULL,
            'email' TEXT NOT NULL UNIQUE,
            'last_login' TEXT NOT NULL,
            'accept_emails' INT NOT NULL
            );
            """)

    def create_table_databases(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS 'databases'(
            'database_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'user_id' INTEGER NOT NULL,
            FOREIGN KEY ('user_id') REFERENCES 'users'('user_id')
            );
            """)

    def setup_database(self):
        self.create_table_users()
        self.create_table_databases()

    def insert_user(self, name, password_hash, email, accept_emails, last_login='nunca logado'):
        # Se retornar False o usuário já está cadastrado, caso contrário retorna True
            self.cursor.execute(
                """
                SELECT * FROM users WHERE email=? OR name=?
                """, (email, name)
            )

            result = self.cursor.fetchone()

            if result:
                return False

            self.cursor.execute(
                """
                INSERT INTO users(name, password_hash, email, last_login, accept_emails) VALUES(?, ?, ?, ?, ?);
                """, (name, password_hash, email, last_login, accept_emails)
            )
            self.insert_database(email)

            return True

    def select_last_user_id(self):
        self.cursor.execute("SELECT last_insert_rowid()")
        last_user_id = self.cursor.fetchone()[0]

        return last_user_id


    def update_last_login(self, date, user_id):
        self.cursor.execute(
            """
            UPDATE users 
            SET last_login=? 
            WHERE user_id=?
            """, (date, user_id)
        )

    def insert_database(self, email):
        self.cursor.execute(
            """
            SELECT user_id FROM users WHERE email=?
            """, (email,)
          )

        result = self.cursor.fetchone()

        self.cursor.execute(
            """
            INSERT INTO databases (user_id) VALUES(?);
            """, (result[0],)
            )

    def check_login(self, username, password_hash):
        self.cursor.execute(
            """
            SELECT * FROM users WHERE name=? and password_hash=?
            """, (username, password_hash))

        result = self.cursor.fetchone()
        if not result:
            return False
        return True




class SystemDataBase:
    def __init__(self, name="system.db") -> None:
        database_folder = "databases"
        os.makedirs(database_folder, exist_ok=True)
        db_path = os.path.join(database_folder, name)
        self.name = db_path
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        if isinstance(exc_val, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def create_table_users(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS 'users'(
            'user_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'name' TEXT NOT NULL UNIQUE,
            'password_hash' TEXT NOT NULL,
            'email' TEXT NOT NULL UNIQUE,
            'last_login' TEXT NOT NULL UNIQUE,
            'accept_emails' INT NOT NULL
            );
            """)

    def create_table_messages(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS 'messages'(
            'message_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'message_path' TEXT NOT NULL UNIQUE
            );
            """)

    def create_table_recipients(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS 'recipients'(
            'recipient_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'name' TEXT NOT NULL,
            'email' TEXT NOT NULL UNIQUE,
            'age' TEXT NULL,
            'sex' TEXT NULL,
            'country_code' TEXT NULL
            );
            """)

    def create_table_log_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS 'log_table'(
            'log_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'timestamp' TEXT NOT NULL,
            'event_type' TEXT NOT NULL,
            'description' TEXT NOT NULL,
            'code' TEXT NOT NULL
            );
            """)

    def setup_database(self):
        self.create_table_users()
        self.create_table_recipients()
        self.create_table_log_table()
        self.create_table_messages()
