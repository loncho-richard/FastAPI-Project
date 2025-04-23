from fastapi import APIRouter, Depends
from app.core.permissions import PermissionChecker
from app.models.role import Role


router = APIRouter()


@router.get("/admin")
async def admin_router(
    _ = Depends(PermissionChecker([Role.ADMIN,]))
):
    return {"message": "This path is only for admins"}