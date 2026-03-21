from rich.progress import Progress, TextColumn, BarColumn
from rich.console import Console
from modules.scanner import tier_1, tier_2, data

console = Console()

def couleur_score(score):
    if score >= 65:
        return f"[bold green]Score : {score}/80 ✓[/bold green]"
    else:
        return f"[bold yellow]Score : {score}/80 ~[/bold yellow]"


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


def afficher_resultats(scores, pseudo, sites_cibles):
    resultats = []
    compte_trouvés = 0

    with Progress(
        TextColumn("\n"),
        TextColumn("[rgb(100,100,255)]{task.description}[/]"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:

        total_sites = len([s for s in data['sites'] if s['name'] in tier_1 or s['name'] in tier_2])
        task = progress.add_task("Affichage des résultats...", total=total_sites)

        # Tier 1
        for sites in data['sites']:
            if sites["name"] in tier_1:
                score = scores.get(sites['name'], 0)
                if score >= 50:
                    progress.console.print()
                    progress.console.print(f"[rgb(100,100,255)][[/][bold yellow]+[/][rgb(100,100,255)]] Trouvé sur[/] {sites['name']} : {tier_1[sites['name']].format(pseudo)} [rgb(100,100,255)][[/]{couleur_score(score)}[rgb(100,100,255)]][/]")
                    if sites['name'] in breaches:
                        progress.console.print(f"    [rgb(100,100,255)][[/][bold yellow]Fuite connue[/][rgb(100,100,255)]] : {breaches[sites['name']]}")
                        resultats.append(f"    [Fuite connue] : {breaches[sites['name']]}\n")
                    resultats.append(f"[+] {sites['name']} : {tier_1[sites['name']].format(pseudo)}\n")
                    compte_trouvés += 1
                progress.update(task, advance=1)

        # Tier 2
        progress.console.print("\n[dim]── Tier 2 ──[/dim]")
        for sites in data['sites']:
            if sites["name"] in tier_2:
                score = scores.get(sites['name'], 0)
                if score >= 50:
                    url_trouvée = tier_2[sites['name']].format(pseudo)
                    progress.console.print()
                    progress.console.print(f"[rgb(100,100,255)][[/][bold yellow]+[/][rgb(100,100,255)]] Trouvé sur[/] {sites['name']} : {url_trouvée} [rgb(100,100,255)][[/]{couleur_score(score)}[rgb(100,100,255)]][/]")
                    if sites['name'] in breaches:
                        progress.console.print(f"    [rgb(100,100,255)][[/][bold yellow]Fuite connue[/][rgb(100,100,255)]] : {breaches[sites['name']]}")
                        resultats.append(f"    [Fuite connue] : {breaches[sites['name']]}\n")
                    resultats.append(f"[+] {sites['name']} : {url_trouvée}\n")
                    compte_trouvés += 1
                progress.update(task, advance=1)

        if compte_trouvés == 0:
            progress.console.print(f"[rgb(100,100,255)][[/][bold red]-[/][rgb(100,100,255)]] Aucun compte trouvé pour {pseudo}")

    return resultats, compte_trouvés