import asyncio
from database import async_engine, Base
from model import User

# 데이터베이스 초기화 함수
async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())

