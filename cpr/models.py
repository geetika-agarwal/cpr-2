from cpr import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    tech = db.relationship('Tech', backref='user', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}')"


class Tech(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tech1 = db.Column(db.String(60))
    tech2 = db.Column(db.String(60))
    tech3 = db.Column(db.String(60))
    tech4 = db.Column(db.String(60))
    tech5 = db.Column(db.String(60))
    tech6 = db.Column(db.String(60))
    tech7 = db.Column(db.String(60))
    tech8 = db.Column(db.String(60))
    tech9 = db.Column(db.String(60))
    tech10 = db.Column(db.String(60))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Tech('{self.tech1}', '{self.tech2}', '{self.tech3}', '{self.tech4}', '{self.tech5}', '{self.tech6}', '{self.tech7}', '{self.tech8}', '{self.tech9}', '{self.tech10}')"


@login_manager.user_loader
def load_user(user_id):
    return Ruser.query.get(int(user_id))


class Ruser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String(40), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self) -> str:
        return f"Ruser('{self.username}', '{self.email}')"
