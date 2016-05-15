#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from message import Message
from contato import Contato

class Celular(Message,Contato):
    def __init__(self,nome,telefone):
        self.__nome = nome
        self.__telefone = telefone
    @property
    def nome(self):
        return self.__nome
    @property
    def telefone(self):
        return self.__telefone
