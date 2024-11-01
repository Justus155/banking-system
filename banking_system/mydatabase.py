import _mysql_connector
import sqlite3

def create_tables(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                equity_card_number TEXT NOT NULL UNIQUE,
                account_type TEXT NOT NULL
            )
        ''')

def add_client(conn, user):
    with conn:
        conn.execute('''
            INSERT INTO clients (first_name, last_name, equity_card_number, account_type)
            VALUES (?, ?, ?,?)
        ''', (user.first_name, user.last_name, user.equity_card_number, user.account_type))

def update_client(conn, equity_card_number, first_name, last_name):
    with conn:
        conn.execute('''
            UPDATE clients
            SET first_name = ?, last_name = ?
            WHERE equity_card_number = ?
        ''', (first_name, last_name, equity_card_number))

def delete_client(conn, equity_card_number):
    with conn:
        conn.execute('''
            DELETE FROM clients
            WHERE equity_card_number = ?
        ''', (equity_card_number,))

def get_client(conn, equity_card_number):
    cursor = conn.execute('''
        SELECT first_name, last_name, equity_card_number, account_type
        FROM clients
        WHERE equity_card_number = ?
    ''', (equity_card_number,))
    row = cursor.fetchone()
    if row:
        if row[3] == 'savings':
            return SavingsUser(row[0], row[1], row[2])
        elif row[3] == 'current':
            return CurrentUser(row[0], row[1], row[2])
    return None
