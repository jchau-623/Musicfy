from app.models import db, User

users = [
    User(
        username='Demo',
        email='demo@aa.io',
        password='password',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/user-seeds/corgi.jpg'
        ),
    User(
        username='marnie',
        email='marnie@aa.io',
        password='password',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/user-seeds/corgi.jpg'
        ),
    User(
        username='bobbie',
        email='bobbie@aa.io',
        password='password',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/user-seeds/corgi.jpg'
        )
]

# Adds a demo user, you can add other users here if you want
def seed_users():
    for user in users:
        db.session.add(user)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
