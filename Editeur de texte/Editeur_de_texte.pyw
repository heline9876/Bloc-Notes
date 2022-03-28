import tkinter as Tk
from tkinter import filedialog
import tkinter.font as tkfont
from tkinter import messagebox

fichiers = [
            ('Fichiers textes', '*.txt'), 
            ('Fichiers Pythons', '*.py *.pyw'),
            ('Tous les fichiers', '*.*')
            ]

class Action():
    def __init__(self, root):
        self.nom_fichier_ouvert, self.root = "*Sans-titre*", root
        self.root.title(f"{self.nom_fichier_ouvert} - Bloc-notes")

    def ouvrir(self, ev=None):
        self.fenetre_avertissement()
        nom_fichier_ouvert = (filedialog.askopenfilename(initialdir = "/", title = "Ouvrir", filetypes = fichiers, defaultextension = fichiers))
        if nom_fichier_ouvert == '':
            return None
        self.nom_fichier_ouvert = nom_fichier_ouvert
        zone_de_texte.delete(0.0, Tk.END)
        with open (self.nom_fichier_ouvert, 'r', encoding="utf-8-sig") as fichier_ouvert:
            texte = (fichier_ouvert.readlines())
            texte = "".join(texte)
            zone_de_texte.insert(0.0, texte)
        self.root.title(str(f"{self.nom_fichier_ouvert} - Bloc-notes"))
    
    def enregistrer_sous(self, ev=None):
        nom = filedialog.asksaveasfilename(title = "Enregistrer sous...", filetypes = fichiers, defaultextension = fichiers)
        if nom == '':
            return None
        with open(nom, "w", encoding="utf-8-sig") as fichier_ouvert:
            fichier_ouvert.write(zone_de_texte.get(0.0, Tk.END))
        self.nom_fichier_ouvert = nom
        self.root.title(str(f"{self.nom_fichier_ouvert} - Bloc-notes"))
        self.check_enregistrement()
    
    def enregistrer(self, ev=None):
        if self.nom_fichier_ouvert == "*Sans-titre*":
            self.enregistrer_sous()
        else:
            with open(self.nom_fichier_ouvert, 'w', encoding="utf-8-sig") as fichier_ouvert:
                fichier_ouvert.write(zone_de_texte.get(0.0, Tk.END))
        self.check_enregistrement()
    
    def nouveau(self, ev=None):
        self.fenetre_avertissement()
        zone_de_texte.delete(0.0, Tk.END)   
        self.nom_fichier_ouvert = "*Sans-titre*"
        self.root.title(str(f"{self.nom_fichier_ouvert} - Bloc-notes"))
        
    def fenetre_avertissement(self):
        self.check_enregistrement()
        if self.enregistré is False:
            rep = messagebox.askquestion("Enregistrement", (f"Voulez-vous sauvegarder les modifications apportés à {self.nom_fichier_ouvert} ?"))
            if rep == "yes":
                self.enregistrer()   
    
    def check_enregistrement(self, ev=None):
        if self.nom_fichier_ouvert == "*Sans-titre*":
            self.enregistré = False
        else:
            with open(self.nom_fichier_ouvert, "r", encoding="utf-8-sig") as fichier:
                texte = fichier.readlines()
                texte = "".join(texte)
                texte = texte.rstrip()
            if texte != zone_de_texte.get(0.0, Tk.END).rstrip():
                self.nom_fichier_affiché = f"*{self.nom_fichier_ouvert}"
                self.enregistré = False
            else:
                self.nom_fichier_affiché = self.nom_fichier_ouvert
                self.enregistré = True
            self.root.title(self.nom_fichier_affiché)
    
    def quitter(self, ev=None):
        self.fenetre_avertissement()
        root.destroy()
    
