from pydantic import BaseModel


class InputItem(BaseModel):
    name: str
    description: str
    price: int
    quantity: int
    on_offer: bool

    class Config:
        orm_mode = True


class Item(InputItem):
    id: int
