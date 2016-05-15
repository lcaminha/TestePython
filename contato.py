# -*- coding: utf-8 -*-
class Contato(object):
    contatos = []
    def add_contato(self,celular):
        if isinstance(celular,type(self)) == False:
            raise TypeError("o remetente não é um object Celular")
        self.contatos.append(celular)
    def lista_contatos(self):
        for c in self.contatos:
            print "nome: "+c.nome+" - telefone: "+c.telefone
    def get_contato(self,nome):
        for c in self.contatos:
            if(c.nome == nome):
                return c
