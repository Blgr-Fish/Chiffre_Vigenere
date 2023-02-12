import string
from tkinter import *
from tkinter import ttk 

def chiffrement(val):
    
    global entree1
    
    
    
    def chiffre_vigenere(mot_clair,cle_chiffrement):
        """
        Génère un mot/une phrase chiffrée à l'aide d'un mot clair et d'une clé de chiffrement
    
        Paramètres 
        ----------
        mot_clair : string
                une chaîne de caractère comprenant seulement des lettres de l'alphabet. Les lettres peuvent être
                soit en minuscule soit en majsucule. Le programme les changera en Majuscule dans tous les cas
    
        cle_chiffrement : string 
                une chaîne de caractère comprenant seulement des lettres de l'alphabet. Les lettres peuvent être
                soit en minuscule soit en majsucule. Le programme les changera en Majuscule dans tous les cas
                Il est recommandé d'avoir une clé de chiffrement assez longue pour assurer la sécurité du message.
        """
    
        liste_mot = []                                                                                                 # Une liste qui contiendra le mot chiffré
        longueur_mot = len(mot_clair)                                                                                  # La longueur du mot
   
        mot_split = list(mot_clair)                                                                                    # Le mot coupé en lettres dans une liste
        for char in mot_split :
            assert (ord(char) - 65) >= 0 and (ord(char) - 65) <= 25, "Un des caracteres du mot n'est pas une lettre"
    
        cle_split = list(cle_chiffrement*longueur_mot)                                                                  # On découpe notre clé en petit morceaux 
        for char in cle_split :
            assert (ord(char) - 65) >= 0 and (ord(char) - 65) <= 25, "Un des caracteres de la clé n'est pas une lettre"


        for i in range(longueur_mot):
        
            lettre_modifiee = ord(mot_split[i]) - 65                                                                    # On transforme la lettre en décimal puis on lui soustrait 65 pour travailler entre 0 et 25
            cle_modifiee = ord(cle_split[i]) - 65

            lettre_chiffree = ( lettre_modifiee + cle_modifiee ) % 26                                                   # La lettre chiffrée est la somme des crans de la lettre du mot et celle de clé. Le modulo 26 sert à rester entre 0 et 25
        
            liste_mot.append(chr(lettre_chiffree + 65))                                                                 # On transforme la lettre en caractere avec chr() en lui ajoutant 65 pour qu'elle reprenne sa réelle position

   
        return ''.join(liste_mot)


    def dechiffre_vigenere(mot_chiffre,cle_dechiffrement):
        """
        Génère un mot/une phrase déchiffré à l'aide d'un mot chiffré et d'une clé de déchiffrement
    
        Paramètres 
        ----------
        mot_chiffre : string
                une chaîne de caractère comprenant seulement des lettres de l'alphabet. Les lettres peuvent être
                soit en minuscule soit en majsucule. Le programme les changera en Majuscule dans tous les cas
    
        cle_dechiffrement : string 
                une chaîne de caractère comprenant seulement des lettres de l'alphabet. Les lettres peuvent être
                soit en minuscule soit en majsucule. Le programme les changera en Majuscule dans tous les cas
                Il est recommandé d'avoir une clé de chiffrement assez longue pour assurer la sécurité du message.
        """
    
        liste_mot = []                                                                                                 # Une liste qui contiendra le mot chiffré
        longueur_mot = len(mot_chiffre)                                                                                  # La longueur du mot
   
        mot_split = list(mot_chiffre)                                                                                    # Le mot coupé en lettres dans une liste
        for char in mot_split :
            assert (ord(char) - 65) >= 0 and (ord(char) - 65) <= 25, "Un des caracteres du mot n'est pas une lettre"
    
        cle_split = list(cle_dechiffrement*longueur_mot)                                                                  # On découpe notre clé en petit morceaux 
        for char in cle_split :
            assert (ord(char) - 65) >= 0 and (ord(char) - 65) <= 25, "Un des caracteres de la clé n'est pas une lettre"


        for i in range(longueur_mot):
        
            lettre_modifiee = ord(mot_split[i]) - 65                                                                    # On transforme la lettre en décimal puis on lui soustrait 65 pour travailler entre 0 et 25
            cle_modifiee = ord(cle_split[i]) - 65

            lettre_chiffree = ( lettre_modifiee - cle_modifiee ) % 26                                                   # La lettre chiffrée est la somme des crans de la lettre du mot et celle de clé. Le modulo 26 sert à rester entre 0 et 25
        
            liste_mot.append(chr(lettre_chiffree + 65))                                                                 # On transforme la lettre en caractere avec chr() en lui ajoutant 65 pour qu'elle reprenne sa réelle position

   
        return ''.join(liste_mot)
    
    if val == 0:
        return chiffre_vigenere(str(entree1),'cle')
    else :
        return dechiffre_vigenere(str(entree1),'cle')
    
    


#TESTS

"""mot = input('Mot à chiffrer : ')
cle = input('Cle de chiffrement : ')

choix = input('Chiffrer/Dechiffrer : ')
if choix.upper() == 'chiffrer'.upper() :
    print(chiffre_vigenere(mot.upper().replace(" ", ""),cle.upper().replace(" ", "")))
elif choix.upper() == 'dechiffrer'.upper():
    print(dechiffre_vigenere(mot.upper().replace(" ", ""),cle.upper().replace(" ", "")))
else :
    print("Erreur syntaxe")"""

jeu = Tk()
jeu.title('Chiffreur')
jeu.geometry('600x400')

titre_cadre = Frame(jeu) # Création de l'interface
titre_cadre.pack(padx=5,pady=5,side='top')
titre = Label(titre_cadre,font=("Helvetica",25),text='CHIFFRATOR 2000')
titre.pack(padx=5,pady=5,)

cadre = LabelFrame(jeu,text='Entrée')
cadre.pack(padx=20,pady=5,anchor=W)
entree1 = Entry(cadre)
entree1.pack(padx=5,pady=5)


valeur = IntVar()

boutton0 = Radiobutton(jeu,variable=valeur,value=0,text="Chiffrer")
boutton0.pack(padx=5,pady=5,anchor=W)
boutton1 = Radiobutton(jeu,variable=valeur,value=1,text="Déchiffrer")
boutton1.pack(padx=5,pady=5,anchor=W)



dechiffre_cadre = Frame(jeu)
dechiffre_cadre.pack(padx=5,pady=5,anchor=W)

boutton_sortie =Button(dechiffre_cadre,text='Appuyer',command=chiffrement(valeur))




cadre2 =LabelFrame(jeu,text='Sortie')
cadre2.pack(padx=20,pady=5,anchor=W)

entree2 = Entry(cadre2)
entree2.pack(padx=5,pady=5)


jeu.mainloop() # le programme tourne non-stop ok











