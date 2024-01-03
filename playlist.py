import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class Playlist:
    def __init__(self, nome, listaMusicasPlaylist):
        self.__nome = nome
        self.__musicas = listaMusicasPlaylist

    @property
    def nome(self):
        return self.__nome
    
    @property
    def musicas(self):
        return self.__musicas
    
    def addMusica(self, musica):
        self.__musicas.append(musica)

class LimiteInserePlaylist(tk.Toplevel):
    def __init__(self, controle, listaArtista):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameNomeArtista = tk.Frame(self)
        self.frameMusicas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameNomeArtista.pack()
        self.frameMusicas.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome da Playlist: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.labelNomeArtista = tk.Label(self.frameNomeArtista, text="Escolha o artista: ")
        self.labelNomeArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameNomeArtista, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaArtista
        self.combobox.bind("<<ComboboxSelected>>", controle.insereLista)

        self.labelMusicas = tk.Label(self.frameMusicas, text="Escolha as músicas: ")
        self.labelMusicas.pack(side="left")
        self.listbox = tk.Listbox(self.frameMusicas)
        self.listbox.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton, text="Insere música")
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereMusica)

        self.buttonCria = tk.Button(self.frameButton, text="Cria Playlist")
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraPlaylist():
    def __init__(self, str):
        messagebox.showinfo('Lista de playlist', str)

class CtrlPlaylist():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPlaylists = []

    def getPlaylist(self, nome):#recebe nome como parametro
        play = None
        for playlist in self.listaPlaylists:#itera sobre a lista de playlists
            if nome.lower() == playlist.nome.lower():#compara os nomes
                play = playlist
        return play

    def inserePlaylist(self):
        self.listaMusicasPlaylist = []#inicializa lista vazia para armazenar as musicas da playlist
        listaArtistas = self.ctrlPrincipal.ctrlArtista.getNomeArtista()
        #obtém a lista de artistas do controle de artistas
        self.limiteIns = LimiteInserePlaylist(self, listaArtistas)
        #insere a playlist

    def criaPlaylist(self, event):
        nome = self.limiteIns.inputNome.get()#obtém o nome da playlist
        playlist = Playlist(nome, self.listaMusicasPlaylist)#cria nova instancia playlist
        self.listaPlaylists.append(playlist)#add playlist a lista
        self.limiteIns.mostraJanela('Sucesso', 'Playlist criada com sucesso!')
        self.limiteIns.destroy()

    def insereMusica(self, event):
        musicaSel = self.limiteIns.listbox.get(tk.ACTIVE)#obtém a musica selecionada
        artSel = self.ctrlPrincipal.ctrlArtista.getArtista(self.limiteIns.escolhaCombo.get())
        #obtém artista selecionado no combobox
        musica = self.ctrlPrincipal.ctrlArtista.getMusica(artSel, musicaSel)
        self.listaMusicasPlaylist.append(musica)#add a musica a lista
        self.limiteIns.mostraJanela('Sucesso', 'Música adicionada com sucesso!')
    
    def insereLista(self, event):#quando o usuario seleciona um artista
        self.limiteIns.listbox.delete(0, tk.END)#limpa a lista de musica
        artista = self.limiteIns.escolhaCombo.get()#obtém artista do combobox
        artista = self.ctrlPrincipal.ctrlArtista.getArtista(artista)
        #obtém a instancia do artista do controle de artistas
        if artista:
            listaMusica = self.ctrlPrincipal.ctrlArtista.getListaMusica(artista)
            listaMusica = list(set(listaMusica))# Remova duplicatas antes de inserir na listbox
        for musica in listaMusica:
            self.limiteIns.listbox.insert(tk.END, musica)

    def consultaPlaylist(self):
        msg = 'Playlist consultada:\n'
        answer = simpledialog.askstring("Input", "Nome da playlist: ")
        playlist = self.getPlaylist(answer)#playlist chama o método getPlaylist e recebe answer
        msg = 'Playlist não encontrada!'
        if playlist != None: 
            msg = 'Playlist: ' + playlist.nome + '\n'
            for musica in playlist.musicas:
                msg += musica.titulo + '\n'
            self.limiteIns.mostraJanela('Playlist consultada', msg)

    


 