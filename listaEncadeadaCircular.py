class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        



class ListaCircular:
    def __init__(self):
        self.primeiro = None
        self.atual = None


    def adicionar(self, valor):
        novo_no = No(valor)

        if self.primeiro is None:
            self.primeiro = novo_no
            novo_no.proximo = self.primeiro
        else:
            atual = self.primeiro
            while atual.proximo != self.primeiro:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.proximo = self.primeiro

    def mostrar(self):
        if self.atual is None:
            self.atual = self.primeiro
            print(self.atual.valor)
        else:
            print(self.atual.valor)

    def proximo(self):
         if not self.atual:
            self.atual = self.primeiro
         else:
             self.atual = self.atual.proximo

    def anterior(self):
        if not self.atual:
            self.atual = self.primeiro
        else:
            atual = self.primeiro
            anterior = None
            while atual.proximo != self.primeiro and atual != self.atual:
                anterior = atual
                atual = atual.proximo

            
            if self.atual == self.primeiro:
                atual = self.primeiro
                while atual.proximo != self.primeiro:
                    atual = atual.proximo

                self.atual = atual

            else:
                self.atual = anterior

    def no_atual(self):
        if not self.atual:
            self.atual = self.primeiro
            print(self.atual.valor)
        else:
            print(self.atual.valor)
                
        



lista = ListaCircular()

lista.adicionar(10)
lista.adicionar(15)
lista.adicionar(54)
lista.adicionar(10)
lista.adicionar(19)
lista.adicionar(90)

lista.no_atual()
lista.proximo()
lista.mostrar()
lista.anterior()
lista.anterior()
lista.mostrar()