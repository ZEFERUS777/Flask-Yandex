from sqlalchemy import integer, SQLAlchemy, Column, Text, String, DateTime, Boolean


class Jobs(SQLAlchemy):
    id = Column(integer)
    team_leader = Column(integer)
    job = Column(Text)
    work_size = Column(integer)
    collaborators = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_finished = Column(Boolean)
