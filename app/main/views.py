from . import main
from flask import render_template, redirect, url_for
from ..models import Blog, Comments
from .forms import CommentForm, BlogForm
from flask_login import login_required, current_user
from .. import db


@main.route('/')
def index():
    test = 'Working!'
    return render_template('index.html', test=test)

@main.route('/quotes')
def quotes():
    all = Blog.query.all()
    people = Blog.query.filter_by(category='people').all()
    nature = Blog.query.filter_by(category='nature').all()
    test = 'Working'
    return render_template('quotes.html',all=all,test=test,people=people,nature=nature)


@main.route('/blog', methods=['GET', 'POST'])
def blog():
    test = 'What do you think of aesthists?'
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        p_body = blog_form.p_body.data
        p_author = blog_form.p_author.data
        category = blog_form.category.data
        new_post = Blog(p_body=p_body,p_author=p_author,category=category)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('blog.html', test=test, blog_form=blog_form)

@main.route('/comments/<int:id>', methods=['GET', 'POST'])
@login_required
def comments(id):
    comment_form = CommentForm()
    comments = Comments.query.order_by('-id').limit(3).all()
    blog = Blog.query.get(id)
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comments(comment=comment,users=current_user.username)
        new_comment.save_comment()
        return redirect(url_for('main.comments', id=blog.id))
    return render_template('comments.html',blog=blog,comments=comments,comment_form=comment_form)


@main.route('/delete/<int:id>')
@login_required
def delete(id):
    del_comment = Comments.query.get(id)
    db.session.delete(del_comment)
    db.session.commit()
    return redirect(url_for('main.index'))