from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create an SQLite database and table for demonstration
def init_db():
    with sqlite3.connect('app.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users
                        (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
        conn.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpass')")
        conn.execute("INSERT INTO users (username, password) VALUES ('user1', 'user1pass')")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    with sqlite3.connect('app.db') as conn:
        cursor = conn.execute(query)
        user = cursor.fetchone()
        if user:
            return jsonify({"status": "success", "user": user})
        else:
            return jsonify({"status": "failure"}), 401

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

