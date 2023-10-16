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

    def check_logged_user_id(self, username, password_hash):
        self.cursor.execute(
            """
            SELECT user_id FROM users WHERE name=? and password_hash=?
            """, (username, password_hash))

        result = self.cursor.fetchone()
        if not result:
            return False
        return result[0]


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
            'path' TEXT NOT NULL UNIQUE,
            'name' TEXT NOT NULL UNIQUE
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

    def create_table_campaigns(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS 'campaigns'(
            'campaign_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'week_day' TEXT NOT NULL,
            'time' TEXT NOT NULL,
            'sex' TEXT NOT NULL,
            'age' INTEGER,
            'country_code' TEXT,
            'message_id' INTEGER NOT NULL,
            'type' TEXT NOT NULL,
            'answer' TEXT,
            FOREIGN KEY ('message_id') REFERENCES 'messages'('message_id') 
            );
            """)

    def insert_campaign(self, day, time, message_id, type, country='null', answer='null', sex='null', age='null'):
        self.cursor.execute(
            """
            INSERT INTO campaigns(week_day, time, sex, age, country_code, message_id, type, answer) 
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
            """, (day, time, sex, age, country, message_id, type, answer)

        )

    def select_campaign(self):
        self.cursor.execute(
            """
            SELECT * FROM campaigns
            """
        )
        result = self.cursor.fetchall()
        return result





    def create_table_smtp(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS 'smtp'(
            'smtp_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'server' TEXT NOT NULL,
            'port' TEXT NOT NULL,
            'email' TEXT NOT NULL,
            'password' TEXT NOT NULL
            )
            """)

    def create_table_imap(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS 'imap'(
            'imap_id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'server' TEXT NOT NULL,
            'port' TEXT NOT NULL,
            'email' TEXT NOT NULL,
            'password' TEXT NOT NULL
            )
            """)

    def insert_smtp(self, server, port, email, password):
        self.cursor.execute(
            """
            REPLACE INTO smtp(server, port, email, password) VALUES(?, ?, ?, ?)
            """, (server, port, email, password))

    def insert_imap(self, server, port, email, password):
        self.cursor.execute(
            """
            REPLACE INTO imap(server, port, email, password) VALUES(?, ?, ?, ?)
            """, (server, port, email, password))

    def insert_recipient(self, name, email, age, sex, country_code):
        self.cursor.execute(
            """
            INSERT OR REPLACE INTO recipients(name, email, age, sex, country_code) VALUES(?, ?, ?, ?, ?)
            """, (name, email, age, sex, country_code))

    def select_message_byname(self, name):
        self.cursor.execute(
            """
            SELECT path FROM messages WHERE name=?
            """, (name,))

        result = self.cursor.fetchone()
        if not result:
            return False
        return result[0]

    def select_message_bypath(self, path):
        self.cursor.execute(
            """
            SELECT message_id FROM messages WHERE path=?
            """, (path,))

        result = self.cursor.fetchone()
        if not result:
            return False
        return result[0]

    def select_message_by_id(self, id):
        self.cursor.execute(
            """
            SELECT name FROM messages WHERE message_id=?
            """, (id,))
        result = self.cursor.fetchone()
        if not result:
            return False
        return result[0]

    def insert_message(self, path, name):
        self.cursor.execute(
            """
            INSERT OR REPLACE INTO messages(path, name) VALUES(?, ?)
            """, (path, name))

        last_id = self.cursor.lastrowid

        return last_id

    def delete_message(self, name):
        self.cursor.execute(
            """
            DELETE FROM messages WHERE name=?
            """, (name,)
        )

    def select_all_messages(self):
        self.cursor.execute(
            """
            SELECT * FROM messages
            """)
        result = self.cursor.fetchall()
        return result

    def select_recipients(self):
        self.cursor.execute(
            """
            SELECT name, email FROM recipients;
            """)
        result = self.cursor.fetchall()
        return result

    def select_smtp(self):
        self.cursor.execute(
            """
            SELECT server, port, email, password FROM smtp;
            """)
        result = self.cursor.fetchone()
        return result

    def select_imap(self):
        self.cursor.execute(
            """
            SELECT server, port, email, password FROM imap;
            """)
        result = self.cursor.fetchone()
        return result


    def setup_database(self):
        self.create_table_users()
        self.create_table_recipients()
        self.create_table_log_table()
        self.create_table_messages()
        self.create_table_campaigns()
        self.create_table_smtp()
        self.create_table_imap()
