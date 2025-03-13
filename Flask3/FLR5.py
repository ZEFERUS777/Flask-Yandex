from sqlalchemy.orm import sessionmaker

db_name = input().strip()

global_init(db_name)
sess = create_session()
colons_id = sess.query(User.id).filter(User.address == 'module_1', User.speciality.notlike('%engineer%'),
                                       User.position.notlike('%engineer%')).all()

for i in colons_id:
    print(i[0])
