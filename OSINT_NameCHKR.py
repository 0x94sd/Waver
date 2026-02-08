import httpx
from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn

Console = Console()

vague = r"""
 █     █░ ▄▄▄    ██▒   █▓▓█████  ██▀███  
▓█░ █ ░█░▒████▄ ▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒█░ █ ░█ ▒██  ▀█▄▓██  █▒░▒███   ▓██ ░▄█ ▒
░█░ █ ░█ ░██▄▄▄▄██▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░░██▒██▓  ▓█   ▓██▒▒▀█░  ░▒████▒░██▓ ▒██▒
░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒ ░ ░    ▒   ▒▒ ░░ ░░   ░ ░  ░  ░▒ ░ ▒░
  ░   ░    ░   ▒     ░░     ░     ░░   ░ 
    ░          ░  ░   ░     ░  ░   ░     
                     ░                                
"""

vague_coloree = ""
for caractere in vague:
    if caractere in ["█", "▓"]:
        
        vague_coloree += f"[bold white]{caractere}[/bold white]"
    elif caractere in ["▒", "░"]:

        vague_coloree += f"[cyan]{caractere}[/cyan]"
    else:
        vague_coloree += f"[blue]{caractere}[/blue]"

Console.print(vague_coloree)

pseudo = Console.input("[bold blue]Entrez le nom de la cible : [/bold blue]").strip() #.strip() pour enlever les espaces avant et après le pseudo 
repertoire_sites = {
    # Réseaux Sociaux
    "Instagram": "https://www.instagram.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Twitter/X": "https://twitter.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    
    # Tech & Dev
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "DockerHub": "https://hub.docker.com/u/{}",
    "Dev.to": "https://dev.to/{}",
    "TryHackMe": "https://tryhackme.com/p/{}",
    
    # Gaming
    "Twitch": "https://www.twitch.tv/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Chess.com": "https://www.chess.com/member/{}",
    "Roblox": "https://www.roblox.com/user.aspx?username={}",
    
    # Médias
    "YouTube": "https://www.youtube.com/@{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Medium": "https://medium.com/@{}",
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"} # Pour ne pas être bloqué a cause des firewalls

with open(f"{pseudo}.txt", "a", encoding="utf-8") as ficher: # enregistre les resultats dans un fichier texte
    ficher.write(f"\n--- Scan du {pseudo} ---\n")
        
    with Progress( # affichage d'une barre de progression pendant le scan
            TextColumn("\n"), 
            TextColumn("[cyan]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=Console
        ) as progress:

        for nom_site, maquette in repertoire_sites.items():
                url_complete = maquette.format(pseudo)
    
                try:
                    response = httpx.get(url_complete, headers=headers, timeout=5.0, follow_redirects=True) # envoie d'une requete http pour acceder a la cible

                    if response.status_code == 200: # si le site existe, on affiche le resultat et on l'enregistre dans le fichier texte
                        progress.console.print(f"[bold blue][[/][bold yellow]+[/][bold blue]] Trouvé sur[/] {nom_site} : {url_complete}")
                        ficher.write(f"[+] {nom_site} : {url_complete}\n")

                except Exception: # si erreur -> on ignore et on continue le scan
                    pass

Console.print()        
Console.print(f"[bold yellow]Terminé![/] Les résultats sont sauvegardés dans [cyan]'{pseudo}.txt'[/].")