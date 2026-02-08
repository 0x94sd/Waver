# 🌊 Waver - Username Search Tool

Un outil Python pour rechercher la présence d'un pseudonyme sur plusieurs plateformes en ligne.

## 📋 Description

Waver permet de scanner rapidement plusieurs sites web et réseaux sociaux pour vérifier si un nom d'utilisateur est présent sur ces plateformes. L'outil effectue des requêtes HTTP et enregistre les résultats dans un fichier texte.

## ✨ Fonctionnalités

- 🔍 Recherche simultanée sur 20+ plateformes
- 💾 Sauvegarde automatique des résultats dans un fichier texte
- 🎨 Interface colorée avec Rich
- ⚡ Gestion des timeouts et redirections
- 📊 Barre de progression en temps réel

## 🎯 Plateformes supportées

### Réseaux Sociaux
- Instagram, TikTok, Twitter/X, Facebook
- Snapchat, Reddit, Pinterest, LinkedIn

### Tech & Dev
- GitHub, GitLab, StackOverflow
- DockerHub, Dev.to, TryHackMe

### Gaming
- Twitch, Steam, Chess.com, Roblox

### Médias
- YouTube, Spotify, SoundCloud, Medium

## 📦 Installation

### Prérequis
- Python 3.7+
- pip

### Dépendances

```bash
pip install httpx rich
```

## 🚀 Utilisation

```bash
python waver.py
```

L'outil vous demandera d'entrer le pseudonyme à rechercher :

```
Entrez le nom de la cible : exemple_user
```

Les résultats seront affichés en temps réel et sauvegardés dans `exemple_user.txt`.

## 📄 Format de sortie

Les résultats sont enregistrés dans un fichier texte avec le format suivant :

```
--- Scan du exemple_user ---
[+] GitHub : https://github.com/exemple_user
[+] Twitter/X : https://twitter.com/exemple_user
[+] Instagram : https://www.instagram.com/exemple_user
```

## ⚙️ Configuration

Pour ajouter de nouvelles plateformes, modifiez le dictionnaire `repertoire_sites` :

```python
repertoire_sites = {
    "Nom_Plateforme": "https://exemple.com/{}",
}
```

Le `{}` sera remplacé par le pseudonyme recherché.

## ⚠️ Avertissements

- **Usage légal uniquement** : Cet outil est destiné à des fins de recherche légitime (OSINT, vérification de disponibilité de pseudonymes, etc.)
- Respectez les conditions d'utilisation de chaque plateforme
- Certains sites peuvent bloquer les requêtes automatisées
- Un timeout de 5 secondes est défini par défaut pour éviter les blocages

## 🛠️ Limitations

- Les résultats peuvent inclure des faux positifs (profils différents avec le même nom)
- Certaines plateformes peuvent nécessiter une authentification
- Les sites avec protection anti-bot peuvent ne pas être détectés

## 📝 Licence

Ce projet est fourni à des fins éducatives. Utilisez-le de manière responsable et éthique.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Ajouter de nouvelles plateformes
- Améliorer la détection
- Corriger des bugs
- Optimiser les performances

## 📧 Support

Pour toute question ou problème, n'hésitez pas à ouvrir une issue sur le dépôt du projet.

---

**Note** : Cet outil effectue des recherches publiques sur des plateformes accessibles. Il ne contourne aucune mesure de sécurité et n'accède à aucune information privée.
