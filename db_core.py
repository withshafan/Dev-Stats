import sqlite3
import os

# db file path set karo
db_p = os.path.join("db", "devstats.db")

def get_c():
    # db connect karo
    return sqlite3.connect(db_p)

def init_db():
    # table banao agar nahi hai
    c = get_c()
    cr = c.cursor()
    
    cr.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE,
            followers INTEGER
        )
    ''')
    
    c.commit()
    c.close()

def save_user(lg, fol):
    # user add ya update karo
    c = get_c()
    cr = c.cursor()
    
    cr.execute("SELECT id FROM users WHERE login = ?", (lg,))
    rw = cr.fetchone()
    
    if rw:
        u_id = rw[0]
        cr.execute("UPDATE users SET followers = ? WHERE id = ?", (fol, u_id))
    else:
        cr.execute("INSERT INTO users (login, followers) VALUES (?, ?)", (lg, fol))
        u_id = cr.lastrowid
        
    c.commit()
    c.close()
    return u_id

def save_repos(u_id, r_dat):
    # repos db mein save karne k liye (abhi dashboard direct api use kar raha hai)
    pass

def get_saved_users():
    # list nikalo sab users ki
    c = get_c()
    cr = c.cursor()
    cr.execute("SELECT login, followers FROM users ORDER BY followers DESC")
    rws = cr.fetchall()
    c.close()
    return rws