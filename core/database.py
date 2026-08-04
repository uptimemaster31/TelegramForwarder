import aiosqlite
import os

DB_PATH = "data/database.db"


async def init_database():
    os.makedirs("data", exist_ok=True)

    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            source_channel TEXT,
            source_message_id INTEGER,

            converter_message_id INTEGER,

            destination_channel TEXT,
            destination_message_id INTEGER,

            status TEXT DEFAULT 'pending',

            retry_count INTEGER DEFAULT 0,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            UNIQUE(source_channel, source_message_id)
        )
        """)

        await db.commit()


async def add_message(
    source_channel,
    source_message_id,
    destination_channel
):

    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute("""
        INSERT OR IGNORE INTO messages
        (
            source_channel,
            source_message_id,
            destination_channel
        )
        VALUES (?, ?, ?)
        """,
        (
            str(source_channel),
            source_message_id,
            str(destination_channel)
        ))

        await db.commit()



async def update_status(
    source_channel,
    source_message_id,
    status
):

    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute("""
        UPDATE messages
        SET status=?
        WHERE source_channel=?
        AND source_message_id=?
        """,
        (
            status,
            str(source_channel),
            source_message_id
        ))

        await db.commit()



async def is_processed(
    source_channel,
    source_message_id
):

    async with aiosqlite.connect(DB_PATH) as db:

        cursor = await db.execute("""
        SELECT status
        FROM messages
        WHERE source_channel=?
        AND source_message_id=?
        """,
        (
            str(source_channel),
            source_message_id
        ))

        result = await cursor.fetchone()


        if result:
            return result[0]

        return None



async def get_pending():

    async with aiosqlite.connect(DB_PATH) as db:

        cursor = await db.execute("""
        SELECT *
        FROM messages
        WHERE status='pending'
        """)

        return await cursor.fetchall()
