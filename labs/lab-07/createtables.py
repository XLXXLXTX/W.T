#  Web Technologies Lab 7 | Author: Javier Pardos | javier.pardos10@e-uvt.ro 
from flaskapp import db, User, app

with app.app_context():
    db.create_all()

    # Populate database with some entries
    admin = User(username='admin', email='admin@example.com', age=42)
    regular_user = User(username='user', email='user@example.com', age=20)

    db.session.add(admin)
    db.session.add(regular_user)

    db.session.commit()