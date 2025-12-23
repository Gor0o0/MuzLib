from sqlalchemy import Column, Integer, String
from app.database import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    playlist = Column(String, nullable=False)
    duration = Column(String, nullable=False)