def raccourcis_claviers():
    fen = Tk.Toplevel()
    fen.resizable(False, False)
    fen.title("Listes des raccourcis claviers")
    fen.configure(bg="light yellow")
    fen.iconphoto(False, Tk.PhotoImage(file='F:\Codes\Python\Projets Autres\Outils\Editeur de texte\icone.gif'))
    label = Tk.Label(fen, text = "Listes des raccourcis claviers\n", bg="light yellow")
    font = tkfont.Font(label, label.cget("font"))
    font.configure(underline = True)
    label.configure(font=font)
    label.pack()
    Tk.Label(fen, text = "Copier : Ctrl + c", bg="light yellow").pack()
    Tk.Label(fen, text = "Coller : Ctrl + v", bg="light yellow").pack()
    Tk.Label(fen, text = "Sélectionner tout : Ctrl + a", bg="light yellow").pack()
    Tk.Label(fen, text = "Supprimer la sélection : Suppr", bg="light yellow").pack()
    Tk.Label(fen, text = "Coller : Ctrl + v", bg="light yellow").pack()
    Tk.Label(fen, text = "Nouveau : Ctrl + n", bg="light yellow").pack()
    Tk.Label(fen, text = "Ouvrir... : Ctrl + p", bg="light yellow").pack()
    Tk.Label(fen, text = "Enregistrer : Ctrl + s", bg="light yellow").pack()
    Tk.Label(fen, text = "Enregistrer sous... : Ctrl + Maj + S", bg="light yellow").pack()
    Tk.Label(fen, text = "Quitter : Alt + F4", bg="light yellow").pack()
    fen.mainloop()
        
def a_propos():
    fen = Tk.Toplevel()
    fen.resizable(False, False)
    fen.title("A propos...")
    fen.configure(bg="light yellow")
    fen.iconphoto(True, Tk.PhotoImage(file='F:\Codes\Python\Projets Autres\Outils\Editeur de texte\icone.gif'))
    label = Tk.Label(fen, text="Bloc-notes\n", bg="light yellow")
    font = tkfont.Font(label, label.cget("font"))
    font.configure(underline = True)
    label.configure(font=font)
    label.pack()
    Tk.Label(fen, text="Logiciel rudimentaire de prise de notes inspiré du notepad Windows.", bg="light yellow").pack()
    Tk.Label(fen, text="Langage : Python 3.10.1", bg="light yellow").pack()
    Tk.Label(fen, text="Auteure : Héline Baumgarten", bg="light yellow").pack()
    Tk.Label(fen, text="Date : 25/02/2022", bg="light yellow").pack()
    fen.mainloop()

root = Tk.Tk()
action = Action(root)
root.geometry("400x500")
root.iconphoto(False, Tk.PhotoImage(file='F:\Codes\Python\Projets Autres\Outils\Editeur de texte\icone.gif'))

root.bind("<Control-n>", action.nouveau)
root.bind("<Control-p>", action.ouvrir)
root.bind("<Control-s>", action.enregistrer)
root.bind("<Control-Shift-S>", action.enregistrer_sous)
root.bind("<Alt-F4>", action.quitter)
root.bind("<Key>", action.check_enregistrement)

scroll_bar_y = Tk.Scrollbar(root)
scroll_bar_y.pack(side=Tk.RIGHT, fill = Tk.Y)

zone_de_texte = Tk.Text(root, yscrollcommand=scroll_bar_y.set, exportselection = 0, width=100000, height=100000, wrap="word")
zone_de_texte.pack(side=Tk.LEFT)

font = tkfont.Font(font=zone_de_texte['font'])
font = tkfont.Font(family="Consolas", size=11)
zone_de_texte.config(font=font)
tab_size = font.measure('    ')
zone_de_texte.config(tabs=tab_size)

scroll_bar_y.config(command=zone_de_texte.yview)

menubar = Tk.Menu(root) 

menu_fichier = Tk.Menu(menubar, tearoff=0)
menu_fichier.add_command(label="Nouveau", command=action.nouveau)
menu_fichier.add_command(label="Ouvrir...", command=action.ouvrir)
menu_fichier.add_separator()
menu_fichier.add_command(label="Enregistrer sous...", command=action.enregistrer_sous)
menu_fichier.add_command(label="Enregistrer", command=action.enregistrer)
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", command=action.quitter)

menu_aide = Tk.Menu(menubar, tearoff=0)
menu_aide.add_command(label="Raccourcis claviers", command=raccourcis_claviers)
menu_aide.add_separator()
menu_aide.add_command(label="A propos...", command=a_propos)

menubar.add_cascade(label="Fichier", menu=menu_fichier)
menubar.add_cascade(label="Aide", menu=menu_aide)

root.config(menu=menubar)

root.mainloop()