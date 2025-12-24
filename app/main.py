from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models import Song, Playlist   # ✅ импортируем обе модели

# Создаём таблицы (если их ещё нет)
Base.metadata.create_all(bind=engine)

# Инициализация FastAPI
app = FastAPI()

# Подключение шаблонов Jinja2
templates = Jinja2Templates(directory="templates")


# Функция для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Главная страница — вывод песен и плейлистов из базы
@app.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    songs = db.query(Song).all()         # ✅ список песен
    playlists = db.query(Playlist).all() # ✅ список плейлистов
    return templates.TemplateResponse("index.html", {
        "request": request,
        "songs": songs,
        "playlists": playlists
    })
