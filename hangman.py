import getpass
import random

francais = [
    #chatgpt-made list cause i couldn't make my file system work :(

"chat","chien","éléphant","girafe","kangourou","dauphin","baleine","tigre","lion","ours",
"loup","singe","zèbre","cheval","renard","lapin","panda","chameau","loutre","rhinocéros",
"écureuil","guépard","léopard","pingouin","phoque","crocodile","alligator","buffle","orignal","renne",
"cerf","hyène","blaireau","castor","rat","souris","chauve-souris","hérisson","porc-épic","tortue",
"aigle","faucon","hibou","perroquet","moineau","paon","flamant","corbeau","goéland","pigeon",
"colombe","papillon","abeille","fourmi","guêpe","libellule","moustique","requin","pieuvre","calmar",
"crabe","homard","méduse","étoile de mer","hippocampe","morse","lamantin","narval","ornithorynque","tatou",
"paresseux","koala","lémurien","chimpanzé","orang-outan","gorille","âne","buffle","yak","bison",
"orignal","éland","kangourou","wallaby","daman","furet","loutre","tortue","lézard","serpent",
"ordinateur","clavier","écran","souris","imprimante","téléphone","appareil photo","télévision","sac à dos","chaise",
"table","lampe","cahier","lunettes","crayon","bouteille","horloge","montre","portefeuille","parapluie",
"chaussure","chapeau","écharpe","veste","bague","collier","livre","magazine","canapé","coussin",
"miroir","tasse","assiette","fourchette","cuillère","couteau","balai","brosse","brosse à dents","projecteur",
"enceinte","microphone","tablette","chargeur","ventilateur","routeur","switch","modem","bougie","chauffage",
"aspirateur","blender","cuisinière","four","réfrigérateur","congélateur","poêle","casserole","seau","échelle",
"corde","clou","marteau","tournevis","clé","serrure","pince","perceuse","ruban","papier",
"enveloppe","agrafeuse","dossier","classeur","calepin","calculatrice","ciseaux","colle","peinture","toile",
"pinceau","oreiller","couverture","rideau","tapis","étagère","placard","porte","fenêtre","stylo",
"france","allemagne","brésil","canada","inde","chine","japon","mexique","italie","espagne",
"portugal","norvège","suède","egypte","nigeria","australie","argentine","chili","pérou","colombie",
"russie","ukraine","pologne","finlande","danemark","irlande","écosse","pays de galles","turquie","grèce",
"thailande","vietnam","malaisie","indonésie","pakistan","bangladesh","népal","sri lanka","iraq","iran",
"arabie saoudite","maroc","tunisie","kenya","afrique du sud","zimbabwe","éthiopie","ouganda","ghana","tanzanie",
"cuba","haïti","jamaïque","venezuela","équateur","bolivie","uruguay","paraguay","panama","costa rica",
"israel","jordanie","liban","syrie","koweït","oman","qatar","uae","bahreïn","corée du sud",
"corée du nord","mongolie","kazakhstan","ouzbekistan","turkménistan","kirghizistan","tadjikistan","afghanistan","myanmar","philippines",
"courir","sauter","nager","voler","lire","écrire","dessiner","chanter","danser","cuisiner",
"dormir","penser","jouer","écouter","regarder","conduire","construire","voyager","apprendre","enseigner",
"peindre","grimper","skier","patiner","surfer","creuser","attraper","lancer","cacher","chercher",
"marcher","ramper","sprinter","jogger","crier","chuchoter","hurler","rire","pleurer","respirer",
"cligner","sourire","froncer","embrasser","secouer","pousser","tirer","soulever","laisser","attraper",
"donner","frapper","couper","trancher","mélanger","mesurer","verser","bouillir","frire","cuire",
"laver","nettoyer","repasser","balayer","passer l'aspirateur","laver","épousseter","planter","récolter","arroser",
"heureux","triste","fâché","excité","grand","petit","gros","mince","rapide","lent",
"lumineux","sombre","drôle","sérieux","fort","faible","froid","chaud","doux","amer",
"épicé","dur","mou","rond","carré","long","court","étroit","large","propre",
"sale","riche","pauvre","jeune","vieux","neuf","ancien","moderne","amical","hostile",
"poli","impoli","beau","laid","paresseux","actif","courageux","timide","intelligent","bête",
"chanceux","malchanceux","silencieux","bruyant","calme","orageux","doux","rugueux","fiable","traître",
"pomme","banane","orange","raisin","pastèque","fraise","ananas","mangue","kiwi","citron",
"lime","pêche","poire","prune","cerise","myrtille","framboise","noix de coco","papaye","avocat",
"carotte","pomme de terre","tomate","oignon","poivron","fromage","pain","gâteau","chocolat","beurre",
"lait","yaourt","œuf","riz","pâtes","nouilles","pizza","hamburger","sandwich","soupe",
"steak","poulet","poisson","crevette","homard","huître","salade","épinard","laitue","chou",
"brocoli","chou-fleur","maïs","pois","haricots","lentilles","piment","ail","gingembre","herbes",
"épices","sucre","sel","poivre","huile","vinaigre","sauce","ragoût","curry","bouillon",
"rouge","bleu","vert","jaune","violet","orange","noir","blanc","rose","marron",
"gris","cyan","magenta","indigo","turquoise","beige","bordeaux","or","argent","bronze",
"pêche","lavande","crème","olive","menthe","cerise","lime","marine","sarcelle","corail",
"aigue-marine","saumon","prune","abricot","brun","kaki","charbon","fuchsia","ivoire","mahogany",
"saphir","rubis","émeraude","topaze","ambre","onyx","jade","or","argent","bronze",
"algorithme","python","pendu","programmation","internet","science","éducation","robot","capteur","réseau",
"serveur","base de données","clavier","écran","logiciel","matériel","application","système","appareil","circuit",
"tension","courant","énergie","force","mouvement","gravité","atome","molécule","cellule","gène",
"physique","chimie","biologie","astronomie","géologie","mathématiques","ingénierie","technologie","robotique","intelligence",
"artificielle","machine","apprentissage","neural","circuit","programme","code","déboguer","compiler","exécuter",
"univers","galaxie","planète","océan","montagne","forêt","désert","volcan","rivière","vallée",
"pluie","neige","orage","vent","nuage","feu","terre","sable","roche","pierre",
"lumière","ombre","rêve","idée","esprit","cœur","âme","temps","espace","mémoire",
"musique","chanson","mélodie","poème","histoire","roman","peinture","sculpture","danse","théâtre",
"aventure","voyage","quête","bataille","héros","méchant","magie","puzzle","mystère","secret",
"amour","amitie","famille","joie","tristesse","colère","peur","courage","honneur","gloire",
"liberté","égalité","fraternité","justice","vérité","mensonge","paix","guerre","victoire","défaite",
"succès","échec","espoir","désespoir","confiance","trahison","loyauté","tristesse","bonheur","malheur",
"richesse","pauvreté","santé","maladie","force","faiblesse","beauté","laideur","chance","malchance",
"chanceux","malchanceux","sagesse","folie","éducation","travail","jeu","loisir","fête","rêver"
]

