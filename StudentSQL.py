import sqlite3

db = sqlite3.connect('./Student.db')  # creates database
cursor = db.cursor()
query = ('''CREATE TABLE IF NOT EXISTS Ten_Students(ID INT NOT NULL PRIMARY KEY, First_name TEXT, Last_name TEXT, Midterm REAL, 
        Final REAL, Project1 REAL, Project2 REAL, Grade REAL, Letter_Grade TEXT);''')  # creates table
cursor.execute(query)
query = ('''INSERT INTO Ten_Students VALUES
        ('111111', 'John', 'Doe', '85', '87.5', '92', '86', '87.89999999999999', 'B'),
        ('111112', 'Jane', 'Smith', '78', '83.0', '75', '75', '77.2', 'C'),
        ('111113', 'Sarah', 'Thomas', '96', '98.0', '100', '100', '98.80000000000001', 'A'),
        ('111114', 'Frank', 'Brown', '75', '72.5', '87', '92', '83.19999999999999', 'B'),
        ('111115', 'Mike', 'Davis', '48', '65.0', '80', '75', '69.1', 'D'),
        ('111116', 'Jennifer', 'Wilson', '69', '86.0', '91', '95', '86.8', 'B'),
        ('111117', 'Jessica', 'Garcia', '82', '80.0', '86', '91', '85.5', 'B'),
        ('111118', 'Fred', 'Clark', '85', '100.0', '95', '96', '94.3', 'A'),
        ('111119', 'Bob', 'Lopez', '56', '75.0', '80', '80', '74.2', 'C'),
        ('111120', 'Anthony', 'White', '92', '100.0', '95', '92', '94.5', 'A');''')  # inserts all records in one INSERT query
cursor.execute(query)
db.commit()
query = '''SELECT * FROM Ten_Students ORDER BY First_name;'''  # order students by first names
print(cursor.execute(query).fetchall())
query = '''SELECT Letter_Grade, COUNT(*) FROM Ten_Students GROUP BY Letter_Grade;'''  # selects each grade with the number of records matching grade
print(cursor.execute(query).fetchall())
query = '''DELETE FROM Ten_Students WHERE Letter_Grade = 'D';'''  # deletes all records where letter grade is D
cursor.execute(query)
db.commit()
db.close()
