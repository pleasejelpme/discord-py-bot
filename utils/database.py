import aiosqlite

async def create_connection(db_file):    
    try:
        conn = await aiosqlite.connect(db_file)
        return conn
    except RuntimeError as e:
        print(e)
        raise
    

