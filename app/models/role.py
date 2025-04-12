from enum import Enum


class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"
    MODERATOR = "moderator"
    EDITOR = "editor"