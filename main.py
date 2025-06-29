from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import users
import pages

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users.router)
app.include_router(pages.router)