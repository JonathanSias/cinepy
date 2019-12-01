# -*- coding: utf-8 -*-
# ##################################################
### KEY WORDS
# list
# sections
# confirm
# pay
 
### PARAMETERS
# typelist
# moviename
# choice
# myname mycard mycpf
# ##################################################
import socket

# classe movie
class Movie:
    def __init__(self, name, tickets, price, section, genre):
        self.name = name
        self.tickets = tickets
        self.price = price
        self.section = section
        self.genre = genre
# ##################################################
# filme, lugares, preço, horario, genero
movie0 = Movie("Watchmen", 40, 20.0, 9, "comics")
movie1 = Movie("John Wick", 25, 10.5, 10, "action")
movie2 = Movie("The Mandalorian", 15, 10.0, 10, "sfiction")
movie3 = Movie("Eurotrip", 15, 10.0, 12, "comedia")
movie4 = Movie("Superbad", 15, 10.0, 14, "comedia")
movie5 = Movie("Projeto X", 40, 15.5, 12, "comedia")
movie6 = Movie("From Dusk Till Dawn", 15, 10.0, 16, "terror")
movie7 = Movie("As Branquelas", 25, 10.5, 13, "comedia")
movie8 = Movie("Os Incríveis", 40, 20.0, 14, "animation")
movie9 = Movie("The Avengers - Ifinite War", 40, 20.0, 17, "comics")
movie10 = Movie("The Avengers - Endgame", 40, 20.0, 20, "comics")
movie11 = Movie("Joker", 40, 20.0, 23, "comics")
movie12 = Movie("Indiana Jones", 25, 10.5, 15, "aventura")
movie13 = Movie("SpiderMan into The Spider Verse", 30, 20.0, 10, "animation")
movie14 = Movie("Baby Driver", 30, 20.0, 12, "drama")
movie15 = Movie("Titanic", 30, 20.0, 15, "romance")
movie16 = Movie("O Pistoleiro Solitário", 30, 20.0, 17, "western")
movie17 = Movie("Por Um Punhado de Dólares", 30, 20.0, 19, "western")
movie18 = Movie("Era Uma Vez No México", 30, 20.0, 21, "western")
movie19 = Movie("O Senhor dos Anéis: O Retorno do Rei", 60, 25.5, 19, "fantasy")
movie20 = Movie("Chernobyl", 60, 25.5, 16, "documentario")
movie21 = Movie("Click", 20, 5.50, 14, "drama")
movie22 = Movie("O Resgate do Soldade Ryan", 20, 5.50, 16, "guerra")
movie23 = Movie("Bird Box", 20, 5.50, 19, "suspense")
movie24 = Movie("2Fast 2Furious", 10, 5, 19, "action")
movie25 = Movie("Resident Evil", 10, 5, 20, "terror")
movie26 = Movie("Star Trek", 60, 25.5, 13, "sfiction")
movie27 = Movie("O Senhor dos Anéis: As Duas Torres", 60, 25.5, 10, "fantasy")
movie28 = Movie("Deadpool", 65, 27.5, 10, "comics")
movie29 = Movie("El Camino", 65, 30, 13, "drama")
movie30 = Movie("Pelas Garotas e Pela Glória", 10, 5, 10, "comedia")
# ##################################################
# Separados por gênero
action = [movie1, movie24]
aventura = [movie12]
terror = [movie6, movie25]
sfiction = [movie2, movie26]
romance = [movie15]
comedia = [movie3, movie4, movie5, movie7, movie30]
documentario = [movie20]
fantasy = [movie19, movie27]
drama = [movie14, movie21, movie29]
western = [movie16, movie17, movie18]
guerra = [movie22]
animation = [movie8, movie13]
suspense = [movie23]
comics = [movie0, movie9, movie10, movie28]
allmovies = [movie0, movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, movie11, movie12, movie13, movie14, movie15, movie16, movie17, movie18, movie19, movie20, movie21, movie22, movie23, movie24, movie25, movie26, movie27, movie28, movie29, movie30]
# ##################################################
# função que lista os filmes disponiveis
def lista_filmes(typelist):
    if(typelist == "action"):
        for i in range(len(action)):
            # print(action[i].name)
    elif(typelist == "aventura"):
        for i in range(len(aventura)):
            # print(aventura[i].name)
    elif(typelist == "terror"):
        for i in range(len(terror)):
            # print(terror[i].name)
    elif(typelist == "sfiction"):
        for i in range(len(sfiction)):
            # print(sfiction[i].name)
    elif(typelist == "romance"):
        for i in range(len(romance)):
            # print(romance[i].name)
    elif(typelist == "comedia"):
        glist = ""
        for i in range(len(comedia)):
            glist += ((comedia[i].name)+"\n")
        con.send(glist)
            # print(comedia[i].name)
    elif(typelist == "documentario"):
        for i in range(len(documentario)):
            # print(documentario[i].name)
    elif(typelist == "fantasy"):
        for i in range(len(fantasy)):
            # print(fantasy[i].name)
    elif(typelist == "drama"):
        for i in range(len(drama)):
            # print(drama[i].name)
    elif(typelist == "western"):
        for i in range(len(western)):
            # print(western[i].name)
    elif(typelist == "guerra"):
        for i in range(len(guerra)):
            # print(guerra[i].name)
    elif(typelist == "animation"):
        for i in range(len(animation)):
            # print(animation[i].name)
    elif(typelist == "suspense"):
        for i in range(len(suspense)):
            # print(suspense[i].name)
    elif(typelist == "comics"):
        for i in range(len(comics)):
            # print(comics[i].name)
    elif(typelist == "tudo"):
        for i in range(len(allmovies)):
            # print(allmovies[i].name)
    else:
        # print("ERRO 404 NOT FOUND")
        break
# ##################################################
# funçao lista os horarios

# ##################################################
HOST = ''                   # Endereco IP do Servidor
PORT = 5000                 # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    con.send("Bem Vindo ao CINEPY")
    print('Concetado por', cliente)
    while True:
        msg = con.recv(1024)
        # trata a requisição do cliente
        if (msg == "lista tudo"):
            typelist = "tudo"
            lista_filmes(typelist)
        if (msg == "lista action"):
            typelist = "action"
            lista_filmes(typelist)
        if (msg == "lista aventura"):
            typelist = "aventura"
            lista_filmes(typelist)
        if (msg == "lista terror"):
            typelist = "terror"
            lista_filmes(typelist)
        if (msg == "lista sfiction"):
            typelist = "sfiction"
            lista_filmes(typelist)
        if (msg == "lista romance"):
            typelist = "romance"
            lista_filmes(typelist)
        if (msg == "lista comedia"):
            typelist = "comedia"
            lista_filmes(typelist)
        if (msg == "lista documentario"):
            typelist = "documentario"
            lista_filmes(typelist)
        if (msg == "lista fantasy"):
            typelist = "fantasy"
            lista_filmes(typelist)
        if (msg == "lista drama"):
            typelist = "drama"
            lista_filmes(typelist)
        if (msg == "lista western"):
            typelist = "western"
            lista_filmes(typelist)
        if (msg == "lista guerra"):
            typelist = "guerra"
            lista_filmes(typelist)
        if (msg == "lista animation"):
            typelist = "animation"
            lista_filmes(typelist)
        if (msg == "lista suspense"):
            typelist = "suspense"
            lista_filmes(typelist)
        if (msg == "lista comics"):
            typelist = "comics"
            lista_filmes(typelist)
        if not msg: break
        print(cliente, msg)
        # con.send("bla bla bla")
    print('Finalizando conexao do cliente', cliente)
    con.close()