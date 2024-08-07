from fastapi import APIRouter

router = APIRouter(
    # prefix="/index",
    # tags=["landing page"],
    # responses={404: {"description": "Not found"}},
)


@router.get("/")
async def index():
    return {"Ola": "indice"}
