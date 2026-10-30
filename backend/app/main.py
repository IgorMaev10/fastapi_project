from fastapi import FastAPI
from apps.users.routers import router_users
from settings import settings

def get_application() -> FastAPI:
    _app = FastAPI(
        title='backend',
        root_path='/api',
        debug=settings.DEBUG
    )
    _app.include_router(router_users, prefix='/users', tags=['Users'])
    return _app

app = get_application()
