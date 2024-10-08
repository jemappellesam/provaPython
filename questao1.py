palavra = input("Digite uma palavra: ")


def isPalindromo(palavra):
    palindromo = False
    controle = True
    indice = len(palavra)-1
    novaPalavra = ""
    while controle:
        novaPalavra = novaPalavra + palavra[indice]
        indice = indice - 1
        if(indice == -1):
         controle = False
    if(novaPalavra== palavra):
        palindromo = True
    return palindromo
     
    

if(palavra != ""):
    print("Resultado do palindromo: " + str(isPalindromo(palavra)))
else:
    print("Entrada invalida")