from sqlalchemy import and_, not_


def main():
    db_name = input().strip()
    global_init(db_name)
    session = create_session()
    colonists = session.query(User.id).join(Jobs, User.id == Jobs.user_id).filter(
        User.module == 1,
        ~Jobs.speciality.ilike('%engineer%'),
        ~Jobs.position.ilike('%engineer%')
    ).all()

    for (colonist_id,) in colonists:
        print(colonist_id)


if __name__ == "__main__":
    main()
