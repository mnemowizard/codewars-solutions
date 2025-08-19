import sqlite3 as sq

with sq.connect('sql_lessons.db') as con:
    cur = con.cursor()

    cur.execute('SELECT rowid, * FROM users')
    all_players = cur.fetchall()


print('------------------------------------------------------------')
for user in all_players:
    print(user)
print('------------------------------------------------------------')


print('end')