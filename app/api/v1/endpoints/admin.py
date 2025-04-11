from fastapi import APIRouter, Depends
from app.core.security import check_superuser


router = APIRouter()


@router.get("/admin")
async def admin_router(
    _ = Depends(check_superuser)
):
    return {"message": "This path is only for admins"}