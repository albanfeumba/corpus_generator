#!/usr/bin/env python3
import random, requests, argparse, time, os
from topics import TOPICS_ALL
from prompts import PROMPTS

OLLAMA_URL   = "https://psychic-chatting-shaking.ngrok-free.dev"
OLLAMA_KEY   = "alban"
OLLAMA_MODEL = "e2b"

SYSTEM = """Tu écris des données pour entraîner un LLM français.
Texte encyclopédique dense et informatif. 600 à 1200 mots.
Pas de listes. Pas de markdown. Pas de titres.
Style naturel et académique. Toujours en français."""

def generer_texte(instruction, model=OLLAMA_MODEL):
    resp = requests.post(
        f"{OLLAMA_URL}/generate",
        headers={"X-Mac-Mini-Key": OLLAMA_KEY},
        json={"task": "generation", "prompt": SYSTEM + "\n\n" + instruction, "model": model},
        timeout=120
    )
    resp.raise_for_status()
    return resp.json().get("result", "").strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", choices=["claude","gpt","gemini","deepseek","all"], default="all")
    parser.add_argument("--model",  default=OLLAMA_MODEL)
    parser.add_argument("--target", type=int, default=500_000_000)
    parser.add_argument("--output", default=None)
    parser.add_argument("--delay",  type=float, default=0.2)
    args = parser.parse_args()

    if args.domain == "all":
        topics = {}
        for t in TOPICS_ALL.values():
            topics.update(t)
    else:
        topics = TOPICS_ALL[args.domain]

    output_file = args.output or f"corpus_{args.domain}.txt"
    written = 0
    errors  = 0
    start   = time.time()

    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as f:
            written = len(f.read())
        print(f"Reprise depuis {written:,} caractères...")
        f_out = open(output_file, "a", encoding="utf-8")
    else:
        f_out = open(output_file, "w", encoding="utf-8")

    print(f"Modèle : {args.model} | Cible : {args.target:,} | Sortie : {output_file}")
    print("─" * 70)

    while written < args.target:
        try:
            category    = random.choice(list(topics.keys()))
            subject     = random.choice(topics[category])
            instruction = random.choice(PROMPTS).format(subject)
            text        = generer_texte(instruction, args.model)

            if len(text) < 100:
                continue

            sample = f"""### Instruction\n{instruction}\n\n### Réponse\n{text}\n\n"""
            f_out.write(sample)
            f_out.flush()
            written += len(sample)
            errors   = 0

            elapsed = time.time() - start
            speed   = written / elapsed if elapsed > 0 else 1
            eta     = (args.target - written) / speed
            eta_str = f"{int(eta//3600)}h{int((eta%3600)//60)}m"

            print(f"{written:>15,} / {args.target:,} ({written/args.target*100:.2f}%) | "
                  f"⏱ {elapsed/60:.1f}min | ETA {eta_str} | [{category[:20]}] {subject[:25]}")

            time.sleep(args.delay)

        except Exception as e:
            errors += 1
            print(f"Erreur : {e} — attente 5s ({errors})")
            time.sleep(5)
            if errors > 15:
                print("Trop d'erreurs — arrêt")
                break

    f_out.close()
    print(f"\n✓ Terminé : {written:,} caractères → {output_file}")

if __name__ == "__main__":
    main()
