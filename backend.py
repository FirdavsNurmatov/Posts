from mysql.connector import Error

import mysql.connector

class Database:
    def __init__(self):
        self.connect()

    def connect(self):
        self.connecttion = mysql.connector.connect(
            host = 'localhost',
            username = 'root',
            password = 'root',
            database = 'exam'
        )

    def add_user(self, user: dict) -> bool:
        try:
            self.connect()
            with self.connecttion.cursor() as cursor:
                query = "INSERT INTO users  (full_name, phone_number, username, password) VALUE (%s, %s, %s, %s)"
                cursor.execute(query, (user['full_name'], user['phone_number'], user['username'], user['password']))
                self.connecttion.commit()
                cursor.close()
                return True
        except Error:
            return False
        
    def check_user(self, user: dict) -> str:
        try:
            self.connect()
            with self.connecttion.cursor() as cursor:
                query = """
                    SELECT id FROM users
                    WHERE username = %s AND password = %s
                """
                cursor.execute(query, (user['username'], user['password']))
                data = cursor.fetchone()
                cursor.close()
                if data:
                    return data[0]
                return 'empty'
        except Error:
            return 'err'
        
    def bring_all_comments(self):
        try:
            self.connect()
            with self.connecttion.cursor() as cursor:
                query = """
                    SELECT username, comment, date FROM comments
                    ORDER BY date DESC
                """
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                if data:
                    return data
                return ''
        except Error:
            return ''

    def bring_my_comments(self, data: str):
        try:
            self.connect()
            with self.connecttion.cursor() as cursor:
                query = """
                    SELECT username, comment, date FROM comments
                    WHERE username = %s
                    ORDER BY date DESC
                """
                cursor.execute(query,(data,))
                data = cursor.fetchall()
                cursor.close()
                if data:
                    return data
                return ''
        except Error:
            return ''

    def write_comment(self, user: dict) -> bool:
        try:
            self.connect()
            with self.connecttion.cursor() as cursor:
                query = "INSERT INTO comments (username, comment) VALUE (%s, %s)"
                cursor.execute(query, (user['username'], user['comment']))
                self.connecttion.commit()
                cursor.close()
                return True
        except Error:
            return False