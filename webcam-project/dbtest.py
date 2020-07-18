import mysql.connector as mydb

# 接続する 
conn = mydb.connect(
    host='192.168.10.8',
    port='3306',
    user='root',
    password='password',
    database='django_docker'
)

# カーソルを取得する
cur = conn.cursor()

# SQL（データベースを操作するコマンド）を実行する
# userテーブルから、HostとUser列を取り出す
sql = "select * from USER"
cur.execute(sql)

# 実行結果を取得する
rows = cur.fetchall()

# 一行ずつ表示する
for row in rows:
 print(row)

cur.close
conn.close
