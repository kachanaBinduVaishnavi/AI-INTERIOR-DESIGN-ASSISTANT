import sqlite3
from datetime import datetime

DATABASE = "interior_design.db"

def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()


    cursor.execute("""
         CREATE TABLE IF NOT EXISTS design_history (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             image_name TEXT,
             room_type TEXT,
             style TEXT,
             budget TEXT,
             ai_analysis TEXT,
             created_at TEXT
            )
        """)

    connection.commit()
    connection.close()


def save_design(image_name, room_type, style, budget, ai_analysis):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO design_history
        (image_name, room_type, style, budget, ai_analysis, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        image_name,
        room_type,
        style,
        budget,
        ai_analysis,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
)

    connection.commit()
    connection.close()


def get_designs():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM design_history
    ORDER BY id DESC
""")

    designs = cursor.fetchall()

    connection.close()
    return designs

