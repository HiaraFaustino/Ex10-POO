import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from musica import Musica

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano
        self.__faixas = []
        artista.addAlbum(self)#add o album à lista de álbuns do artista

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def faixas(self):
        return self.__faixas
    
    def addFaixa(self, titulo, artista=None):
        if artista is None:
            artista = self.__artista
        nroFaixa = len(self.__faixas)
        musica = Musica(titulo, artista, nroFaixa)
        self.__faixas.append(musica)
        artista.addMusica(musica)

class LimiteInsereAlbum(tk.Toplevel):
    def __init__(self, controle, listaArtista):
        tk.Toplevel.__init__(self)
        self.geometry('280x120')
        self.title("Álbum")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameAno.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo, text="Título: ")
        self.labelArtista = tk.Label(self.frameArtista, text="Artista: ")
        self.labelAno = tk.Label(self.frameAno, text="Ano: ")
        self.labelTitulo.pack(side="left")
        self.labelArtista.pack(side="left")
        self.labelAno.pack(side="left")

        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width=15, textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaArtista
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")

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

class LimiteInsereFaixa(tk.Toplevel):
    def __init__(self, controle, album):
        tk.Toplevel.__init__(self)
        self.geometry('280x120')
        self.title("Cadastro de Faixas")
        self.controle = controle
        self.album = album
        self.faixas = []

        self.frameFaixas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameFaixas.pack()
        self.frameButton.pack()

        self.labelFaixas = tk.Label(self.frameFaixas, text="Faixas: ")
        self.labelFaixas.pack(side="left")

        self.inputFaixas = tk.Entry(self.frameFaixas, width=20)
        self.inputFaixas.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Adicionar faixa")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", lambda event: controle.enterHandlerFaixa(event, self.album))

        self.buttonClose = tk.Button(self.frameButton, text="Close")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.closeHandler)

class LimiteMostraAlbum():
    def __init__(self, str):
        messagebox.showinfo('Lista de álbum', str)

class CtrlAlbum():
    def __init__(self, ControlePrincipal):
        self.ctrlPrincipal = ControlePrincipal
        self.listaAlbuns = []

    def insereAlbum(self):#inicia a janela de inserção de um novo álbum
        listaArtista = self.ctrlPrincipal.ctrlArtista.getNomeArtista()
        self.limiteIns = LimiteInsereAlbum(self, listaArtista)
        #cria instancia da classe LimiteInsereAlbum e a exibe

    def getAlbum(self, titulo):#receb titulo como parametro
        alb = None
        for album in self.listaAlbuns:#itera sobre a lista de álbuns
            if titulo.lower() == album.titulo.lower():#compara os titulos
                alb = album
        return alb#retona uma instancia de álbum com  base no titulo fornecido

    def consultaAlbum(self):
        msg = 'Álbum consultado:\n'
        answer = simpledialog.askstring("Input", "Título do álbum:")
        album = self.getAlbum(answer)#album chama o método getAlbum e recebe answer
        msg = 'Álbum não encontrado!'
        if album != None:
            msg = 'Faixas:\n'
            for faixa in album.faixas:
                msg += str(faixa.nroFaixa) + '-' + faixa.titulo + '\n'
            self.limiteIns.mostraJanela('Álbum consultado', msg)

    def enterHandler(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        artistaNome = self.limiteIns.combobox.get()
        ano = self.limiteIns.inputAno.get()
        artista = self.ctrlPrincipal.ctrlArtista.getArtista(artistaNome)
        #obtém a instancia do artista com base no nome fornecido
        album = Album(titulo, artista, ano)#cria nova instancia de album
        self.listaAlbuns.append(album)#add album na lista
        self.limiteInsereFaixas = LimiteInsereFaixa(self, album)
        #inicializa uma janela p/ inserir faixas nesse album
        self.limiteIns.mostraJanela('Sucesso', 'Álbum cadastrado com sucesso')
        self.clearHandler(event)

    def enterHandlerFaixa(self, event, album):
        faixa = self.limiteInsereFaixas.inputFaixas.get()
        if faixa:
            album.addFaixa(faixa)#add a faixa no album
            self.limiteInsereFaixas.inputFaixas.delete(0, tk.END)
            messagebox.showinfo('Sucesso', 'Faixa cadastrada com sucesso!')

    def clearHandler(self, event):
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.combobox.set("")
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))

    def closeHandler(self, event):
        self.limiteIns.destroy()
        if self.limiteInsereFaixas:
            self.limiteInsereFaixas.destroy()


