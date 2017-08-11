# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import resources

class Action:
    def __init__(self, iface):
        self.inicializarVariaveis()
        self.definirIface(iface)
        self.definirAction(self.criarAction())

    def inicializarVariaveis(self):
        self.iface = None
        self.action = None
        self.controlador = None

    def definirIface(self, i):
        self.iface = i

    def obterIface(self):
        return self.iface

    def definirControlador(self, c):
        self.controlador = c

    def obterControlador(self):
        return self.controlador

    def definirAction(self, a):
        self.action = a

    def obterAction(self):
        return self.action

    def criarAction(self):
        action = QtGui.QAction(QtGui.QIcon(":/plugins/Configurador/visualizacoes/iconRegra.png"), u"Carregar Regras", self.obterIface().mainWindow())
        action.triggered.connect(self.rodar)
        return action

    def rodar(self):
        self.obterControlador().rodarComando("abrir frame")

    def adicionarAction(self):
        self.obterIface().digitizeToolBar().addAction(self.obterAction())

    def removerAction(self):
        self.obterIface().digitizeToolBar().removeAction(self.obterAction())

    def messagem(self):
        pass