english = [
"cat","dog","elephant","giraffe","kangaroo","dolphin","whale","tiger","lion","bear",
"wolf","monkey","zebra","horse","fox","rabbit","panda","camel","otter","rhino",
"squirrel","cheetah","leopard","penguin","seal","crocodile","alligator","buffalo","moose","reindeer",
"deer","hyena","badger","beaver","rat","mouse","bat","hedgehog","porcupine","tortoise",
"eagle","hawk","owl","parrot","sparrow","peacock","flamingo","crow","raven","seagull",
"pigeon","dove","falcon","caterpillar","butterfly","bee","ant","wasp","dragonfly","mosquito",
"shark","octopus","squid","crab","lobster","jellyfish","starfish","clam","oyster","seahorse",
"walrus","manatee","narwhal","platypus","armadillo","sloth","koala","lemur","chimpanzee","orangutan",
"gorilla","donkey","buffalo","yak","bison","moose","elk","kangaroo","wallaby","hyrax",

"computer","keyboard","monitor","mouse","printer","phone","camera","television","backpack","chair",
"table","lamp","notebook","glasses","pencil","bottle","clock","watch","wallet","umbrella",
"shoe","hat","scarf","jacket","ring","necklace","book","magazine","sofa","cushion",
"mirror","cup","plate","fork","spoon","knife","broom","brush","toothbrush","projector",
"speaker","microphone","tablet","charger","fan","router","switch","modem","lamp","candle",
"fan","heater","vacuum","blender","stove","oven","fridge","freezer","pan","pot",
"bucket","ladder","rope","nail","hammer","screwdriver","wrench","pliers","drill","tape",
"paper","envelope","stapler","folder","clipboard","calculator","scissors","glue","paint","canvas",
"brush","pillow","blanket","curtain","mat","rug","shelf","cabinet","door","window",
"key","lock","pen","marker","highlighter","eraser","chalk","board","notepad","lamp",

"france","germany","brazil","canada","india","china","japan","mexico","italy","spain",
"portugal","norway","sweden","egypt","nigeria","australia","argentina","chile","peru","colombia",
"russia","ukraine","poland","finland","denmark","ireland","scotland","wales","turkey","greece",
"thailand","vietnam","malaysia","indonesia","pakistan","bangladesh","nepal","sri lanka","iraq","iran",
"saudiarabia","morocco","tunisia","kenya","southafrica","zimbabwe","ethiopia","uganda","ghana","tanzania",
"cuba","haiti","jamaica","venezuela","ecuador","bolivia","uruguay","paraguay","panama","costarica",
"israel","jordan","lebanon","syria","iraq","kuwait","oman","qatar","uae","bahrain",
"southkorea","northkorea","mongolia","kazakhstan","uzbekistan","turkmenistan","kyrgyzstan","tajikistan","afghanistan","myanmar",
"philippines","singapore","laos","cambodia","brunei","maldives","bhutan","taiwan","hongkong","macau",
"newzealand","fiji","samoa","tonga","papuanewguinea","solomonislands","vanuatu","kiribati","marshallislands","micronesia",

"run","jump","swim","fly","read","write","draw","sing","dance","cook",
"sleep","think","play","listen","watch","drive","build","travel","learn","teach",
"paint","climb","ski","skate","surf","dig","catch","throw","hide","seek",
"walk","crawl","sprint","jog","yell","whisper","shout","laugh","cry","breathe",
"blink","smile","frown","hug","kiss","shake","push","pull","lift","drop",
"grab","kick","punch","tap","knock","open","close","turn","slide","spin",
"cut","slice","stir","mix","measure","pour","boil","fry","bake","grill",
"wash","clean","iron","sweep","vacuum","mop","dust","plant","harvest","water",
"dig","build","repair","destroy","fix","paint","draw","write","read","calculate",
"program","design","plan","organize","teach","learn","study","solve","analyze","compare",
"observe","record","measure","weigh","count","estimate","predict","guess","decide","choose",

"happy","sad","angry","excited","tall","short","big","small","fast","slow",
"bright","dark","funny","serious","strong","weak","cold","hot","sweet","sour",
"spicy","bitter","soft","hard","round","square","long","short","narrow","wide",
"clean","dirty","rich","poor","young","old","new","ancient","modern","friendly",
"hostile","polite","rude","beautiful","ugly","lazy","active","brave","shy","clever",
"smart","dumb","lucky","unlucky","quiet","noisy","calm","stormy","gentle","rough",
"happy","sad","angry","tired","sleepy","hungry","thirsty","bored","curious","excited",
"proud","ashamed","jealous","lonely","friendly","mean","kind","cruel","graceful","clumsy",
"strong","weak","bold","timid","optimistic","pessimistic","honest","dishonest","loyal","faithful",

"apple","banana","orange","grape","watermelon","strawberry","pineapple","mango","kiwi","lemon",
"lime","peach","pear","plum","cherry","blueberry","raspberry","coconut","papaya","avocado",
"carrot","potato","tomato","onion","pepper","cheese","bread","cake","chocolate","butter",
"milk","yogurt","egg","rice","pasta","noodles","pizza","hamburger","sandwich","soup",
"steak","chicken","fish","shrimp","lobster","oyster","salad","spinach","lettuce","cabbage",
"broccoli","cauliflower","corn","peas","beans","lentils","chili","garlic","ginger","herbs",
"spices","sugar","salt","pepper","oil","vinegar","sauce","soup","stew","curry",
"noodle","dumpling","bread","muffin","bagel","croissant","waffle","pancake","toast","pie",

"red","blue","green","yellow","purple","orange","black","white","pink","brown",
"gray","cyan","magenta","violet","indigo","turquoise","beige","maroon","gold","silver",
"bronze","peach","lavender","cream","olive","mint","cherry","lime","navy","teal",
"coral","aqua","salmon","plum","apricot","tan","khaki","charcoal","fuchsia","cream",
"cerulean","ivory","mahogany","sapphire","ruby","emerald","topaz","amber","onyx","jade",

"algorithm","python","hangman","programming","internet","science","education","robot","sensor","network",
"server","database","keyboard","monitor","software","hardware","application","system","device","circuit",
"voltage","current","energy","force","motion","gravity","atom","molecule","cell","gene",
"physics","chemistry","biology","astronomy","geology","mathematics","engineering","technology","robotics","artificial",
"intelligence","machine","learning","neural","circuit","program","code","debug","compile","execute",

"universe","galaxy","planet","ocean","mountain","forest","desert","volcano","river","valley",
"rain","snow","storm","wind","cloud","fire","earth","sand","rock","stone",
"light","shadow","dream","idea","mind","heart","soul","time","space","memory",
"music","song","melody","poem","story","novel","painting","sculpture","dance","theater",
"adventure","journey","quest","battle","hero","villain","magic","puzzle","mystery","secret"
]


