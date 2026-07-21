# Générateur de Corpus LLM — 2 Milliards de Caractères

## Architecture

```
corpus_generator/
├── topics.py        ← Tous les sujets pour les 4 modèles
├── prompts.py       ← 30 templates de questions
├── generate.py      ← Génération via OpenRouter
├── clean.py         ← Nettoyage du corpus
├── deduplicate.py   ← Suppression des doublons
├── merge.py         ← Fusion des 4 corpus
└── README.md
```

---

## Configuration

```bash
# Installer les dépendances
pip install requests

# Définir la clé OpenRouter
export OPENROUTER_API_KEY="sk-or-votre-cle"
```

---

## Lancer la génération pour chaque modèle

### Claude — Science / Philosophie / Médecine
```bash
python generate.py --model claude --target 500000000 --output corpus_claude.txt
```

### GPT — Histoire / Géopolitique / Droit
```bash
python generate.py --model gpt --target 500000000 --output corpus_gpt.txt
```

### Gemini — Technologie / Économie / Environnement
```bash
python generate.py --model gemini --target 500000000 --output corpus_gemini.txt
```

### DeepSeek — Littérature / Art / Culture / Société
```bash
python generate.py --model deepseek --target 500000000 --output corpus_deepseek.txt
```

---

## Pipeline complet

```bash
# 1. Générer les 4 corpus (peut tourner en parallèle)
python generate.py --model claude   --target 500000000 &
python generate.py --model gpt      --target 500000000 &
python generate.py --model gemini   --target 500000000 &
python generate.py --model deepseek --target 500000000 &
wait

# 2. Nettoyer chaque corpus
python clean.py --input corpus_claude.txt   --output corpus_claude_clean.txt
python clean.py --input corpus_gpt.txt      --output corpus_gpt_clean.txt
python clean.py --input corpus_gemini.txt   --output corpus_gemini_clean.txt
python clean.py --input corpus_deepseek.txt --output corpus_deepseek_clean.txt

# 3. Dédupliquer
python deduplicate.py --input corpus_claude_clean.txt   --output corpus_claude_dedup.txt
python deduplicate.py --input corpus_gpt_clean.txt      --output corpus_gpt_dedup.txt
python deduplicate.py --input corpus_gemini_clean.txt   --output corpus_gemini_dedup.txt
python deduplicate.py --input corpus_deepseek_clean.txt --output corpus_deepseek_dedup.txt

# 4. Fusionner
python merge.py
```

---

## Résultat attendu

```
corpus_claude.txt    →  500M caractères  (Science/Philo/Médecine)
corpus_gpt.txt       →  500M caractères  (Histoire/Géopolitique/Droit)
corpus_gemini.txt    →  500M caractères  (Tech/Économie/Environnement)
corpus_deepseek.txt  →  500M caractères  (Littérature/Art/Culture)
─────────────────────────────────────────────────────────────
corpus_final_2B.txt  → 2 000M caractères (~120M tokens BPE)
```

---

## Estimation du coût OpenRouter

```
~800 mots / réponse × 1.33 tokens/mot = ~1066 tokens output
500M chars / 800 chars/réponse = ~625 000 réponses par modèle

Claude Opus  : ~625K × $0.015/1K tokens = ~$9 375
GPT-4o       : ~625K × $0.015/1K tokens = ~$9 375
Gemini Pro   : ~625K × $0.003/1K tokens = ~$1 875
DeepSeek R1  : ~625K × $0.002/1K tokens = ~$1 250

Total estimé : ~$22 000 pour 2 milliards de caractères
```

**Conseil** : utiliser des modèles moins chers pour les premiers tests.
Remplacer `claude-opus-4-6` par `claude-haiku-4-5-20251001` divise le coût par 20.

---

## Options pour réduire le coût

```python
# Dans generate.py, remplacer les modèles par :
MODELS = {
    "claude":   "anthropic/claude-haiku-4-5-20251001",  # 20x moins cher
    "gpt":      "openai/gpt-4o-mini",                   # 10x moins cher
    "gemini":   "google/gemini-flash-1.5",               # très économique
    "deepseek": "deepseek/deepseek-chat",                # très économique
}
```
