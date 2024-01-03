class Musica:
    def __init__(self, titulo, artista, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__nroFaixa = nroFaixa
        artista.addMusica(self)

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def nroFaixa(self):
        return self.__nroFaixa
    
