#! -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from qgis.core import QgsConditionalStyle, QgsMapLayerRegistry, QgsVectorLayer, QgsDataSourceURI, QgsPoint, QGis, QgsGeometry, QgsProject, QgsField

class GeradorDeRegras:
    def __init__(self, iface, bancoDeDados):
        'Construtor'
        self.inicializarVariaveis()
        self.definirBancoDeDados(bancoDeDados)
        self.definirIface(iface)

    def inicializarVariaveis(self):
        'Metodo para inicializar variaveis'
        self.iface = None
        self.bancoDeDados = None
        self.valoresDeRegra = None

    def definirBancoDeDados(self, b):
        'Metodo para registrar banco de dados'
        self.bancoDeDados = b

    def obterBancoDeDados(self):
        'Metodo para obter banco de dados'
        return self.bancoDeDados

    def definirIface(self, i):
        'Metodo para registrar o objeto iface do qgis'
        self.iface = i

    def obterIface(self):
        'Metodo para obter o objeto iface do qgis'
        return self.iface

    def gerarRegras(self, tipo):
        'Metodo que pega os dados da tabela layer_rules do banco de dados e cria uma estrutura de  dicionario de todas as regras'
        tabela = self.obterBancoDeDados().obterTabelaDeRegras(tipo)
        regras = { 'atributo' : {}, 'linha' : {}}
        for linha in tabela:
            valoresDeRegra = self.organizarValoresDeRegra(linha)
            regra = self.criarEstiloDeRegra(valoresDeRegra)
            if(not valoresDeRegra['atributo']) and (not valoresDeRegra['camada'] in regras['linha'].keys()):
                regras['linha'][valoresDeRegra['camada']] = [regra]
            elif(not valoresDeRegra['atributo']) and (valoresDeRegra['camada'] in regras['linha'].keys()):
                regras['linha'][valoresDeRegra['camada']].append(regra)
            elif(valoresDeRegra['atributo']) and (not valoresDeRegra['camada'] in regras['atributo'].keys()):
                regras['atributo'][valoresDeRegra['camada']] = {valoresDeRegra['atributo'] : [regra]}
            elif(valoresDeRegra['camada'] in regras['atributo'].keys()) and (valoresDeRegra['atributo'] in regras['atributo'][valoresDeRegra['camada']].keys()):
                regras['atributo'][valoresDeRegra['camada']][valoresDeRegra['atributo']].append(regra)
            elif(valoresDeRegra['camada'] in regras['atributo'].keys()) and (not valoresDeRegra['atributo'] in regras['atributo'][valoresDeRegra['camada']].keys()):
                regras['atributo'][valoresDeRegra['camada']] = {valoresDeRegra['atributo'] : [regra]}
        self.configurarRegrasEmCamadas(regras)

    def organizarValoresDeRegra(self, linha):
        'Metodo que pega o linha da tabela layer_rules e a organiza em uma estrutura de dicionario'
        valoresDeRegra = {
                                'camada' : linha[0],
                                'tipo_regra' : linha[1],
                                'descricao' : linha[2],
                                'corRgb' : [ int(linha[3].split(',')[0]), int(linha[3].split(',')[1]), int(linha[3].split(',')[2])],
                                'regra' : linha[4],
                                'atributo' : linha[6]
                             }
        return valoresDeRegra

    def criarEstiloDeRegra(self, valoresDeRegra):
        'Metodo para criar regra'
        estilo = QgsConditionalStyle()
        estilo.setName( valoresDeRegra['descricao'] )
        estilo.setRule( valoresDeRegra['regra'] )
        estilo.setBackgroundColor(
                                    QtGui.QColor(
                                           valoresDeRegra['corRgb'][0],
                                           valoresDeRegra['corRgb'][1],
                                           valoresDeRegra['corRgb'][2]
                                          )
                                 )
        return estilo

    def configurarRegrasEmCamadas(self, regras):
        'Metodo para configurar todas as regras montadas nas camadas'
        for tipo in regras:
            for camadaNome in regras[tipo]:
                camadasMap = QgsMapLayerRegistry.instance().mapLayersByName(camadaNome)
                for camadaMap in camadasMap:
                    if tipo == 'atributo':
                        for atributo in regras[tipo][camadaNome]:
                            camadaMap.conditionalStyles().setFieldStyles( atributo, regras[tipo][camadaNome][atributo] )
                    else:
                        camadaMap.conditionalStyles().setRowStyles( regras[tipo][camadaNome] )







