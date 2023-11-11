
def query_spec_type(quterm:str, qureturn:str, quval:str):
    import sqlite3
    init = sqlite3.connect('assets.db')
    cursor = init.cursor()


    aisle_retriever = cursor.execute(f"""
        SELECT {qureturn}
        FROM assets
        WHERE {quterm} = ?
    """, (quval, ))
    type_result = str(cursor.fetchall())
    return type_result