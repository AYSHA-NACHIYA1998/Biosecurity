import mysql.connector
# MySQL connection configuration
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='biosecurity'
)
cursor = db_connection.cursor(dictionary=True)  # Use dictionary cursor to fetch results as dictionaries
