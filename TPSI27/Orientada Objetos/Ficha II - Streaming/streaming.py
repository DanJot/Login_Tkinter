from Video import Video

clubeVideo = []

def InserirVideo():

    titulo = input("Indique o titulo do video: ")
    duracao = int(input("Indique a duração do video: "))
    ano = int(input("Indique o ano do video: "))
    classificacao = int(input("Indique a classificação do video: "))

    novoVideo = Video(titulo, duracao, ano, classificacao)
    clubeVideo.append(novoVideo) #criação de lista  composta por objetos da classe video

    print("\n Infomação guardada com sucesso !")

def ListarVideos():

    if not clubeVideo: # Se não existir video na listagem...
        print("\n Não existem videos registados!")
    else:
        print(f"{"Titulo":15} {"Duração":15} {"Ano":15} {"Classificação":15}")
        for videos in clubeVideo:
            videos.mostrarDados()


def ListarVideos5():
    if not clubeVideo:
        print("\n Não existem videos registados!")
    else:
        mostrar = False
        for videos in clubeVideo:

            if videos.classificacao == 5:
                videos.mostrarDados()
                mostrar = True

        if not mostrar:
            print("Não existem videos com claissificação 5 para apresentar")

def RemoverVideos():
    if not clubeVideo:
        print("\n Não existem videos registados!")

    else:
        encontrado = False
        tituloRemover = input("Indique o titulo do Vídeo a remover: ")
        for posicao, videos in enumerate(clubeVideo):

            if videos.titulo == tituloRemover:
                encontrado = True
                clubeVideo.pop(posicao)
                print("Video removido com sucesso!")

        if not encontrado:
            print("O titulo procurado não existe")
