import sqlite3


init = sqlite3.connect('assets.db')
cursor = init.cursor()


cursor.execute("CREATE TABLE assets(name, id, preview, type)")
init.commit()