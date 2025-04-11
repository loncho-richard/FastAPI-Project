from fastapi import APIRouter, Depends, status

from app.api.deps import (
    get_user_service
)
from app.schemas.user import (
    UserCreate,
    UserOut
)
from app.services.user_service import UserService


router = APIRouter()


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def create_user(
    user_create: UserCreate,
    user_service: UserService = Depends(get_user_service)
) -> UserOut:
    return user_service.create_user(user_create)