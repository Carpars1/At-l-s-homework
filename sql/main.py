import sqlite3

import os
print("DB yolu:", os.path.abspath("students.db"))


def create_database():
    # Eğer db varsa sil (sıfırdan oluşturmak için)
    if os.path.exists("students.db"):
        os.remove("students.db")

    # Veritabanı oluştur
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    # DB'nin tam yolunu göster (kontrol için)
    print("DB oluşturulduğu yol:")
    print(os.path.abspath("students.db"))

    return conn, cursor


def create_tables(cursor):
    cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
    """)


def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        conn.commit()
        print("students tablosu başarıyla oluşturuldu")

    except sqlite3.Error as e:
        print("SQLite Hatası:", e)

    finally:
        conn.close()
        print("Veritabanı bağlantısı kapatıldı")


if __name__ == "__main__":
    main()
