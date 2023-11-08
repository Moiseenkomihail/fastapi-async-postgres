from fastapi import Depends, FastAPI, status
from sqlalchemy.ext.asyncio import AsyncSession

import uvicorn

from model import Test
from schemas import CreateTest
from crud import creeate_new_test
from db import get_session  


app = FastAPI()

@app.get('/')
async def hello():
    return 'hello'

@app.post('/create_test', status_code=status.HTTP_201_CREATED,)
async def create_test(
    test_model_request: CreateTest,
    the_session: AsyncSession = Depends(get_session),
):
    data = creeate_new_test(test_in=test_model_request, session=the_session)
    return data

    # test = Test(**test_in.model_dump())
    # session.add(test)
    # await session.commit()
    # # await session.refresh(test)
    # return test

# @app.get('/get_test', response_model=list(Test))


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)