def criar_produto(nome, codigo, preco, estoque):
    tupla = (nome, codigo, preco, estoque)
    return tupla

def atualizar_estoque(produto, quantidade):
    estoque = produto[3] + quantidade
    novatupla=(produto[0], produto[1], produto[2], estoque)
    return novatupla


def listar_produtos(produtos):
    for i in produtos:
        print(i)

produtos = list()

produtos.append(criar_produto("feijao",25,5,100))
produtos.append(criar_produto ("Arroz", 26,8,200))
produtos.append(criar_produto("Macarrao", 27,6,500))

listar_produtos(produtos)

print("-------------------------------------------")
produtos[1]= atualizar_estoque(produtos[1], 52)

listar_produtos(produtos)