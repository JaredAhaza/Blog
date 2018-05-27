from . import main
from flask import render_template, redirect, url_for
from ..models import Blog, Comments
from .forms import CommentForm, BlogForm
from flask_login import login_required, current_user
from .. import db