from pydantic import BaseModel


class CreateTest(BaseModel):
    name: str
    