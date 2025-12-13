

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "agenda.db")
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1
        FROM sqlite_master
        WHERE type = 'table'
          AND name = 'schedule'
        LIMIT 1
    """)

    exists = cursor.fetchone() is not None
    if exists is False:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schedule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(70) NOT NULL,
                date DATETIME NOT NULL,
                description VARCHAR(500)
            )
        """)

        cursor.execute("""
            INSERT INTO schedule (title, date, description)
            VALUES (?, ?, ?)
        """, (
            "Reunião",
            "2025-12-15 10:00",
            "Reunião para definir as metas da próxima sprint"
        ))

        cursor.execute("""
            INSERT INTO schedule (title, date, description)
            VALUES (?, ?, ?)
        """, (
            "Entrega do relatório",
            "2025-12-20 17:30",
            "Entrega final do relatório mensal"
        ))
        conn.commit()

        conn.close()

def get_all_schedules():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM schedule
    """)
    rows = cursor.fetchall() 
    conn.close()  

    schedules = []
    for row in rows:
        schedules.append({
            "id": row[0],
            "title": row[1],
            "date": row[2],
            "description": row[3]
        })
        
    return schedules

def search_schedule(search: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM schedule where Title like ?
    """, (f"%{search}%",))
    rows = cursor.fetchall() 
    conn.close()  

    schedules = []
    for row in rows:
        schedules.append({
            "id": row[0],
            "title": row[1],
            "date": row[2],
            "description": row[3]
        })
        
    return schedules

def create_schedule(schedule):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO schedule (title, date, description)
        VALUES (?, ?, ?)
    """, (schedule["title"], schedule["date"], schedule["description"]))

    conn.commit()
    conn.close()  

def delete_schedule(id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM SCHEDULE WHERE ID = ?
    """, (id,))

    conn.commit()
    conn.close() 


def edit_schedule(schedule):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE schedule 
        SET title = ?, date = ?, description = ?
        WHERE id = ?
    """, (schedule["title"], schedule["date"], schedule["description"], schedule["id"]))

    conn.commit()
    conn.close()           
