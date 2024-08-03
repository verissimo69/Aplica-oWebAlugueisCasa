
# Definição da Função:
# A função lista_locacao é definida com um parâmetro request. Este parâmetro representa a solicitação HTTP recebida pelo servidor.
# Consulta ao Banco de Dados:
# imobiles = Immobile.objects(is_locate=False):
# Aqui, estamos utilizando o ORM (Object-Relational Mapping) do Django para consultar a tabela Immobile no banco de dados.
# Immobile.objects é uma interface para realizar consultas na tabela Immobile.
# is_locate=False é um filtro aplicado à consulta, retornando apenas os imóveis que não estão locados (ou seja, is_locate é False).
# Criação do Contexto:
# context = {'immobiles': imobiles}:
# Um dicionário chamado context é criado. Este dicionário contém uma chave immobiles que armazena o resultado da consulta ao banco de dados.
# Este contexto será passado para o template, permitindo que os dados sejam acessados e exibidos na página HTML.
# Renderização do Template:
# return render(request, 'list-location', context):
# A função render do Django é utilizada para renderizar um template HTML.
# request é o objeto de solicitação HTTP.
# 'list-location' é o nome do template HTML que será renderizado.
# context é o dicionário de contexto que contém os dados a serem exibidos no template.
# Resumo
# A função lista_locacao consulta todos os imóveis que não estão locados no banco de dados, cria um contexto com esses imóveis e renderiza um template HTML chamado list-location, passando o contexto para que os dados possam ser exibidos na página.
# Se precisar de mais alguma coisa ou tiver dúvidas, estou aqui para ajudar!

from django.views import View
from django.shortcuts import render
from .models import Immobile


class list_location(View):
    def lista_locacao(request):
        immobiles = Immobile.objects.filter(is_locate = False)
        context = {
            'immobiles': immobiles
        }
        return render(request, 'todos/list-location.html',context)
