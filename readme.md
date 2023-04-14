Utilisation:
-
-
-

1- Télécharger  python (a ce momment j'utilise la version 3.11.3)
    https://www.python.org/downloads/



2 - ouvrez un terminal/invite de commande et accedez au dossier du projet: 


pour ouvrir une invite de commande sur WINDOWS :
    appuyer sur les touches windows+r et taper cmd ou taper cmd dans la barre de recherche windows 

sur macOS : 
    touche command+espace et taper terminal
    
        cd chemin/de/mon/projet

vous pouvez aussi utiliser le terminal de votre editeur de code si vous en avez un




3 - installer les bibliotheques requises:

    pip install openai gtts pygame pydub python-dotenv




5 - creer un compte sur openai et creer votre clé API https://platform.openai.com/account/api-keys et la copier dans le fichier "exemple.env.txt"   
    renommer le fichier "exemple.env.txt" en ".env" 
    



5 - lancer le fichier gpt-tts.py
    
    python gpt-tts.py







"Si vous rencontrez des erreur apres ces etapes vous pouvez suivre la demarche si dessous (utile aussi pour ceux qui ont deja python et des bibliotheques d'installées, cela permet d'eviter des problemmes de compatibilité)"


essayer d'utilisé un environnement virtuel:
pour creer un environement virtuel

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
