class Message(object):
    messagens_recebidas = [];
    messagens_enviadas  = [];

    def compoe_messagem(self,remetente,messagem):
        remetente.add_caixa_de_entrada({self:messagem})
        self.add_caixa_de_saida({remetente:messagem})

    def add_caixa_de_entrada(self,messagem):
        self.messagens_recebidas.append(messagem)

    def add_caixa_de_saida(self,messagem):
        self.messagens_enviadas.append(messagem)

    def ler_caixa_de_entrada(self):
        for m in self.messagens_enviadas:
            print m

    def ler_caixa_de_saida(self):
        for m in self.messagens_enviadas:
            print m
