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

    def adicionar_fim(self, valor):
        novo_no = No(valor)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
    
    def remover_inicio(self):
        atual = self.primeiro
        if atual is None:
            return print('Lista vazia')
        else:
            self.primeiro = self.primeiro.proximo
            atual = None

    def remover_fim(self):
        atual = self.primeiro
        if atual is None:
            return print('Lista vazia')
        else:
            anterior = None
            while atual.proximo is not None:
                anterior = atual
                atual = atual.proximo
            anterior.proximo = None
    
    def remover(self, valor):
        atual = self.primeiro
        anterior = None
        if atual.valor is None:
            return print('Lista vazia')
        elif atual.valor == valor:
            self.primeiro = atual.proximo
            return print('Valor removido')
        else:
            while atual.proximo is not None and atual.valor != valor:
                anterior = atual
                atual = atual.proximo
            if atual.valor == valor:
                    anterior.proximo = atual.proximo
                    return print('Valor removido')
            else:
                return print('Valor não encontrado')
            
    def adicionar_apos(self, apos, novo):
        atual = self.primeiro
        novo_no = No(novo)
        proximo = None
        if atual.valor is None:
            return print('Lista vazia')
        elif atual.valor == apos:
            novo_no.proximo = atual.proximo
            self.primeiro.proximo = novo_no
        else:
            while atual.proximo is not None and atual.valor != apos:
                    atual = atual.proximo
                    proximo = atual.proximo
            if atual.valor == apos:
                atual.proximo = novo_no
                novo_no.proximo = proximo

                

listaEncadeada = ListaEncadeada()

listaEncadeada.adicionar(10)
listaEncadeada.adicionar(20)
listaEncadeada.adicionar(30)
listaEncadeada.adicionar(35)
listaEncadeada.adicionar(40)
listaEncadeada.adicionar(50)
listaEncadeada.imprimir()
print('Adicionados os valores')

retorno = listaEncadeada.buscar(10)
print(retorno)
print('Valor buscado')

listaEncadeada.adicionar_inicio(5)
listaEncadeada.adicionar_fim(55)
listaEncadeada.imprimir()
print('Valores adicionados no início e fim da lista')

listaEncadeada.remover_inicio()
listaEncadeada.remover_fim()
listaEncadeada.imprimir()
print('Valores removidos do início e fim da lista')

listaEncadeada.remover(35)
listaEncadeada.imprimir()

print("Adicionar após")
listaEncadeada.adicionar_apos(50, 15)
listaEncadeada.imprimir()