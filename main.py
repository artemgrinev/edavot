import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

from api import router as api_router
from create_app import create_app

main_app = create_app(
    create_custom_static_urls=True,
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
    