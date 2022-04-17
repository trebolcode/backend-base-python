from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes:
from app.routes import welcome
from app.routes import items


def get_application():

    app = FastAPI(
        title="Backend Basic Python",
        description="Backend Basic Python",
        docs_url="/",
        version="0.2.0"
    )

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(welcome.router)
    app.include_router(items.router)

    return app


application = get_application()
