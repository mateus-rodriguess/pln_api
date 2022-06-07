from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from apps.models import accuracy_models
from apps.models import user_models
from apps.routes import accuracy_router

from .database import Base, SessionLocal, engine

app = FastAPI(openapi_url="/openapi.json")



#Base.metadata.drop_all(bind=engine, tables=[accuracy_models.AccuracyModel.__table__])
#Base.metadata.drop_all(bind=engine, tables=[user_models.UserModel.__table__])
accuracy_models.Base.metadata.create_all(bind=engine)
user_models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8080"
    "http://0.0.0.0:8000/",
    "http://0.0.0.0"

    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# prefix and version api
# app.router.prefix = "/api/v1"

app.include_router(accuracy_router.router)
# uvicorn apps.main:app --reload
# uvicorn apps.main:app --reload --workers 1 --host 0.0.0.0 --port 8090
