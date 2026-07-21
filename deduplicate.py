#!/usr/bin/env python3
"""
deduplicate.py — Suppression des doublons dans le corpus
Usage : python deduplicate.py --input corpus_clean.txt --output corpus_dedup.txt
"""

import argparse
import hashlib
import re


def extraire_blocs(texte: str) -> list[dict]:
    """Extrait les blocs ### Instruction / ### Réponse."""
    pattern = r'### Instruction\n(.*?)\n\n### Réponse\n(.*?)(?=\n### Instruction|\Z)'
    blocs   = []
    for m in re.finditer(pattern, texte, re.DOTALL):
        instruction = m.group(1).strip()
        reponse     = m.group(2).strip()
        # Hash de la réponse pour détecter les doublons
        hash_rep = hashlib.md5(reponse[:200].encode()).hexdigest()
        blocs.append({
            "instruction": instruction,
            "reponse":     reponse,
            "hash":        hash_rep,
            "texte":       m.group(0)
        })
    return blocs


def main():
    parser = argparse.ArgumentParser(description="Déduplication du corpus")
    parser.add_argument("--input",    required=True,  help="Fichier d'entrée")
    parser.add_argument("--output",   required=True,  help="Fichier de sortie")
    parser.add_argument("--min-chars", type=int, default=200,
                        help="Longueur minimum d'une réponse")
    args = parser.parse_args()

    print(f"Lecture de {args.input}...")
    with open(args.input, "r", encoding="utf-8") as f:
        texte = f.read()

    blocs = extraire_blocs(texte)
    print(f"Blocs trouvés   : {len(blocs):,}")

    # Déduplication
    vus      = set()
    uniques  = []
    doublons = 0
    courts   = 0

    for bloc in blocs:
        if len(bloc["reponse"]) < args.min_chars:
            courts += 1
            continue
        if bloc["hash"] in vus:
            doublons += 1
            continue
        vus.add(bloc["hash"])
        uniques.append(bloc)

    print(f"Doublons supprimés : {doublons:,}")
    print(f"Trop courts        : {courts:,}")
    print(f"Blocs uniques      : {len(uniques):,}")

    with open(args.output, "w", encoding="utf-8") as f:
        for bloc in uniques:
            f.write(f"### Instruction\n{bloc['instruction']}\n\n")
            f.write(f"### Réponse\n{bloc['reponse']}\n\n")

    taille = sum(len(b['instruction']) + len(b['reponse']) for b in uniques)
    print(f"Taille finale : {taille:,} caractères → {args.output}")


if __name__ == "__main__":
    main()
