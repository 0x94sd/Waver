from datetime import date
import os
import httpx
from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn
import json

Console = Console()

def couleur_score(score):  # ← tout en haut, avant le while True
    if score >= 65:
        return f"[bold green]Score : {score}/80 ✓[/bold green]"
    else:
        return f"[bold yellow]Score : {score}/80 ~[/bold yellow]"


while True:
    os.system('cls' if os.name == 'nt' else 'cls')
    
    vague = r"""
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
    """
    
    lignes = vague.split('\n')
    vague_coloree = ""
    for i, ligne in enumerate(lignes):
        ratio = i / max(len(lignes) - 1, 1)
        r = int(255 * (1 - ratio))
        g = int(255 * (1 - ratio))
        b = 255
        vague_coloree += f"[rgb({r},{g},{b})]{ligne}[/rgb({r},{g},{b})]\n"
    Console.print(vague_coloree)    

    pseudo = Console.input("[rgb(100,100,255)]Entrez le nom de la cible : [/rgb(100,100,255)]").strip() #.strip() pour enlever les espaces avant et après le pseudo 

    with open("wmn-data.json", "r", encoding="UTF-8") as f:
        data = json.load(f)

    tier_1 = {
        "Instagram": "https://www.instagram.com/{}",
        "TikTok": "https://www.tiktok.com/@{}",
        "Twitter/X": "https://twitter.com/{}",
        "Facebook": "https://www.facebook.com/{}",
        "Snapchat": "https://www.snapchat.com/add/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "Pinterest": "https://www.pinterest.com/{}/",
        "LinkedIn": "https://www.linkedin.com/in/{}",
        "YouTube": "https://www.youtube.com/@{}",
        "Spotify": "https://open.spotify.com/user/{}",
        "SoundCloud": "https://soundcloud.com/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "GitHub": "https://github.com/{}",
        "Steam": "https://steamcommunity.com/id/{}",
        "Discord": "https://discord.com/users/{}",
        "Amazon": "https://www.amazon.com/gp/profile/amzn1.account.{}",
        "Shein": "https://www.shein.com/profile/{}",
        "AliExpress": "https://www.aliexpress.com/store/{}",
        "PayPal.Me": "https://paypal.me/{}",
        "Vinted": "https://www.vinted.fr/member/{}",
    }

    tier_2 = {
        "Dribbble": "https://dribbble.com/{}",
        "Letterboxd": "https://letterboxd.com/{}/",
        "Threads": "https://www.threads.net/@{}",
        "Quora": "https://www.quora.com/profile/{}",
    }

    breaches = {
        "LinkedIn": "Fuite 2021 (~700M comptes exposés)",
        "Twitter/X": "Fuite 2022 (~400M emails/numéros exposés)",
        "Facebook": "Fuite 2021 (~533M comptes exposés)",
        "Instagram": "Fuite 2019 (~49M profils scrappés)",
        "Twitch": "Fuite 2021 (code source + données internes)",
        "Spotify": "Fuite 2020 (~380M identifiants exposés)",
        "Reddit": "Fuite 2018 (emails + mots de passe hashés)",
        "GitHub": "Fuite 2023 (tokens OAuth exposés)",
        "Discord": "Fuite 2023 (~760M emails via bot)",
        "Steam": "Fuite 2011 (~35M comptes exposés)",
        "AliExpress": "Fuite 2020 (~1.1M comptes exposés)",
        "Shein": "Fuite 2022 (~39M comptes exposés)",
        "Quora": "Fuite 2018 (~100M comptes exposés)",
    }

    def verifier_site(site_data, pseudo):
        url = site_data['uri_check'].replace("{account}", pseudo)
        response = httpx.get(url, headers=headers, timeout=10.0, follow_redirects=True)
        
        score = 0
        
        # Critère principal : compte détecté selon WMN
        if response.status_code == site_data['e_code'] and site_data['e_string'] in response.text:
            score += 60
            
            # Bonus uniquement si le compte est déjà détecté
            if site_data.get('m_string') and site_data['m_string'] not in response.text:
                score += 20
        
        return score

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"} # Pour ne pas être bloqué a cause des firewalls

    ficher = open(f"{pseudo}.txt", "a", encoding="utf-8")
    ficher.write(f"\n--- Scan du {pseudo} ---\n")
        
    compte_trouvés = 0

    with Progress(
            TextColumn("\n"), 
            TextColumn("[rgb(100,100,255)]{task.description}[/]"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=Console
        ) as progress:

        task = progress.add_task("Scan en cours...", total=len([s for s in data['sites'] if s['name'] in tier_1]))
        
        # Tier 1 - Plus de critères, donc score plus élevé nécessaire pour valider la présence du compte
        for sites in data['sites']:
            if sites["name"] in tier_1:
                try:
                    score = verifier_site(sites, pseudo)  # ← ne pas oublier
                    if score >= 50:                        # ← ne pas oublier
                        progress.console.print()
                        progress.console.print(f"[rgb(100,100,255)][[/][bold yellow]+[/][rgb(100,100,255)]] Trouvé sur[/] {sites['name']} : {tier_1[sites['name']].format(pseudo)} [rgb(100,100,255)][[/]{couleur_score(score)}[rgb(100,100,255)]][/]")
                        if sites['name'] in breaches:
                            progress.console.print(f"    [rgb(100,100,255)][[/][bold yellow]Fuite connue[/][rgb(100,100,255)]] : {breaches[sites['name']]}")
                            ficher.write(f"    [Fuite connue] : {breaches[sites['name']]}\n")
                        ficher.write(f"[+] {sites['name']} : {tier_1[sites['name']].format(pseudo)}\n")
                        compte_trouvés += 1
                except Exception:
                    pass
                finally:
                    progress.update(task, advance=1)

        # Tier 2 - Moins de critères, donc moins de score nécessaire pour valider la présence du compte
        for sites in data['sites']:
            if sites["name"] in tier_2:
                try:
                    score = verifier_site(sites, pseudo)
                    if score >= 50:
                        url_trouvée = sites['uri_check'].replace("{account}", pseudo)
                        progress.console.print(f"[rgb(100,100,255)][[/][bold yellow]+[/][rgb(100,100,255)]] Trouvé sur[/] {sites['name']} : {url_trouvée} [rgb(100,100,255)][[/]{couleur_score(score)}[rgb(100,100,255)]][/]")
                        if sites['name'] in breaches:
                            progress.console.print(f"    [rgb(100,100,255)][[/][bold yellow]Fuite connue[/][rgb(100,100,255)]] : {breaches[sites['name']]}")
                            ficher.write(f"    [Fuite connue] : {breaches[sites['name']]}\n")
                        ficher.write(f"[+] {sites['name']} : {url_trouvée}\n")
                        compte_trouvés += 1
                except Exception:
                    pass

        if compte_trouvés == 0:
            progress.console.print(f"[rgb(100,100,255)][[/][bold red]-[/][rgb(100,100,255)]] Aucun compte trouvé pour {pseudo}")

    sauvegarder = Console.input("\n[rgb(100,100,255)]Sauvegarder les résultats ? (o/n) : [/]").strip().lower()
    Console.print()
    
    ficher.close()
    if sauvegarder == "o":
        Console.print(f"[rgb(100,100,255)]Les résultats sont sauvegardés dans '{pseudo}.txt'[/].")
    else:
        os.remove(f"{pseudo}.txt")
        Console.print(f"[rgb(100,100,255)]Résultats non sauvegardés.[/]")

    continuer = Console.input("\n[rgb(100,100,255)]Nouvelle recherche ? (o/n) : [/rgb(100,100,255)]").strip().lower()
    if continuer != "o":
        break