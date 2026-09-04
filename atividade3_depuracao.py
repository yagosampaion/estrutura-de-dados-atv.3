class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.proximo = n2
n2.proximo = n3

atual = n1

while atual is not None:
    print(atual.valor)
    atual = atual.proximo