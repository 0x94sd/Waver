import json

def sauvegarder_resultats(pseudo, resultats):
    # Export TXT
    with open(f"{pseudo}.txt", "w", encoding="utf-8") as f:
        f.writelines(resultats)

    # Export JSON
    with open(f"{pseudo}.json", "w", encoding="utf-8") as f:
        json.dump({"pseudo": pseudo, "resultats": resultats}, f, ensure_ascii=False, indent=4)