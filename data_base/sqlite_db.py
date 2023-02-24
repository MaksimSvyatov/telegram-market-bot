import sqlite3 as sq
from create_bot import dp, bot

def sql_start():
    global base, cur
    base = sq.connect('market_bot_db.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS {}(ticker TEXT PRIMARY KEY, date TEXT)'.format('data'))
    base.commit()
        
async def sql_add_command(ticker,date):
    cur.execute('INSERT INTO data VALUES(?,?)', (ticker, date))
    base.commit()
        
async def sql_read(message):
    for ret in cur.execute('SELECT * FROM data').fetchall():
        await bot.send_message(message.from_user.id, f'Date: {ret[0]}, time: {ret[1]}') #\nType: {ret[2]}')
    # r = cur.execute('SELECT * FROM data').fetchall()
    # print(r)