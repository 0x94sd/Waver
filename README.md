# 🌊 Waver — OSINT Username Scanner

> Outil de reconnaissance OSINT permettant de vérifier la présence d'un pseudo sur les principales plateformes sociales, avec détection des fuites de données associées.

```
     ...    .     ...                     _                                 
  .~`"888x.!**h.-``888h.                 u                                  
 dX   `8888   :X   48888>               88Nu.   u.                .u    .   
'888x  8888  X88.  '8888>        u     '88888.o888c      .u     .d88B :@8c  
'88888 8888X:8888:   )?""`    us888u.   ^8888  8888   ud8888.  ="8888f8888r 
 `8888>8888 '88888>.88h.   .@88 "8888"   8888  8888 :888'8888.   4888>'88"  
   `8" 888f  `8888>X88888. 9888  9888    8888  8888 d888 '88%"   4888> '    
  -~` '8%"     88" `88888X 9888  9888    8888  8888 8888.+"      4888>      
  .H888n.      XHn.  `*88! 9888  9888   .8888b.888P 8888L       .d888L .+   
 :88888888x..x88888X.  `!  9888  9888    ^Y8888*""  '8888c. .+  ^"8888*"    
 f  ^%888888% `*88888nx"   "888*""888"     `Y"       "88888%       "Y"      
      `"**"`    `"**""      ^Y"   ^Y'                  "YP'                  

                By https://github.com/0x94sd aka Keryan
```

**By [0x94sd](https://github.com/0x94sd) aka Keryan**

---

## ✨ Fonctionnalités

- 🔍 Recherche de pseudo sur **20+ plateformes** (Tier 1 & Tier 2)
- 📊 **Score de confiance** sur 80 points par résultat
- 🔴 Affichage des **fuites de données connues** liées aux plateformes trouvées
- 💾 Sauvegarde optionnelle des résultats dans un fichier `.txt`
- 🎨 Interface CLI colorée avec barre de progression en temps réel
- 🔄 Mode multi-recherche sans relancer le script

---

## 📋 Plateformes couvertes

**Tier 1** (principales) : Instagram, TikTok, Twitter/X, Facebook, Snapchat, Reddit, Pinterest, LinkedIn, YouTube, Spotify, SoundCloud, Twitch, GitHub, Steam, Discord, Amazon, Shein, AliExpress, PayPal.Me, Vinted

**Tier 2** (secondaires) : Dribbble, Letterboxd, Threads, Quora

---

## 🚀 Installation

### 1. Cloner le repo
```bash
git clone https://github.com/0x94sd/waver
cd waver
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Télécharger la base de données WhatsMyName
Le fichier `wmn-data.json` est requis et provient du projet [WhatsMyName](https://github.com/WebBreacher/WhatsMyName).

```bash
curl -o wmn-data.json https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json
```

Ou télécharge-le manuellement et place-le **dans le même dossier** que `Waver.py`.

---

## ▶️ Utilisation

```bash
python Waver.py
```

Puis entre le pseudo de la cible lorsque demandé :

```
Entrez le nom de la cible : johndoe

[+] Trouvé sur GitHub : https://github.com/johndoe [Score : 80/80 ✓]
[+] Trouvé sur Reddit : https://www.reddit.com/user/johndoe [Score : 80/80 ✓]
    [Fuite connue] : Fuite 2018 (emails + mots de passe hashés)
```

---

## 📊 Système de score

| Score | Couleur | Signification |
|-------|---------|---------------|
| 80/80 | 🟢 Vert | Compte détecté + confirmé (très fiable) |
| 60/80 | 🟡 Jaune | Compte détecté mais résultat ambigu |

> Un score < 50 est filtré et n'apparaît pas dans les résultats.

---

## 📁 Structure du projet

```
waver/
├── Waver.py            # Script principal
├── wmn-data.json       # Base de données WhatsMyName (à télécharger)
├── requirements.txt    # Dépendances Python
└── README.md
```

---

## 📦 Dépendances

```
httpx
rich
```

---

## ⚠️ Avertissement légal

Cet outil est destiné à un usage **éducatif et de recherche en cybersécurité uniquement**.  
L'utilisation de cet outil sur des cibles sans consentement explicite peut être **illégale** selon la juridiction.  
L'auteur décline toute responsabilité pour une utilisation malveillante.

---

## 📜 Licence

MIT License — voir [LICENSE](LICENSE)
