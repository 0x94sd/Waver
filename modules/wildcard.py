voyelles = "aeiouyàâéèêëîïôùûüæœ"


def extraire_consonnes(mot):
    return "".join(c for c in mot.lower() if c not in voyelles)


def tronquer(mot, n=3):
    return mot.lower()[:n]


def generer_variantes(prenom, nom):
    prenom = prenom.lower().strip()
    nom = nom.lower().strip()

    p = prenom
    p3 = tronquer(prenom)
    n = nom
    n3 = tronquer(nom)
    cp = extraire_consonnes(prenom)
    cn = extraire_consonnes(nom)

    separateurs = [".", "_", "__", "___", "____", ""]

    variantes = set()

    for sep in separateurs:
        # prénom + nom
        variantes.add(f"{p}{sep}{n}")
        # prénom + nom tronqué
        variantes.add(f"{p}{sep}{n3}")
        # prénom + consonnes nom
        variantes.add(f"{p}{sep}{cn}")
        # prénom tronqué + nom
        variantes.add(f"{p3}{sep}{n}")
        # prénom tronqué + nom tronqué
        variantes.add(f"{p3}{sep}{n3}")
        # prénom tronqué + consonnes nom
        variantes.add(f"{p3}{sep}{cn}")
        # nom + prénom
        variantes.add(f"{n}{sep}{p}")
        # 1ère lettre nom + prénom
        variantes.add(f"{n[0]}{sep}{p}")
        # prénom + 1ère lettre nom
        variantes.add(f"{p}{sep}{n[0]}")
        # nom tronqué + prénom
        variantes.add(f"{n3}{sep}{p}")

    # Avec underscore final ou initial
    variantes.add(f"{p}_")
    variantes.add(f"_{p}")
    variantes.add(f"{n[0]}{p}_")

    return list(variantes)