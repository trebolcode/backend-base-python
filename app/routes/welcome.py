from typing import Optional
from fastapi import APIRouter, status


router = APIRouter(tags=["Welcome"])


@router.get(
    path="/welcome",
    status_code=status.HTTP_200_OK,
    summary="Return a message"
)
def welcome(name: Optional[str] = None):

    if name is None:
        return {"message": f"Welcome to TrebolCode!"}
    else:
        return {"message": f"Welcome to TrebolCode {name}!"}
