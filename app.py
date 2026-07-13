import os
from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

from dotenv import load_dotenv

if os.path.exists('.env'):
    load_dotenv() 
    
print(f"DEBUG: MAIL_SERVER={os.environ.get('MAIL_SERVER')}")

app = Flask(__name__)

# Configuration Flask-Mail
def str_to_bool(s):
    if isinstance(s, bool):
        return s
    return str(s).lower() in ['true', '1', 't', 'y', 'yes']




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

@app.route('/services/cloud-devops')
def services_cloud():
    """Page service cloud et devops"""
    return render_template('services_cloud.html')

@app.route('/services/data-ia')
def services_IA():
    """Page service Data and IA engineering"""
    return render_template('services_IA.html')

@app.route('/about')
def about():
    """Page À propos"""
    return render_template('about.html')

@app.route('/why-us')
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

@app.route('/portfolio/cloud-monitoring')
def portfolio_cloud():
    """Page portfolio cloud et devops"""
    return render_template('portfolio_cloud.html')

@app.route('/portfolio/data-ia')
def portfolio_IA():
    """Page portfolio Data and IA engineering"""
    return render_template('portfolio_IA.html')

@app.route('/contact')
def contact():
    """Page contact"""
    return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def send_contact_email():
    try:
        nom = request.form.get('nom')
        email = request.form.get('email')
        message = request.form.get('message')

        if not all([nom, email, message]):
            return jsonify({'success': False, 'error': 'Tous les champs sont requis'}), 400

        url = "https://api.brevo.com/v3/smtp/email"
        headers = {
            "api-key": os.environ.get('BREVO_API_KEY'),
            "Content-Type": "application/json"
        }
        payload = {
            "sender": {"name": "Sydra", "email": "contact@sydra-one.com"},
            "to": [{"email": "contact@sydra-one.com"}],
            "replyTo": {"email": email, "name": nom},
            "subject": f"Nouveau message de contact de {nom}",
            "textContent": f"Nom: {nom}\nEmail: {email}\n\nMessage:\n{message}"
        }

        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        return jsonify({'success': True, 'message': 'Email envoyé avec succès!'}), 200

    except Exception as e:
        print(f"DEBUG ERREUR: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500
    

@app.route('/mentions-legales')
def mentions_legales():
    return render_template('mentions_legales.html')

@app.route('/confidentialite')
def confidentialite():
    return render_template('confidentialite.html')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

@app.route('/cgv')
def cgv():
    return render_template('cgv.html')
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

