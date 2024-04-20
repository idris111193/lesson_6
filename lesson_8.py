import sqlite3
"""data base"""
"""SQL"""
"""субд"""
"""nosql sql-relation"""

with sqlite3.connect('new.db') as conn:
    pult=conn.cursor()
    pult.execute("""CREATE TABLE IF NOT EXISTS login(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    pol INT NOT NULL,
    password TEXT NOT NULL DEFAULT 'PASSWORD'
    )""")

    pult.execute("""CREATE TABLE IF NOT EXISTS game(
    id INTEGER,
    name TEXT,
    score INT)
    """)
    """create """
    # pult.execute("""INSERT INTO game(id,name,score) VALUES(1,'beka',200),
    # (1,'beka',209),(1,'beka',2),(1,'beka',2000)""")
    # pult.execute("""SELECT * FROM game""")
    # for i in pult:
    #     print(i)
    # print()
    """CRUD"""
    """ UPDATE """
    # pult.execute('''UPDATE login SET name = 'Aygul' WHERE length(password) > 5''')

    """ =,==,<,>,>=,<=,!=,<>,BETWEEN(1,5) """

    """read"""
    # pult.execute("""SELECT * FROM login """)

    """where=if"""
    """ fetchmany(n) - nное количество данных
        fetchone()-1 данную и первую 
        fetchall()-все данные   
    """
    # for i in pult:
    #     print(i)

    pult.execute("""SELECT login.name, game.score FROM game 
    JOIN login ON game.id=login.id ORDER BY score   """)
    for i in pult:
        print(i)

    """агрегирование  MIN MAX AVG COUNT SUMM"""
    pult.execute("""SELECT COUNT(score) FROM game WHERE id=1  """)
    for i in pult:
        print(i)

    pult.execute("""DELETE FROM login WHERE id=1""")
