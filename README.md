# Site Vitrine - ESN

Bienvenue sur le site vitrine de notre entreprise. Cette application web présente nos services et notre savoir-faire.

## 📌 À propos

Site vitrine professionnel créé avec Flask et hébergé sur Railway.

## 🚀 Démarrer localement

### Installation

1. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

2. Lancer l'application :
   ```bash
   python app.py
   ```

3. Accéder au site :

### Variables d’environnement

Le formulaire de contact nécessite les variables suivantes :

- `BREVO_API_KEY` : clé API Brevo utilisée pour l’envoi des messages ;
- `TURNSTILE_SITE_KEY` : clé publique Cloudflare Turnstile ;
- `TURNSTILE_SECRET_KEY` : clé secrète Cloudflare Turnstile.

La clé secrète doit uniquement être configurée côté serveur (par exemple dans les variables du projet Railway), jamais dans un template ou dans le code client.

## 📂 Organisation du projet

```
Projet_esn/
├── app.py              # Application principale
├── requirements.txt    # Dépendances
├── templates/          # Pages HTML
├── static/             # Images et styles
└── README.md           # Ce fichier
```

## 🌐 Déploiement

L'application est déployée automatiquement sur [Railway](https://railway.app).

Pour mettre à jour le site en production, simplement faire un push sur la branche principale.

## 📞 Contact

Pour toute information, veuillez nous contacter.

---

*Créé en mai 2026*
