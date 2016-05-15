from celular import Celular

#celular
telefone_do_ramon = Celular("Ramon","981388010")
telefone_do_adriano = Celular("Adriano","999199911")
telefone_do_davi = Celular("Davi","1234567")

#contato
telefone_do_ramon.add_contato(telefone_do_adriano)
telefone_do_ramon.add_contato(telefone_do_davi)
telefone_do_ramon.lista_contatos()

contato = telefone_do_ramon.get_contato("Adriano")
print "deve trazer o telefone de adriano"
print contato.telefone

print "-------------------------------------"
# messagem
telefone_do_ramon.compoe_messagem(telefone_do_adriano,"e ai cara")
print "Testa caixa de entrada de adriano..."
telefone_do_adriano.ler_caixa_de_entrada()
print "-------------------------------------"
print "Testa caixa de saide de ramon..."
telefone_do_ramon.ler_caixa_de_saida()
