#! -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from qgis.core import QgsConditionalStyle, QgsMapLayerRegistry, QgsVectorLayer, QgsDataSourceURI, QgsPoint, QGis, QgsGeometry, QgsProject, QgsField

class GeradorDeRegras:
    def __init__(self, iface, bancoDeDados):
        self.inicializarVariaveis()
        self.definirBancoDeDados(bancoDeDados)
        self.definirIface(iface)

    def inicializarVariaveis(self):
        self.iface = None
        self.bancoDeDados = None
        self.valoresDeRegra = None
        self.estiloRegra = None

    def definirBancoDeDados(self, b):
        self.bancoDeDados = b

    def obterBancoDeDados(self):
        return self.bancoDeDados

    def definirIface(self, i):
        self.iface = i

    def obterIface(self):
        return self.iface

    def gerarRegras(self, tipo):
        tabela = self.obterBancoDeDados().obterTabelaDeRegras(tipo)
        regrasPorAtributo = {}
        regrasPorLinha = {}
        for linha in tabela:
            self.definirValoresDeRegra(linha)
            self.definirEstiloDeRegra()
            if (self.obterValoresDeRegras()['atributo']) and (not self.obterValoresDeRegras()['atributo'] in regrasPorAtributo.keys()):
                regrasPorAtributo[ self.obterValoresDeRegras()['atributo'] ] = {
                                                                                    self.obterValoresDeRegras()['camada'] : []
                                                                               }
            if not  self.obterValoresDeRegras()['camada'] in self.regras.keys():
                regras[ self.obterValoresDeRegras()['camada'] ] = []
            regras[ self.obterValoresDeRegras()['camada'] ].append( self.obterEstiloDeRegra() )
        self.configurarRegrasEmCamadas(regras)

    def definirValoresDeRegra(self, linha):
        self.valoresDeRegra = {
                                'camada' : linha[0],
                                'tipo_regra' : linha[1],
                                'descricao' : linha[2],
                                'corRgb' : [ int(linha[3].split(',')[0]), int(linha[3].split(',')[1]), int(linha[3].split(',')[2])],
                                'regra' : linha[4]
                                'atributo' : linha[5]
                             }

    def obterValoresDeRegra(self):
        return self.valoresDeRegra

    def definirEstiloDeRegra(self):
        estilo = QgsConditionalStyle()
        estilo.setName( self.obterValoresDeRegra()['descricao'] )
        estilo.setRule( self.obterValoresDeRegra()['regra'] )
        estilo.setBackgroundColor(
                                    QtGui.QColor(
                                           self.obterValoresDeRegra()['corRgb'][0],
                                           self.obterValoresDeRegra()['corRgb'][1],
                                           self.obterValoresDeRegra()['corRgb'][2]
                                          )
                                 )
        self.estiloRegra = estilo

    def obterEstiloDeRegra(self):
        return self.estiloRegra

    def configurarRegrasEmCamadas(self, regras):
        camadas = QgsMapLayerRegistry.instance().mapLayersByName( self.obterValoresDeRegras()['camada'] )
        for camada in camadas:
            if self.obterValoresDeRegras()['tipo_regra'].lower() == 'atributo':
                camada.conditionalStyles().setFieldStyles( self.obterValoresDeRegras()['atributo'], regras[ self.obterValoresDeRegras()['camada'] ] )
            elif self.obterValoresDeRegras()['tipo_regra'].lower() == 'linha':
                camada.conditionalStyles().setRowStyles( self.obterValoresDeRegras()['camada'] )







