from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import SubmissionForm, LoginForm, RegistrationForm
from app.models import Post, User
from app import db
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
@app.route('/index')
def index():
    current_posts = Post.query.all()
    return render_template('index.html', title='Home', posts=current_posts, logged_in = True)


@app.route('/posts/<postid>')
def showpost(postid):
    if current_user.is_authenticated:
        current_posts = Post.query.filter_by(id=postid)
        return render_template('showpost.html', title='Show Post', post=current_posts[0])
    return render_template('notloggedin.html')


@app.route('/submit', methods=['GET', 'POST'])
def submitpage():
    if current_user.is_authenticated:
        form = SubmissionForm()
        if form.validate_on_submit():
            flash('Topic {} has been submitted.'.format(
                form.title.data))
            new_title = form.title.data
            new_text = form.text.data
            p = Post(title=new_title,body=new_text)
            db.session.add(p)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('submit.html',  title='Submit New Entry', form=form)
    return render_template('notloggedin.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
