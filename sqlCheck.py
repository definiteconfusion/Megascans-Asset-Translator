def check_spec_id(id: str):
    import sqlite3
    init = sqlite3.connect('assets.db')
    cursor = init.cursor()

    id_retiever = cursor.execute("""
        SELECT name
        FROM assets
        WHERE id = ?
    """, (id, ))
    aisle_result = str(cursor.fetchone())
    if aisle_result == "None":
        exists = False
    else:
        exists = True
    return exists