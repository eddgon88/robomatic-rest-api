# application/__init__.py
from fastapi import FastAPI
from routers import apirouter

app = FastAPI()
app.include_router(apirouter.router)
        
