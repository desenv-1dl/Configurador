# -*- coding: utf-8 -*-
from qgis.core import QgsProject
from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QToolBar, QPushButton
from geradorDeRegras import GeradorDeRegras
from bancoDeDados import BancoDeDados

class Configurador:
    def __init__(self, iface):
        'construtor'
        self.inicializarVariaveis()
        self.definirBancoDeDados(BancoDeDados())
        self.definirGeradorDeRegras(GeradorDeRegras(iface, self.obterBancoDeDados()))
        self.definirIface(iface)
        self.definirSettings(QSettings())
        self.iface.mapCanvas().keyPressed.connect(self.rodarAtalho)
        self.iface.actionToggleEditing().triggered.connect(self.definirSnap)
        self.limparAtalhos()

    def inicializarVariaveis(self):
        'Metodo para inicializar as variaveis da classe'
        self.settings = None
        self.iface = None
        self.definicoes = None
        self.geradorDeRegras = None
        self.bancoDeDados = None

    def definirGeradorDeRegras(self, g):
        'Metodo para registrar o objeto gerador de regras'
        self.geradorDeRegras = g

    def obterGeradorDeRegras(self):
        'Metodo para obter o objeto gerador de regras'
        return self.geradorDeRegras

    def definirBancoDeDados(self, b):
        'Metodo para registrar o banco de dados'
        self.bancoDeDados = b

    def obterBancoDeDados(self):
        'Metodo para obter objeto banco de dados'
        return self.bancoDeDados

    def definirIface(self, i):
        'Metodo para registrar o objeto Iface do qgis'
        self.iface = i

    def obterIface(self):
        'Metodo para obter o Iface do qgis'
        return self.iface

    def definirSettings(self, s):
        'Metodo para registrar o objeto QSettings'
        self.settings = s

    def obterSettings(self):
        'Metodo para obter o objeto QSettings'
        return self.settings

    def limparAtalhos(self):
        'Metodo para limpar os atalhos que seram usados e ja existem no qgis para evitar conflitos'
        s = self.obterSettings()
        for varAmbiente in s.allKeys():
            if (u'shortcuts' in varAmbiente):
                s.setValue(varAmbiente, u'')

    def configurar(self):
        'Loop para definir todas as configuracoes'
        s = self.obterSettings()
#        s.setValue("Qgis/newProjectDefault", u'true')
        for definicao in self.obterDefinicoes():
            s.setValue(definicao, self.obterDefinicoes()[definicao])

    def rodarAtalho(self, e):
        'Metodo para filtrar botoes que nao estao no configurador de atalho nativo do qgis'
        if e.text() == 'q':
            #voltar feicao
            self.encontrarBotoes(u'backInspectButton').click()
        elif e.text() == 'w':
            #proxima feicao
            self.encontrarBotoes(u'nextInspectButton').click()
        elif e.text() == 'g':
            #gabarito
            self.encontrarBotoes(u'drawShape').click()
        elif e.text() == 'f':
            #deletar no
            pass

    def encontrarBotoes(self, nome):
        'Metodo para pesquisar botoes escondidos para serem atalhados'
        for a in self.iface.mainWindow().findChildren(QToolBar):
            if a.objectName() == u'DsgTools':
                for b in a.findChildren(QPushButton):
                    if b.objectName() == nome:
                        return b

    def definirSnap(self):
        'Metodo para definir snap'
        layer = self.iface.activeLayer()
        if layer:
            proj = QgsProject.instance()
            proj.writeEntry('Digitizing', 'SnappingMode', 'all_layers')
            proj.writeEntry('Digitizing','DefaultSnapType', 'to vertex and segment') 
            proj.writeEntry('Digitizing','DefaultSnapTolerance', 5)
            proj.setSnapSettingsForLayer(layer.id(), True, 0, 0, 0, True)
            self.iface.actionToggleEditing().triggered.disconnect(self.definirSnap)

    def obterDefinicoes(self):
        'Definicao de todas as configuracoes em portugues e ingles'
        definicoes = {
            u'shortcuts/Sair do QGIS' : u'',
            u'shortcuts/Exit QGIS' : u'',
            u'shortcuts/Mesclar fei\xe7\xf5es selecionadas' : u'M',
            u'shortcuts/Merge Selected Features' : u'M',
            u'shortcuts/Quebrar Fei\xe7\xf5es' : u'C',
            u'shortcuts/Split Features' : u'C',
            u'shortcuts/Identificar fei\xe7\xf5es': u'I',
            u'shortcuts/Identify Features': u'I',
            u'shortcuts/Adicionar fei\xe7\xe3o': u'A',
            u'shortcuts/Add Feature': u'A',
            u'shortcuts/Desfazer sele\xe7\xe3o de fei\xe7\xf5es em todas as camadas': u'D',
            u'shortcuts/Deselect Features from All Layers': u'D',
            u'shortcuts/Ferramenta de n\xf3s' : u'N',
            u'shortcuts/Node Tool' : u'N',
            u'shortcuts/Salvar para todas as camadas' : u'Ctrl+S',
            u'shortcuts/Save for All Layers' : u'Ctrl+S',
            u'shortcuts/Habilitar tra\xe7ar' : u'T',
            u'shortcuts/Enable Tracing' : u'T',
            u'shortcuts/Remodelar fei\xe7\xf5es' : u'R',
            u'shortcuts/Reshape Features' : u'R',
            u'shortcuts/\xc1rea' : u'Z',
            u'shortcuts/Measure Area' : u'Z',
            u'shortcuts/Linha' : u'X',
            u'shortcuts/DSGTools: Generic Selector': u'S',
            u'shortcuts/DSGTools: Seletor Gen\xe9rico': u'S',
            u'shortcuts/DSGTools: Right Degree Angle Digitizing': u'E',
            u'shortcuts/DSGTools: Ferramenta de aquisi\xe7\xe3o com \xe2ngulos retos': u'E',
            u'shortcuts/Measure Line' : u'X',
            u'Qgis/parallel_rendering' : u'true',
            u'Qgis/max_threads' : 8,
            u'Qgis/simplifyDrawingHints': u'0',
            u'cache/size': 1048576,
            u'Qgis/digitizing/marker_only_for_selected' : u'true',
            u'Qgis/digitizing/default_snap_mode' : u'to vertex and segment',
            u'Qgis/default_selection_color_alpha': u'127',
            u'shortcuts/Salvar' : u'',
            u'shortcuts/Save' : u'',
            u'shortcuts/Select Feature(s)' : u'V',
            u'shortcuts/Fei\xe7\xe3o(s)' : u'V',
                          }
        return definicoes

