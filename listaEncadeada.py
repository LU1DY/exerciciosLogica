class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def adicionar(self, valor):
        novo_no = No(valor)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

    def imprimir(self):
        atual = self.primeiro
        while atual is not None:
            print(atual.valor)
            atual = atual.proximo


    def buscar(self, valor):
        atual = self.primeiro
        if atual is None:
            return 'Lista vazia'
        while atual.proximo is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        
        return False
    
    def adicionar_inicio(self, valor):
        novo_no = No(valor)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no
    
    def remover_inicio(self):
        atual = self.primeiro
        if atual is None:
            return print('Lista vazia')
        else:
            self.primeiro = self.primeiro.proximo
            atual = None






listaEncadeada = ListaEncadeada()

listaEncadeada.adicionar(10)
listaEncadeada.adicionar(30)
listaEncadeada.adicionar(20)
listaEncadeada.adicionar_inicio(1)
print(listaEncadeada.buscar(1))
print('-------------')
listaEncadeada.imprimir()
print('-------------')
listaEncadeada.remover_inicio()
print(listaEncadeada.buscar(1))
listaEncadeada.imprimir()
