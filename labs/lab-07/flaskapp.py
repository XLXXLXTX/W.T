#  Web Technologies Lab 7 | Author: Javier Pardos | javier.pardos10@e-uvt.ro 
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'test.db')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"User: {self.username}\nEmail: {self.email}"
    

@app.route('/')
def display_content(content=None):
    return "Hello world"


@app.route('/user/profile/<int:user_id>')
def dispay_user_profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template('user_profile.html', user=user)


@app.route('/users')
def dispay_all_users():
    users = User.query.all()
    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run()