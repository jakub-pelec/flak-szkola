from flask import render_template, redirect, url_for, session
from flask_dance.contrib.github import github
from flask_login import logout_user
from app import app, blueprint


@app.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            return redirect('/home')
    return '<h1>Request failed!</h1>'

@app.route('/logout', methods=["POST"])
def logout():
    logout_user()
    return redirect('/')

@app.route('/home')
def index():
    print(session)
    return render_template('home.html'), 200

@app.route('/about')
def about():
    return render_template('about.html'), 200


@app.route('/contact')
def contact():
    return render_template('contact.html'), 200


@app.route('/gallery')
def gallery():
    return render_template('gallery.html'), 200

@app.errorhandler(404)
def pagenotfound(e):
    return render_template('404.html'), 404