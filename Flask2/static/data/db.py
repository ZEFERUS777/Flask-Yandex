

from sqlalchemy import (create_engine, MetaData, Table,
                        Column, Integer, String, Boolean)

db = create_engine('sqlite:///web.db')
meta = MetaData()

astro_table = Table('Astronafts', meta,
                    Column('id', Integer, primary_key=True),
                    Column('name_work', String(100), nullable=True),
                    Column('Team_Lead', String(100), nullable=True),
                    Column('Duration', String(100), nullable=True),
                    Column('id_teams', String(100), nullable=True),
                    Column('finished', Boolean, nullable=True))

meta.create_all(db)