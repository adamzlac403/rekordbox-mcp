import asyncio
from rekordbox_mcp.database import RekordboxDatabase

async def main():
    db = RekordboxDatabase()

    await db.connect()

    count = await db.get_track_count()
    
    print(f"Tracks: {count}")

asyncio.run(main())