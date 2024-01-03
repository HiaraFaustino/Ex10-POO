import tkinter as tk
from tkinter import messagebox
import artista as art
import album as alb
import playlist as play

class LimitePrincipal():
    def __init__(self,root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)

        self.artistaMenu.add_command(label="Cadastrar", \
                    command=self.controle.insereArtista)
        self.artistaMenu.add_command(label="Consultar", \
                    command=self.controle.consultaArtista)
        self.menubar.add_cascade(label="Artista", \
                    menu=self.artistaMenu)
        
        self.albumMenu.add_command(label="Cadastrar", \
                    command=self.controle.insereAlbum)
        self.albumMenu.add_command(label="Consultar", \
                    command=self.controle.consultaAlbum)
        self.menubar.add_cascade(label="Álbum", \
                    menu=self.albumMenu)
        
        self.playlistMenu.add_command(label="Cadastrar", \
                    command=self.controle.inserePlaylist)
        self.playlistMenu.add_command(label="Consultar", \
                    command=self.controle.consultaPlaylist)
        self.menubar.add_cascade(label="Playlist", \
                    menu=self.playlistMenu)
    
        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlArtista = art.CtrlArtista()
        self.ctrlAlbum = alb.CtrlAlbum(self)
        self.ctrlPlaylist = play.CtrlPlaylist(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Exemplo MVC")
        self.root.mainloop()

    def insereArtista(self):
        self.ctrlArtista.insereArtista()

    def consultaArtista(self):
        self.ctrlArtista.consultaArtista()

    def insereAlbum(self):
        self.ctrlAlbum.insereAlbum()

    def consultaAlbum(self):
        self.ctrlAlbum.consultaAlbum()

    def inserePlaylist(self):
        self.ctrlPlaylist.inserePlaylist()

    def consultaPlaylist(self):
        self.ctrlPlaylist.consultaPlaylist()

if __name__ == '__main__':
    c = ControlePrincipal()
