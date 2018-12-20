import test_affichage

message = test_affichage.index()
fichier = open("index.html", "a")
fichier.write(message)
fichier.close()
