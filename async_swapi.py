import sqlite3


def create_table():
    connection = sqlite3.connect('star_wars_characters.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY,
            birth_year TEXT,
            eye_color TEXT,
            films TEXT,
            gender TEXT,
            hair_color TEXT,
            height TEXT,
            homeworld TEXT,
            mass TEXT,
            name TEXT,
            skin_color TEXT,
            species TEXT,
            starships TEXT,
            vehicles TEXT
        )
    ''')
    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_table()