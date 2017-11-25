# -*- coding: utf-8 -*-

from django.contrib import admin
from trofeu_avai.models import Jurado, Jogador, Tecnico,\
    Arbitro, Competicao, Adversario, Estadio, Jogo, Gol, Nota, Cartao

admin.site.register(Jurado)
admin.site.register(Jogador)
admin.site.register(Tecnico)
admin.site.register(Arbitro)
admin.site.register(Competicao)
admin.site.register(Adversario)
admin.site.register(Estadio)
admin.site.register(Jogo)
admin.site.register(Gol)
admin.site.register(Nota)
admin.site.register(Cartao)
