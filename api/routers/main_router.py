from fastapi import APIRouter


main_router = APIRouter()


@main_router.get("/king")
async def king():
    return {"King": "Kong"}
