from sqlalchemy.orm import sessionmaker
from db import db, meta

connection = db.connect()

Sess = sessionmaker(bind=db)
session = Sess()

# Данные для добавления
new_astronauts = [
    {
        'name_work': 'Scientist',
        'Team_Lead': 'Alice Brown',
        'Duration': '20 hours',
        'id_teams': '1,4',
        'finished': False
    },
    {
        'name_work': 'Pilot',
        'Team_Lead': 'Mike Johnson',
        'Duration': '10 hours',
        'id_teams': '5',
        'finished': True
    },
    {
        'name_work': 'Technician',
        'Team_Lead': 'Sarah Wilson',
        'Duration': '8 hours',
        'id_teams': '2,3,6',
        'finished': False
    },
    {
        'name_work': 'Researcher',
        'Team_Lead': 'David Lee',
        'Duration': '30 hours',
        'id_teams': '7',
        'finished': True
    },
    {
        'name_work': 'Engineer',
        'Team_Lead': 'Emma Davis',
        'Duration': '12 hours',
        'id_teams': '4,5',
        'finished': False
    }
]

# Добавляем все записи
for astronaut in new_astronauts:
    new_ad = meta.tables['Astronafts'].insert().values(**astronaut)
    session.execute(new_ad)

session.commit()
session.close()