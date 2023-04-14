Utilisation


1- Télécharger  python (a ce momment j'utilise la version 3.11.3)
    https://www.python.org/downloads/

    - ouvrez un terminal/invite de commande et accedez au dossier du projet: 
    
        cd chemin/de/mon/projet


2 - installer les bibliotheques:

    pip install openai gtts pygame pydub python-dotenv


3 - creer un compte sur openai et creer votre clé API https://platform.openai.com/account/api-keys et la copier dans le fichier "exemple.env.txt"   
    renommer le fichier "exemple.env.txt" en ".env" 
    


4 - lancer le fichier gpt-tts.py
    
    python gpt-tts.py


Si vous rencontrez des erreur apres ces etapes vous pouvez suivre la demarche si dessous (utile aussi pour ceux qui ont deja python et des bibliotheques d'installer, cela permet d'eviter des probleme de compatibilité) 


vous rencontrez des difficultés a lancé ce script essayer d'utilisé un environnement virtuel, pour creer un environement virtuel

    python -m venv myvenv

Activez l'environnement virtuel. La méthode pour activer l'environnement dépend de l'interpréteur de commandes que vous utilisez :

SUR WINDOWS:

si vous utiliser l'invite de commandes (cmd) :

    myvenv\Scripts\activate.bat

si vous utiliser PowerShell :

    .\myvenv\Scripts\Activate

SUR MACOS:

dans le terminal:

    source venvGPT/bin/activate

Installer les bibliotheque dans votre environement virtuel
    
    pip install openai gtts pygame pydub python-dotenv

Lancer le script:
    gpt.tts.py

Si vous souhaiter quitter l'environnement virtuel:
    deactivate
