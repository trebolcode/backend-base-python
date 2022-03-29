from fastapi import FastAPI
from app.routes.welcome import trebolcode
from fastapi.middleware.cors import CORSMiddleware


def get_application():

    app = FastAPI(
        title="Backend Basic Python",
        description="Backend Basic Python",
        docs_url="/"
    )

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(trebolcode)

    return app


application = get_application()
