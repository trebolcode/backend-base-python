from fastapi import APIRouter, status


trebolcode = APIRouter()


@trebolcode.get(
    path="/welcome",
    status_code=status.HTTP_200_OK,
    tags=["Welcome"],
    summary="Return a message"
)
def welcome():
    return {"message": "Welcome to TrebolCode!"}
