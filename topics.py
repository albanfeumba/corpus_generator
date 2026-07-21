# topics.py — Tous les sujets pour les 4 modèles
# Claude : Science / Philosophie / Médecine
# GPT    : Histoire / Géopolitique / Droit
# Gemini : Technologie / Économie / Environnement
# DeepSeek : Littérature / Art / Culture / Société

TOPICS_CLAUDE = {
    "Physique": [
        "mécanique quantique", "relativité générale", "thermodynamique",
        "électromagnétisme", "physique des particules", "mécanique classique",
        "optique", "physique nucléaire", "cosmologie", "astrophysique",
        "physique du solide", "supraconductivité", "chaos déterministe",
        "physique statistique", "ondes et vibrations", "mécanique des fluides",
        "physique du plasma", "antimatière", "trous noirs", "matière noire"
    ],
    "Chimie": [
        "chimie organique", "chimie inorganique", "électrochimie",
        "chimie quantique", "thermochimie", "chimie des polymères",
        "catalyse", "réactions acide-base", "liaisons chimiques",
        "chimie verte", "spectroscopie", "chimie atmosphérique",
        "cristallographie", "chimie des matériaux", "photochimie"
    ],
    "Biologie": [
        "génétique", "évolution darwinienne", "écologie", "biochimie",
        "microbiologie", "neurobiologie", "immunologie", "embryologie",
        "biologie cellulaire", "biologie moléculaire", "épigénétique",
        "biodiversité", "biologie marine", "mycologie", "virologie",
        "parasitologie", "éthologie", "biologie des systèmes"
    ],
    "Mathématiques": [
        "analyse mathématique", "algèbre linéaire", "géométrie",
        "probabilités", "statistiques", "topologie", "théorie des nombres",
        "calcul différentiel", "théorie des graphes", "logique mathématique",
        "équations différentielles", "théorie des ensembles", "algèbre abstraite",
        "géométrie différentielle", "analyse complexe", "théorie des catégories"
    ],
    "Philosophie": [
        "métaphysique", "épistémologie", "éthique", "philosophie du langage",
        "philosophie de l'esprit", "philosophie politique", "esthétique",
        "existentialisme", "phénoménologie", "stoïcisme", "empirisme",
        "rationalisme", "pragmatisme", "philosophie des sciences",
        "philosophie morale", "bioéthique", "philosophie de la religion",
        "philosophie analytique", "herméneutique", "philosophie sociale"
    ],
    "Médecine": [
        "cardiologie", "neurologie", "oncologie", "immunologie clinique",
        "génétique médicale", "pharmacologie", "chirurgie", "psychiatrie",
        "médecine interne", "infectiologie", "endocrinologie", "rhumatologie",
        "pneumologie", "médecine de précision", "santé publique",
        "dermatologie", "ophtalmologie", "pédiatrie", "gériatrie",
        "médecine d'urgence", "anesthésiologie", "radiologie"
    ],
    "Neurosciences": [
        "plasticité cérébrale", "mémoire", "conscience", "sommeil",
        "neurodégénérescence", "synapse", "neurotransmetteurs",
        "cortex cérébral", "système limbique", "cervelet",
        "neuroimagerie", "cognition", "perception", "attention",
        "langage et cerveau", "émotions et neurologie"
    ],
    "Astronomie": [
        "système solaire", "étoiles", "galaxies", "nébuleuses",
        "exoplanètes", "cosmologie observationnelle", "télescopes",
        "ondes gravitationnelles", "rayonnement cosmologique",
        "formation planétaire", "astéroïdes", "comètes"
    ]
}

TOPICS_GPT = {
    "Histoire mondiale": [
        "Égypte antique", "Empire romain", "Empire byzantin",
        "Empire ottoman", "Moyen Âge européen", "Renaissance",
        "Révolution française", "Révolution industrielle",
        "Première Guerre mondiale", "Seconde Guerre mondiale",
        "Guerre froide", "Décolonisation", "Empire mongol",
        "Civilisation maya", "Civilisation aztèque", "Civilisation chinoise",
        "Civilisation indienne", "Civilisation perse", "Empire carolingien",
        "Croisades", "Réforme protestante", "Absolutisme monarchique",
        "Grèce antique", "Phénicie", "Empire assyrien", "Rome républicaine",
        "Révolution américaine", "Révolution russe", "Guerre d'Espagne"
    ],
    "Géopolitique": [
        "OTAN", "ONU", "Union européenne", "ASEAN", "BRICS", "G20",
        "conflit israélo-palestinien", "guerre en Ukraine", "mer de Chine méridionale",
        "Arctique", "Afrique subsaharienne", "relations Chine États-Unis",
        "Russie", "diplomatie multilatérale", "puissances émergentes",
        "énergie et géopolitique", "migrations internationales",
        "terrorisme international", "prolifération nucléaire",
        "soft power", "hard power", "guerre hybride", "cyberguerre"
    ],
    "Droit": [
        "Constitution", "séparation des pouvoirs", "état de droit",
        "droits fondamentaux", "droit international humanitaire",
        "Cour pénale internationale", "justice constitutionnelle",
        "parlement", "présidence", "liberté d'expression",
        "démocratie représentative", "droit du travail", "droit pénal",
        "droit civil", "propriété intellectuelle", "droit européen",
        "droit des réfugiés", "droit de l'environnement",
        "droit constitutionnel comparé", "protection des données"
    ],
    "Institutions internationales": [
        "Banque mondiale", "FMI", "OMC", "UNESCO", "OMS",
        "Cour internationale de justice", "Conseil de sécurité",
        "Parlement européen", "Commission européenne", "OCDE",
        "Tribunal pénal international", "Conseil des droits de l'homme"
    ],
    "Histoire de France": [
        "Ancien Régime", "Révolution française", "Napoléon Bonaparte",
        "IIIe République", "Vichy", "Résistance française",
        "IVe République", "Ve République", "Mai 68",
        "construction européenne", "décolonisation française"
    ]
}

