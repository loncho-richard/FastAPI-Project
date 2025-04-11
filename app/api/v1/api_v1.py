from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth,
    users
)


router = APIRouter(prefix="/v1")
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(users.router, prefix="/users", tags=["Users"])