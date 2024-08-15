import sqlite3

connection = sqlite3.connect('not_telegram_2.db')  # написание 'connection'
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL    
)''')  # Исправлено 'INTAGER' на 'INTEGER'

ag = 0
w = 0
for i in range(10):
    bal = 1000
    w += 1
    ag += 10
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{w}", f"example{w}@gmail.com", ag, bal))  # Убраны лишние кавычки для ag и bal

    if i % 2 == 0:  # Обновляем баланс только для четных id
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))
    if i % 3 == 0:
        cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{w}", ))

cursor.execute("DELETE FROM Users WHERE id = ?", (6, ))
cursor.execute("SELECT COUNT(*) FROM Users")
total_1 = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
total_2 = cursor.fetchone()[0]
cursor.execute("SELECT AVG(balance) FROM Users")
total_3 = cursor.fetchone()[0]
print(total_1, total_2, total_3)
connection.commit()
connection.close()