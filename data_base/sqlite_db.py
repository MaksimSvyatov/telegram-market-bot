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
        # await bot.send_message(message.from_user.id, f'Tickers: {ret[0]}, periodicity: {ret[1]}, time: {ret[2]}') #\nType: {ret[2]}')
        data_base_list = list(cur.execute('SELECT * FROM data').fetchall())
        return data_base_list
        print(type(data_base_list)) 

# async def fetch_one_item():
#     # for ret in cur.execute('SELECT tickers FROM data WHERE id = 99117096').fetchone():
#         tickers = list(cur.execute('SELECT tickers FROM data WHERE id = 99117096').fetchone())
#         print(tickers)
#         return tickers

# def sql_read1():
#     for ret in cur.execute('SELECT * FROM data').fetchall():
#         # await bot.send_message(message.from_user.id, f'Tickers: {ret[0]}, periodicity: {ret[1]}, time: {ret[2]}') #\nType: {ret[2]}')
#         data_base_list1 = list(cur.execute('SELECT * FROM data').fetchall())
#         return data_base_list1
#         print(type(data_base_list)) 