from flask import url_for, render_template, flash, redirect
from flask_login import login_user, logout_user, current_user, login_required
from celestial_application.forms import RegisterForm, LoginForm, DiaryEntryForm
from celestial_application import app, db, bcrypt
from celestial_application.models import User


@app.route('/')
def home():
    return render_template('home.html', title='Home Page')


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if not current_user.is_admin:
        flash('You do not have permission to see the admin page', 'fail')
        return redirect(url_for('home'))
    return render_template('admin/admin.html', title='Admin Panel')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # If there is no user logged in.
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # If user's entered password
            # matchs with hashed version, then do this.
            login_user(user, remember=form.remember.data)
            flash('Login succesful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'fail')
            return redirect(url_for('login'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # If there is no logged user
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        created_user = User(username=form.username.data,
                            email=form.email.data, password=hashed_password)
        with app.app_context():
            db.session.add(created_user)
            db.session.commit()
        flash(f"Account created for {form.username.data}!", 'success')
        redirect(url_for('login'))
    return render_template('register.html', title='Sign Up', form=form)


@app.route('/logout')
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for('home'))
    logout_user()
    flash(f"You have been logged out.", 'alert')
    return redirect(url_for('home'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/diary', methods=['GET', 'POST'])
def diary():
    if not current_user.is_authenticated:
        return redirect(url_for('home'))
    form = DiaryEntryForm()
    return render_template('diary.html', form=form)
