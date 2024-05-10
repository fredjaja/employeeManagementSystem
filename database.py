import sqlite3

def create_table():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            id TEXT PRIMARY KEY,
            name TEXT,
            gender TEXT,
            position TEXT,
            address TEXT,
            contact TEXT
        )
    ''')
    conn.commit()
    conn.close()

def fetch_employees():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()
    conn.close()
    return employees

def insert_employee(id, name, gender, position, address, contact):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Employees (id, name, gender, position, address, contact) VALUES (?,?,?,?,?,?)', (id, name, gender, position, address, contact))
    conn.commit()
    conn.close()

def delete_employee(id):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Employees WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def update_employee(new_name, new_gender, new_position, new_address, new_contact, id):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Employees SET name = ?, gender = ?, position = ?, address = ?, contact = ? WHERE id = ?', (new_name, new_gender, new_position, new_address, new_contact, id))
    conn.commit()
    conn.close()

def id_exists(id):
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Employees WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

create_table()

