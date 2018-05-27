from . import auth
from .. import db
from ..models import User
from .forms import SignUp, SignIn
from flask_login import login_required, login_user
from flask import render_template, redirect, request, url_for, flash


@auth.route('/register', methods=["GET", "POST"])
def register():
    sign_up = SignUp()

    if sign_up.validate_on_submit():
        user = User(email=sign_up.email.data,
                    username=sign_up.username.data,
                    password=sign_up.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/register.html',sign_up=sign_up,title=title)