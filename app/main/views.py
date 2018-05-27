from . import main
from flask import render_template, redirect, url_for
from ..models import Blog, Comments
from .forms import CommentForm, BlogForm
from flask_login import login_required, current_user
from .. import db

@main.route('/blog', methods=['GET', 'POST'])
def blog():
    test = 'What does minimalism mean for you?'
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        p_body = blog_form.p_body.data
        p_author = blog_form.p_author.data
        category = blog_form.category.data
        p_url = blog_form.p_url.data
        new_post = Blog(p_body=p_body,p_author=p_author,category=category,p_url=p_url)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.gallery'))
    return render_template('blog.html', test=test, blog_form=blog_form)