TOPICS_GEMINI = {
    "Intelligence artificielle": [
        "apprentissage automatique", "deep learning", "réseaux de neurones",
        "traitement du langage naturel", "vision par ordinateur",
        "reinforcement learning", "transformers", "grands modèles de langage",
        "éthique de l'IA", "IA générative", "robotique", "automatisation",
        "IA et emploi", "biais algorithmiques", "explicabilité de l'IA",
        "IA et créativité", "IA et médecine", "IA et droit"
    ],
    "Technologie": [
        "informatique quantique", "blockchain", "Internet des objets",
        "cybersécurité", "cloud computing", "5G et 6G", "réalité virtuelle",
        "réalité augmentée", "semiconducteurs", "nanotechnologie",
        "énergie solaire", "batteries lithium-ion", "hydrogène vert",
        "biotechnologie", "impression 3D", "métavers", "edge computing",
        "informatique neuromorphique", "ordinateurs moléculaires"
    ],
    "Économie": [
        "capitalisme", "keynésianisme", "mondialisation", "inégalités économiques",
        "finance comportementale", "marchés financiers", "banques centrales",
        "inflation", "politique monétaire", "fiscalité internationale",
        "développement durable", "économie numérique", "cryptomonnaies",
        "revenu universel de base", "économie du partage", "décroissance",
        "économie comportementale", "théorie des jeux", "microéconomie"
    ],
    "Environnement": [
        "réchauffement climatique", "énergies renouvelables", "biodiversité",
        "déforestation", "pollution plastique", "acidification des océans",
        "transition énergétique", "agriculture durable", "eau douce",
        "villes durables", "économie circulaire", "empreinte carbone",
        "zones humides", "désertification", "pollutions atmosphériques",
        "effondrement écologique", "géoingénierie", "capture du carbone"
    ],
    "Sciences de l'ingénieur": [
        "aérospatiale", "génie civil", "génie électrique", "robotique industrielle",
        "matériaux composites", "génie chimique", "génie biomédical",
        "automatique et contrôle", "mécatronique", "ingénierie des systèmes"
    ]
}

TOPICS_DEEPSEEK = {
    "Littérature française": [
        "Victor Hugo", "Marcel Proust", "Albert Camus", "Gustave Flaubert",
        "Émile Zola", "Simone de Beauvoir", "Jean-Paul Sartre", "Molière",
        "Racine", "Voltaire", "Balzac", "Maupassant", "Rimbaud", "Baudelaire",
        "romantisme français", "naturalisme", "surréalisme", "existentialisme",
        "nouveau roman", "Stendhal", "La Fontaine", "Montaigne", "Rousseau"
    ],
    "Littérature mondiale": [
        "Shakespeare", "Dostoïevski", "Tolstoï", "Kafka", "García Márquez",
        "Toni Morrison", "Haruki Murakami", "Chinua Achebe", "Cervantes",
        "Dante", "Homère", "réalisme magique", "modernisme littéraire",
        "Goethe", "Virginia Woolf", "James Joyce", "Borges", "Beckett",
        "Orwell", "Huxley", "littérature africaine", "littérature asiatique"
    ],
    "Art et culture": [
        "Renaissance artistique", "impressionnisme", "cubisme", "art contemporain",
        "architecture gothique", "baroque", "Bauhaus", "photographie",
        "cinéma", "jazz", "musique classique", "opéra", "danse contemporaine",
        "sculpture", "design", "gastronomie française", "patrimoine culturel",
        "art abstrait", "pop art", "street art", "art numérique",
        "théâtre", "danse classique", "arts plastiques"
    ],
    "Société et sociologie": [
        "sociologie urbaine", "migrations", "féminisme", "droits humains",
        "racisme systémique", "laïcité", "multiculturalisme", "famille",
        "éducation", "religion", "médias", "réseaux sociaux", "jeunesse",
        "vieillissement démographique", "travail et société", "loisirs",
        "sport et société", "tourisme", "consommation", "identité culturelle"
    ],
    "Anthropologie et culture": [
        "anthropologie culturelle", "rites et traditions", "mythologie grecque",
        "mythologie nordique", "mythologie égyptienne", "chamanisme",
        "organisation sociale", "langage et culture", "anthropologie physique",
        "ethnologie", "folklore", "patrimoine immatériel"
    ],
    "Psychologie": [
        "psychologie cognitive", "psychanalyse", "psychologie sociale",
        "développement de l'enfant", "psychologie positive", "mémoire",
        "émotions", "motivation", "personnalité", "troubles mentaux",
        "thérapies cognitivo-comportementales", "psychologie du sport"
    ]
}

# Dictionnaire global — choisir selon le modèle
TOPICS_ALL = {
    "claude":   TOPICS_CLAUDE,
    "gpt":      TOPICS_GPT,
    "gemini":   TOPICS_GEMINI,
    "deepseek": TOPICS_DEEPSEEK,
}
