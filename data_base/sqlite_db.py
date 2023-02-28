import sqlite3 as sq
from create_bot import dp, bot

def sql_start():
    global base, cur
    base = sq.connect('market_bot_db.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS {}(tickers TEXT, periodicity TEXT, time TEXT)'.format('data'))
    base.commit()
        
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO data VALUES(?,?,?)', tuple(data.values()))
        base.commit()
        
async def sql_read(message):
    for ret in cur.execute('SELECT * FROM data').fetchall():
        await bot.send_message(message.from_user.id, f'Tickers: {ret[0]}, periodicity: {ret[1]}, time: {ret[2]}') #\nType: {ret[2]}')
    # r = cur.execute('SELECT * FROM data').fetchall()
    # print(r)