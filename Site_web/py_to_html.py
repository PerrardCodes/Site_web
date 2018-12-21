import test_affichage
import os
import glob

message = test_affichage.index()

try:
    os.remove('index.html')
except:
    print('No index.html file present')
fichier = open("index.html", "a")
fichier.write(message)
fichier.close()
