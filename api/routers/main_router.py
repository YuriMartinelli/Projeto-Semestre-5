from fastapi import APIRouter


router = APIRouter()

router.get("/king")


def king():
    return {"King": "Kong"}
