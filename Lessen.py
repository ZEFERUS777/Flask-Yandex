from sqlalchemy import Column, Integer, String, Table, MetaData, create_engine

metadata = MetaData()
user_table = Table('user', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String),
                   Column('fullname', String))

jobs_table = Table('jobs', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('title', String),
                   Column('description', String))


engine = create_engine('sqlite:///example.db')
connector = engine.connect()

connector.execute(user_table.insert().values(name='Adriano', fullname='Rodrigues'))
connector.execute(jobs_table.insert().values(title='Programador', description='P0'))
connector.commit()
print(connector.execute(user_table.select()).fetchall())
print(connector.execute(jobs_table.select()).fetchall())