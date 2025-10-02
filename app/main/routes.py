from flask import render_template, redirect, flash
from ..task.service import task_service
from .forms import LoginForm

from app.main import bp


@bp.route("/")
@bp.route("/index")
def index():
    user = {"username": "Chris"}
    tasks = task_service.list_tasks()
    return render_template("index.html", title="Orbit Task Manager", user=user, tasks=tasks)


@bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect("/index")
    return render_template('login.html', title='Sign In', form=form)
