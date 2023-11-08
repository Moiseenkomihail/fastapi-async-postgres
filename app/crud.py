from sqlalchemy.ext.asyncio import AsyncSession

from model import Test
from schemas import CreateTest


async def creeate_new_test(session: AsyncSession, test_in: CreateTest) -> Test:
        print('create_new')

        test = Test(**test_in.model_dump())
        session.add(test)
        await session.commit()
        # await session.refresh(test)
        return test


