import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('market_bot_db.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS {}(tickers TEXT, periodicity TEXT, time TEXT, id TEXT)'.format('data'))
    base.commit()
        
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO data VALUES(?,?,?,?)', tuple(data.values()))
        base.commit()
        
async def sql_read():
    for ret in cur.execute('SELECT * FROM data').fetchall():
        data_base_list = list(cur.execute('SELECT * FROM data').fetchall())
        return data_base_list
       