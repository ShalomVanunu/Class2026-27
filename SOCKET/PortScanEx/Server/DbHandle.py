import sqlite3


def save_to_db(IP, ports_string):
    conn = sqlite3.connect('scanner_results.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS scans (ip TEXT, ports TEXT)')
    cursor.execute('INSERT INTO scans (ip, ports) VALUES (?, ?)', (IP, ports_string))
    conn.commit()
    conn.close()
    print("Saved to Database!")