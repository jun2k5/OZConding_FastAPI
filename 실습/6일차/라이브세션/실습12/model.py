from database import Base
from sqlalchemy import Column, Integer, String


# 데이터베이스 모델 정의
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    password = Column(String, nullable=False)


