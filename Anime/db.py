import sqlite3

connection = sqlite3.connect('chinook.db')
print("Connect to DB Succeed !")
cursor = connection.execute("SELECT * FROM Customers;")
for row in cursor:
    print("Customer ID :",row[1])