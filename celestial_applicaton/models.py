from celestial_applicaton import db, login_manager
from datetime import datetime
from flask_login import UserMixin


# This enables the flask_login package works.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Some id numbers of users will be defined as admin.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean(), default=False, nullable=False)
    date_joined = db.Column(db.String(), default=datetime.utcnow(),
                            nullable=False)
    blogs = db.relationship('Blog', backref='author', lazy=True)

    def __repr__(self):
        return f'User: {self.username}, {self.email}'


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), unique=True, nullable=False)
    context = db.Column(db.Text(), unique=True, nullable=False)
    date_posted = db.Column(db.String(),
                            default=datetime.utcnow(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Blog: {self.title}, {self.date_posted}'
