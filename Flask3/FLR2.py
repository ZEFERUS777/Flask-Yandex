from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text


class Jobs(SqlAlchemyBase):
    id = Column(Integer)
    team_leader = Column(Integer)
    job = Column(Text)
    work_size = Column(Integer)
    collaborators = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_finished = Column(Boolean)
