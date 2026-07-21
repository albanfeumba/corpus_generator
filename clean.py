#!/usr/bin/env python3
"""
clean.py — Nettoyage du corpus généré
Usage : python clean.py --input corpus_claude.txt --output corpus_claude_clean.txt
"""

import re
import argparse
import os


def nettoyer(texte: str) -> str:
    # Supprimer les balises markdown résiduelles
    texte = re.sub(r'\*\*(.+?)\*\*', r'\1', texte)
    texte = re.sub(r'\*(.+?)\*',     r'\1', texte)
    texte = re.sub(r'#{1,6}\s',      '',    texte)
    texte = re.sub(r'`{1,3}.*?`{1,3}', '', texte, flags=re.DOTALL)

    # Supprimer URLs et emails
    texte = re.sub(r'https?://\S+', '', texte)
    texte = re.sub(r'\S+@\S+\.\S+', '', texte)

    # Normaliser les espaces et sauts de ligne
    texte = re.sub(r'[ \t]+',  ' ',    texte)
    texte = re.sub(r'\n{3,}',  '\n\n', texte)

    # Supprimer les lignes trop courtes (résidus)
    lignes = texte.split('\n')
    lignes = [l for l in lignes if len(l.strip()) > 10 or l.strip() == '']
    texte  = '\n'.join(lignes)

    return texte.strip()


def main():
    parser = argparse.ArgumentParser(description="Nettoyage du corpus")
    parser.add_argument("--input",  required=True,  help="Fichier d'entrée")
    parser.add_argument("--output", required=True,  help="Fichier de sortie")
    args = parser.parse_args()

    print(f"Lecture de {args.input}...")
    with open(args.input, "r", encoding="utf-8") as f:
        texte = f.read()

    taille_avant = len(texte)
    print(f"Taille avant : {taille_avant:,} caractères")

    texte = nettoyer(texte)

    taille_apres = len(texte)
    print(f"Taille après : {taille_apres:,} caractères")
    print(f"Réduit de    : {(taille_avant-taille_apres)/taille_avant*100:.1f}%")

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(texte)

    print(f"Sauvegardé → {args.output}")


if __name__ == "__main__":
    main()
