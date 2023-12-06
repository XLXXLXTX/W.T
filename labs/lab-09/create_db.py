#  Web Technologies Lab 9 | Author: Javier Pardos | javier.pardos10@e-uvt.ro 

from datetime import datetime

from flaskapp import app, db, User, Post

with app.app_context():
    db.create_all()
    
    # Populate database with some entries
    admin = User(username='admin', email='admin@example.com', age=42)
    regular_user = User(username='user', email='user@example.com', age=20)
    
    post1 = Post(user_id=1,
                 posted=datetime.strptime("5 November 2021", "%d %B %Y"),
                 title="Hello World!",
                 body="This is the first post on this blog.")
    
    post2 = Post(user_id=1,
                 posted=datetime.strptime("17 November 2021", "%d %B %Y"),
                 title="Post Number two",
                 body="This is the second post on this blog.")
    
    post3 = Post(user_id=2,
                 posted=datetime.utcnow(),
                 title="Post number three",
                 body="This is the third post on this blog.")
    
    
    db.session.add(admin)
    db.session.add(regular_user)
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    
    db.session.commit()