from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brittany'}
    tasks = [
        {
            'taskID': 1,
            'name': {'taskname': 'Task 1'},
            'description': 'This is the description of task 1'
        },
        {
            'taskID': 2,
            'name': {'taskname': 'Task 2'},
            'description': 'This is the description of task 2'
        },
    ]
    return render_template('index.html', title="Home Page", user=user, tasks=tasks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)