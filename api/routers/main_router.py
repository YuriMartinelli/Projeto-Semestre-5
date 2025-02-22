from fastapi import APIRouter


main_router = APIRouter()


@main_router.get("/king")
def king():
    return {"King": "Kong"}
