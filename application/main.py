# application/__init__.py
from fastapi import FastAPI
from .routers import apirouter
from . import config

app_configs = {"title": "rest-api",
               "HOST": config.HOST}
        
def create_app():
    app = FastAPI(**app_configs)
    app.include_router(apirouter.router)
    return app