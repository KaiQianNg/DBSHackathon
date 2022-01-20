import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'raise_on_warnings': True,
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS USERS")
cursor.execute("CREATE DATABASE IF NOT EXISTS LIKED_POST")
cursor.execute("CREATE DATABASE IF NOT EXISTS POST")
cursor.execute("CREATE DATABASE IF NOT EXISTS POST_COMMENT")

cursor.execute("SHOW DATABASES")
for d in cursor: print("DATA",d)