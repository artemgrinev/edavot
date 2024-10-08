from fastapi import APIRouter

from api.routers.fastapi_users_routers import fastapi_users
from api.dependencies.authentication.backend import authentication_backend
from core.config import settings
from schemas.user import (
    UserRead,
    UserCreate,
)

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

# /login and /logout
router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
    ),
)

# /register
router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)
