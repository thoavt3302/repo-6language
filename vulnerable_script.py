
import sqlite3

# Hardcoded secret
API_KEY = "sk_test_1234567890abcdef"

def get_user_info(user_id):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    return cursor.fetchall()
