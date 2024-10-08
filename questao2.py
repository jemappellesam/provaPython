dadosCidades = [("a",[10,25,30,25,20,21,24]), ("b", [5,5,21,12,36,25,5]),("c", [12,25,40,23,25,22,21])]


def calculaTempMedia(dadosCidades):
    ResultadotempMedia = list()
    for i in dadosCidades:
        nomeCidade = i[0]
        temperaturas = i[1]
        calculo = 0
        for t in temperaturas:
            calculo = calculo + int(t)
        TempMedia = calculo/7
        tuplaResultado = (nomeCidade, TempMedia)
        ResultadotempMedia.append(tuplaResultado)
    return ResultadotempMedia   



print(calculaTempMedia(dadosCidades))
