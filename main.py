import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from contextlib import asynccontextmanager

from core.config import settings
from core.db.db_helper import db_helper
from api.routers import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()

main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

main_app.include_router(
    api_router,
)
main_app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.allow_origins,
    allow_credentials=settings.cors.allow_credentials,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
    