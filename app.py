import os
from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

@app.route('/contact', methods=['POST'])
def send_contact_email():
    """Envoie le formulaire de contact par email"""
    try :
        nom = request.form.get('nom')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Validation
        if not all([nom, email, message]):
            return jsonify({'success': False, 'error': 'Tous les champs sont requis'}), 400
        
        smtp_server = os.environ.get('MAIL_SERVER', 'smtp.ionos.fr')
        # On définit 587 comme port par défaut au lieu de 465
        smtp_port = int(os.environ.get('MAIL_PORT', 587))
        sender_email = os.environ.get('MAIL_USERNAME')
        password = os.environ.get('MAIL_PASSWORD')
        recipient = 'contact@sydra-one.com'

        # Construction du message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = f"Nouveau message de contact de {nom}"
        
        body = f"""
Nouveau message de contact via sydra-one.com :

Nom: {nom}
Email: {email}

Message:
{message}
            """
        msg.attach(MIMEText(body, 'plain'))
        
        # Utilisation de SMTP pour le port 587 (STARTTLS)
        with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
            server.starttls()  # Upgrade vers une connexion sécurisée
            server.login(sender_email, password)
            server.send_message(msg)
        return jsonify({'success': True, 'message': 'Email envoyé avec succès!'}), 200
        
    except Exception as e:
        print(f"DEBUG ERREUR: {str(e)}") # Important pour voir l'erreur dans les logs Railway
        return jsonify({'success': False, 'error': str(e)}), 500
    
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