def print_hangman(lives):
    stages = [
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
             |
             |
             |
             |
        =========
        """
    ]

    lives = max(0, min(6, lives))
    print(stages[lives])
prompts = {
        "fr": "Quelle lettre voulez-vous essayer ? ",
        "en": "Which letter do you want to try? "
    }
messages = {
        "one_letter": {
            "fr": "Il ne faut entrer qu'une seule lettre !",
            "en": "You must enter only one letter!"
        },
        "win": {
            "fr": "C'est gagné !",
            "en": "You win!"
        },
        "lose": {
            "fr": "C'est perdu :(",
            "en": "You lost :("
        },
        "lives_left": {
            "fr": "Il vous reste {} vies sur 6 !",
            "en": "You have {} lives left out of 6!"
        },
        "the_word": {
            "fr": "Le mot était : {}.",
            "en": "The word was: {}."
        },
        "play_again": {
            "fr": "Voulez-vous rejouer ? ",
            "en": "Do you want to play again ? "
        },
        "invalid_arg": {
            "fr": "Veuillez choisir 1 ou 2!",
            "en": "Please chose either 1 or 2!"
        }

    }

def test_win(mot, res):
    test = ""
    for i in range(len(res)):
        test = test + (res[i])
    if test == mot:
        return True
    else:
        return False

def main(lives, mot, res, lang):
    test = input(prompts[lang])
    if len(test) != 1:
        print(messages["one_letter"][lang])
        main(lives, mot, res, lang)
        return

    correct = False
    for i in range(len(mot)):
        if mot[i] == test:
            res[i] = test
            correct = True
    if not correct:
        lives -= 1

    if test_win(mot, res):
        print(messages["win"][lang])
        print(messages["lives_left"][lang].format(lives))
        print(messages["the_word"][lang].format(mot))
        replay = input(messages["play_again"][lang])
        if replay == "oui" or replay == "yes":
            start()
        return

    print_hangman(lives)

    if lives == 0:
        print(messages["lose"][lang])
        print(messages["the_word"][lang].format(mot))
        return

    print(" ".join(res))
    print("\n")
    main(lives, mot, res, lang)

def start():
    lang_choice = input("Choose language / Choisissez la langue (fr/en): ").lower()
    if lang_choice not in ["fr", "en"]:
        lang_choice = "fr"

    prompts_start = {
        "fr": "Voulez-vous jouer contre : 1, un mot aléatoire ou 2, un autre joueur en local ? ",
        "en": "Do you want to play against: 1, a random word or 2, another local player? "
    }

    mots = francais if lang_choice == "fr" else english

    choix = input(prompts_start[lang_choice])
    if choix == "1":
        mot = random.choice(mots)
        res = ["_"] * len(mot)
        print(" ".join(res))
        print("\n")
        main(6, mot, res, lang_choice)
    elif choix == 2:
        prompts_player = {
            "fr": "Joueur 1, choisissez le mot secret : ",
            "en": "Player 1, choose the secret word: "
        }
        mot = getpass.getpass(prompts_player[lang_choice])
        print("\n" * 50)
        res = ["_"] * len(mot)
        print(" ".join(res))
        print("\n")
        main(6, mot, res, lang_choice)
    else :
        print(messages["invalid_arg"][lang_choice])
        start()

start()