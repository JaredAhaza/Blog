from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """
    Defining the user object
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comments', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        """
        Here we take a users password and then hash it.
        We then store the hushed password in password_hash
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Here we compare the hushed password to the users
        password to verify validity
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    """
    Defining the blog object
    """
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    p_body = db.Column(db.String)
    p_author = db.Column(db.String)
    category = db.Column(db.String(255))
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    all_blogs = []

    def __init__(self,p_body,p_author,category):
        self.p_body = p_body
        self.p_author = p_author
        self.category = category

    def save_blogs(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):
        blogs = Blog.query.all()
        return blogs

    @classmethod
    def get_categories(cls, category):
        blog_cat = Blog.query.filter_by(categor=category)
        return blog_cat


class Comments(db.Model):
    """
    Defining the comment object
    """
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, comment, users):
        self.comment = comment
        self.users = users

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()