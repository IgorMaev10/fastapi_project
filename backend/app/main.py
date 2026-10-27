from fastapi import FastAPI

def get_application() -> FastAPI:
    _app = FastAPI(
        title='backend'
    )
    return _app

app = get_application()
