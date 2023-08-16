from random import randint
import random


def draw(opc, team):
    teams = open("Teams.txt", "r")

    times = []
    paises = []
    timespaises = {}
    timeschaves = {}
    cabecas = []
    naocabecas = []
    grupo1 = []
    grupo2 = []
    grupo3 = []
    grupo4 = []
    grupo5 = []
    grupo6 = []
    grupo7 = []
    grupo8 = []
    grupos = [grupo1, grupo2, grupo3, grupo4, grupo5, grupo6, grupo7, grupo8]

    for l in teams.readlines():
        timespaises[l.split(' ', 1)[1].rstrip()] = l.split(' ', 1)[0].rstrip()
        times.append(l.split(' ', 1)[1].rstrip())
        for t in times:
            timeschaves[t] = str(t).isupper()
        paises.append(l.split(' ', 1)[0].rstrip())
    for t in times:
        if timeschaves[t]:
            cabecas.append(t)
        else:
            naocabecas.append(t)
        random.shuffle(cabecas)

    def tryy(time):
        i = randint(0, (grupos.__len__() - 1))
        if grupos[i].__len__() != 0:
            if grupos[i].__len__() < 4:
                a = 0
                for c in grupos[i]:
                    if c != time:
                        if timespaises[time] != timespaises[c]:
                            a += 1
                            if a == grupos[i].__len__():
                                grupos[i].append(time)
                        else:
                            tryy(time)
            elif grupos[i].__len__() == 4:
                try:
                    tryy(time)
                except:
                    if opc == "yes":
                        print("loading...")
                    else: print("ERROR")
        elif grupos[i].__len__() == 0:
            grupos[i].append(time)

    for c in cabecas:
        grupos[cabecas.index(c)].append(c)
    for c in naocabecas:
        tryy(c),

    if opc != "yes":
        for g in grupos:
            for h in g:
                if str(h).isupper():
                    g.insert(0, g.pop(g.index(h)))
            print("GRUPO " + str(grupos.index(g) + 1) + "! " + str(g.__len__()) + " TIMES DENTRO")
            print(g)
            print("----------------------------------------------------------------")

    if opc == "yes":
        for g in grupos:
            for h in g:
                if team == h:
                    TT = [x for i, x in enumerate(g) if i != team]
                    return TT

def normal():
    draw("no", "")
    if input("Denovo? Y/N") != "n":
        normal()
def calcular(x, y):
    time = x
    quantidade = y
    times = []
    w = int(quantidade+1)
    x = 0
    while x < (w-1):
        try:
            times.append(draw("yes", time)[0])
            times.append(draw("yes", time)[1])
            times.append(draw("yes", time)[2])
            times.append(draw("yes", time)[3])
            x += 1
            if x%5 == 0:
                print(str(x) + "\t|\t" + str(int(x/w*100)) + "%\n\n\n---------------------------------------------\n\n")
        except:
            print("trying...")

    freq = {}
    total = 0
    for t in times:
        if t != time:
            freq[t] = times.count(t)
            total += 1
    cem = 0
    for f in freq:
        print(str((freq[f]/total*100)) + "%" + " | " + str(freq[f]) + " | " + str(f))
        cem += (freq[f]/total*100)
    print("\n"+str(cem) + "%")

def go():
    if input("Normal ou calcular? 1/2?") == "1":
        normal()
    else:
        calcular(input("Digite o time a simular: "), int(input("Digite o número de simulações: ")))
go()