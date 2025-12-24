from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app import crud, models

# Создаём таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    songs = db.query(Song).all()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "songs": songs
    })
