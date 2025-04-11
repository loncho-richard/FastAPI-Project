from sqlmodel import select
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.hashing import get_password_hash


class UserRepository:
    def __init__(self, session):
        self.session = session

    def create_user(self, user_create: UserCreate):
        hashed_password = get_password_hash(user_create.password)
        db_user = User(**user_create.model_dump(exclude={"password"}), hashed_password=hashed_password)
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user
    
    def get_by_email(self, email: str):
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()