#!/usr/bin/env python3
"""
merge.py — Fusion des 4 corpus en un seul fichier final
Usage : python merge.py
"""

import os
import random

FICHIERS = [
    "corpus_claude_clean.txt",
    "corpus_gpt_clean.txt",
    "corpus_gemini_clean.txt",
    "corpus_deepseek_clean.txt",
]

OUTPUT = "corpus_final_2B.txt"


def main():
    print("Fusion des corpus...\n")
    total = 0
    blocs = []

    for fichier in FICHIERS:
        if not os.path.exists(fichier):
            print(f"⚠ Fichier manquant : {fichier} — ignoré")
            continue
        with open(fichier, "r", encoding="utf-8") as f:
            texte = f.read()
        taille = len(texte)
        total += taille
        print(f"✓ {fichier} : {taille:,} caractères")

        # Découper en blocs
        paragraphes = [p.strip() for p in texte.split("\n\n") if p.strip()]
        blocs.extend(paragraphes)

    print(f"\nTotal avant mélange : {total:,} caractères")
    print(f"Blocs totaux        : {len(blocs):,}")

    # Mélanger pour la diversité
    random.shuffle(blocs)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n\n".join(blocs))

    taille_finale = os.path.getsize(OUTPUT)
    print(f"\n✓ Corpus final : {taille_finale:,} octets → {OUTPUT}")
    print(f"  Estimation tokens BPE : {taille_finale//3:,}")


if __name__ == "__main__":
    main()
