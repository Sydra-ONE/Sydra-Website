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

@app.route('/services/web')
def services_web():
    """Page service web"""
    return render_template('services_web.html')

@app.route('/services/Cloud_et_DevOps')
def services_cloud():
    """Page service cloud et devops"""
    return render_template('services_cloud.html')

@app.route('/services/Data_IA')
def services_IA():
    """Page service Data and IA engineering"""
    return render_template('services_IA.html')

@app.route('/about')
def about():
    """Page À propos"""
    return render_template('about.html')

@app.route('/why_us')
def why_us():
    """Page Pourquoi nous choisir ?"""
    return render_template('pourquoi_nous.html')

@app.route('/portfolio')
def portfolio():
    """Page portfolio"""
    return render_template('portfolio.html')

@app.route('/portfolio/web')
def portfolio_web():
    """Page portfolio web"""
    return render_template('portfolio_web.html')

@app.route('/portfolio/Cloud_et_DevOps')
def portfolio_cloud():
    """Page portfolio cloud et devops"""
    return render_template('portfolio_cloud.html')

@app.route('/portfolio/Data_IA')
def portfolio_IA():
    """Page portfolio Data and IA engineering"""
    return render_template('portfolio_IA.html')

@app.route('/contact')
def contact():
    """Page contact"""
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
