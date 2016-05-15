class Contato(object):
    contatos = []
    def add_contato(self,celular):
        self.contatos.append(celular)
    def lista_contatos(self):
        for c in self.contatos:
            print "nome: "+c.nome+" - telefone: "+c.telefone
    def get_contato(self,nome):
        for c in self.contatos:
            if(c.nome == nome):
                return c
