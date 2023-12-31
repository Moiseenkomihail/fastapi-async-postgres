from os import error
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
    try:
        return await creeate_new_test(test_in=test_model_request, session=the_session) 
    except:
        return {'eror': 'error'}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)