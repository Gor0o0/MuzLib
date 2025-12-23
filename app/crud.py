from sqlalchemy.orm import Session
from app import models

def get_songs(db: Session):
    return db.query(models.Song).all()
