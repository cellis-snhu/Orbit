from flask import render_template, redirect, flash, url_for
from ..task.service import task_service
from .forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app import db
import sqlalchemy as sa
from app.models import User
from flask import request
from urllib.parse import urlsplit

from app.main import bp


@bp.route("/")
@bp.route("/index")
@login_required
def index():
    user = {"username": "Chris"}
    tasks = task_service.list_tasks()
    return render_template("index.html", title="Orbit Task Manager", user=user, tasks=tasks)


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))