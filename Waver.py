import os
import asyncio
import contextlib
import io
from rich.console import Console
from modules.scanner import scanner, tier_1, tier_2
from modules.display import afficher_resultats
from modules.export import sauvegarder_resultats
from modules.wildcard import generer_variantes

os.system('chcp 65001 > nul')
console = Console(highlight=False)


async def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

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
        console.print(vague_coloree)
        

        choix = console.input("[rgb(100,100,255)]Mode de recherche :\n\n[[white]1[/white][rgb(100,100,255)]] Pseudo\n\n[[white]2[/white][rgb(100,100,255)]] Prénom / Nom (wildcard)\n\n[[white]3[/white][rgb(100,100,255)]] Email\n\n> [/]").strip()
        if choix == "1":
            pseudo = console.input("[rgb(100,100,255)]Entrez le Pseudo de la cible : [/rgb(100,100,255)]").strip()
            pseudos = [pseudo]
            nom_fichier = pseudo
        elif choix == "2":
            prenom = console.input("[rgb(100,100,255)]Entrez le Prénom de la cible : [/rgb(100,100,255)]").strip()
            nom = console.input("[rgb(100,100,255)]Entrez le NOM de la cible : [/rgb(100,100,255)]").strip()
            pseudos = generer_variantes(prenom, nom)
            nom_fichier = f"{prenom}_{nom}"
            console.print(f"\n[rgb(100,100,255)][i]{len(pseudos)} variantes générées...[/i][/]\n")
        elif choix == "3":
            email = console.input("[rgb(100,100,255)]Entrez l'email de la cible : [/rgb(100,100,255)]").strip()
            nom_fichier = email.split("@")[0]
            pseudos = []
        else:
            continue

        if choix == "3":
            from modules.email_scan import scanner_email
            with contextlib.redirect_stderr(io.StringIO()):
                resultats_email = await scanner_email(email)
            tous_resultats = []
            for r in resultats_email:
                domain = r.get('domain', '')
                url = f"https://{domain}" if domain else ''
                console.print(f"[rgb(100,100,255)][[/][bold yellow]+[/][rgb(100,100,255)]] Trouvé sur[/] {r['name']} [rgb(100,100,255)]→[/] [underline]{url}[/underline]")
                tous_resultats.append(f"[+] {r['name']} → {url}\n")

        # Scan pseudo / wildcard
        else:
            tous_resultats = []
            sites_cibles = list(tier_1.keys()) + list(tier_2.keys())
            for pseudo in pseudos:
                resultats_bruts = await scanner(pseudo)
                scores = dict(resultats_bruts)
                resultats, _ = afficher_resultats(scores, pseudo, sites_cibles)
                tous_resultats.extend(resultats)

        # Sauvegarde
        sauvegarder = console.input("\n[rgb(100,100,255)]Sauvegarder les résultats ? (o/n) : [/]").strip().lower()
        console.print()

        if sauvegarder == "o":
            sauvegarder_resultats(nom_fichier, tous_resultats)
            console.print(f"[rgb(100,100,255)]Les résultats sont sauvegardés dans '{nom_fichier}.txt' et '{nom_fichier}.json'[/].")
        else:
            console.print("[rgb(100,100,255)]Résultats non sauvegardés.[/]")

        continuer = console.input("\n[rgb(100,100,255)]Nouvelle recherche ? (o/n) : [/rgb(100,100,255)]").strip().lower()
        if continuer != "o":
            break


asyncio.run(main())