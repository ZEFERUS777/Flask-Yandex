from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Базовый класс для моделей
Base = declarative_base()

def create_database(db_url: str = "sqlite:///database.db"):
    """
    Создает БД и таблицы на основе моделей
    :param db_url: URL подключения к БД (по умолчанию SQLite)
    """
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    return engine

def get_session(engine=None, db_url: str = None):
    """
    Возвращает сессию для работы с БД
    :param engine: объект engine (если не передан, создается новый)
    :param db_url: URL подключения к БД
    :return: объект сессии
    """
    if not engine:
        engine = create_engine(db_url or "sqlite:///database.db")

    Session = sessionmaker(bind=engine)
    return Session()

