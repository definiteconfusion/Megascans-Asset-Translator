import sqlite3


init = sqlite3.connect('assets.db')
cursor = init.cursor()

#

def inject(details:list):
        cursor.execute("""
            INSERT INTO assets VALUES (?, ?, ?, ?)
        """, (str(details[0]), str(details[1]), str(details[2]), str(details[3])))
        init.commit()
        return "Committed: {" + str(details) + "}"