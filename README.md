Neste trabalho cada aluno deve implementar um sistema para cadastramento de
artistas, álbuns, músicas e playlists. O diagrama de classes a ser utilizado na sua
implementação encontra-se no final deste documento.
Seu modelo deve levar em conta os seguintes requisitos:
- artistas gravam músicas;
- músicas fazem parte de álbuns;
- cada álbum tem uma ou mais faixas (músicas);
- artistas lançam álbuns;
- álbuns podem ser coletâneas de vários artistas;
- playlists agregam músicas variadas e tem um nome.
Por simplificação deve-se assumir que:
- cada álbum possui um único artista (pode ser uma banda, por exemplo, Skank)
- Num álbum tipo coletânea, o nome do artista será “Vários artistas”.
O seu sistema deve prover um menu com três opções: Artista, Álbum e Playlist.
SubMenu Artista
Deve conter uma opção para Cadastrar artista, apenas informando o nome. Deve
também conter uma opção para Consultar artista por nome. Neste caso, deve-se
mostrar todos os álbuns do artista, com todas as faixas de cada álbum.
SubMenu Álbum
Deve conter uma opção para Cadastrar álbum, informando título, artista, ano e
permitir a inclusão de todas as faixas (músicas) do álbum. Deve também conter uma
opção para Consultar álbuns por título, mostrando todas as faixas do álbum
consultado.
SubMenu Playlist
Deve conter uma opção para Cadastrar playlist, informando nome e permitindo a
inclusão de músicas. O processo de inclusão de músicas na playlist deve ser feito
através de um combo box e um list box. O combo box deve permitir a seleção do
artista. Selecionado o artista, o list box deve exibir todas as músicas do artista
selecionado. Para incluir uma música na playlist, basta clicar no título da música que
está no listbox. Esse procedimento é similar ao que utilizamos na criação de turmas
apresentado na Aula 16. O submenu deve conter também uma opção para Consultar
playlists por nome, mostrando todas as músicas da playlist consultada.
Seu sistema deve ser implementado utilizando o modelo MVC.
