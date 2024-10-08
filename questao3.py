numeros = [11, 22, 45, 50, 25, 26, 27, 28, 30, 41]

def isPrimo(numeros):
    def unidade_primo(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primos = [num for num in numeros if unidade_primo(num)]
    return primos

primos_encontrados = isPrimo(numeros)
print(primos_encontrados)

 