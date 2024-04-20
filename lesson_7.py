"""субд - система управения базами данных"""
import random,colorama
"""sql - язык структурированных запросов """
""" sqlite3 - база данных это хранилище чего то"""
"""база данных 

таблица 
поля 

"""
import sqlite3 as sq3


with sq3.connect('user.db') as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS games(
    id INTEGER,
    name VARCHAR(20) NOT NULL,
    age INTEGER DEFAULT 1,
    data_game DATE 
    ) """)
