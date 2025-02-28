from db_session import global_init, create_session
from users import User

db_name = input().strip()

global_init(db_name)
session = create_session()
colonists = session.query(User).filter(User.address == 'module_1').all()
for colonist in colonists:
    print(colonist)
