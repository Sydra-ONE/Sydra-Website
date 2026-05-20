import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Page d'accueil du site vitrine"""
    return render_template('index.html')

@app.route('/services')
def services():
    """Page services"""
    return render_template('services.html')

@app.route('/about')
def about():
    """Page À propos"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Page contact"""
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
