import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from musica import Musica

class Artista:
    def __init__(self, nome):
        self.__nome = nome
        self.__albuns = []
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def albuns(self):
        return self.__albuns
    
    @property
    def musicas(self):
        return self.__musicas
    
    def addAlbum(self, album):
        self.__albuns.append(album)

    def addMusica(self, musica):
        self.__musicas.append(musica)
    
class LimiteInsereArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
         
        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonClose = tk.Button(self.frameButton, text="Close")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraArtista():
    def __init__(self, str):
        messagebox.showinfo('Lista de artistas', str)

class CtrlArtista():
    def __init__(self):
        self.listaArtistas = []

    def getNomeArtista(self):
        listaart = []
        for artista in self.listaArtistas: #itera sobre a lista de artista e add os nomes
            listaart.append(artista.nome) # e add os nomes dos artistas a uma lista
        return listaart
    
    def getListaMusica(self, artista):#recebe um objeto artista como parametro
        listaMusica = [] 
        for mus in artista.musicas: #itera sobre as musicaas desse artista
            listaMusica.append(mus.titulo)#add os titulos a uma lista
        return listaMusica
    
    def getMusica(self, artista, titulo):#recebe um obj artista e titulo como parametro
        mus = None
        for musica in artista.musicas:#itera sobre as musicas do artista
            if musica.titulo == titulo:#compara os titulos
                mus = musica
        return mus #retorna a instancia da musica correspondente
    
    def getArtista(self, nome):#recebe um nome como parametro
        art = None
        for artista in self.listaArtistas:#itera sobre a lista de artistas
            if nome.lower() == artista.nome.lower():#compara os nomes 
                art = artista
        return art
        
    def insereArtista(self):#inicia a janela de inserção de um novo artista
        self.limiteIns = LimiteInsereArtista(self)

    def consultaArtista(self):
        msg = 'Artista consultado:\n'
        answer = simpledialog.askstring("Input", "Nome:")
        artista = self.getArtista(answer)#artista chama o método getArtista e recebe answer
        msg = 'Artista não encontrado!'
        if artista != None:
            msg = 'Álbum:\n'
            for album in artista.albuns:
                msg += album.titulo + '\n'
                msg += 'Faixas:\n'
                for faixa in album.faixas:
                    msg += str(faixa.nroFaixa) + '-' + faixa.titulo + '\n'
                msg += '---------------\n'
            self.limiteIns.mostraJanela('Artista consultado', msg)

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()#obtem nome do artista da entrada da janela
        artista = Artista(nome)#cria instancia de Artista com esse nome
        self.listaArtistas.append(artista)#add artista a lista 
        self.limiteIns.mostraJanela('Sucesso', 'Artista cadastrado com sucucesso!')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        #obtem a entrada da janela e exclui seu conteúdo

    def closeHandler(self, event):
        self.limiteIns.destroy()
        #detruir a instancia da janela inserção



