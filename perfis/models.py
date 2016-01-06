from __future__ import unicode_literals

from django.db import models

class Perfil(models.Model):
#troca do object pelo model

#    def __init__(self, nome='', email='', telefone='', nome_empresa=''):
#        self.nome = nome
#        self.email = email
#        self.telefone = telefone
#        self.nome_empresa = nome_empresa

    nome =  models.CharField(max_length=255, null=False) 
    email = models.CharField(max_length=255, null=False) 
    telefone = models.CharField(max_length =15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('self')

    def convidar(self, perfil_convidado):    
        Convite(solicitante = self, convidado = perfil_convidado).save()
         #convite = Convite(solicitante = self, convidado = perfil_convidado)
         #convite.save() 

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name = 'convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name = 'convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()