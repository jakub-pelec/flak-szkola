from flask import render_template
from app import app

@app.route('/')
def index():
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