# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic
import sys, os

sys.path.append(os.path.dirname(__file__))
GUI, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'frame.ui'), resource_suffix='')

class Frame(QtGui.QFrame, GUI):
    def __init__(self, iface):
        QtGui.QFrame.__init__(self)
        GUI.__init__(self)
        self.setupUi(self)
        self.inicializarVariaveis()
        self.definirIface(iface)
        self.gifLabel.setVisible(False)
        self.configurarGif()

    def inicializarVariaveis(self):
        self.controlador = None
        self.iface = None
        self.gif = None
        self.banco = None
        self.regra = None

    def definirIface(self, i):
        self.iface = i

    def obterIface(self):
        return self.iface

    def definirControlador(self, c):
        self.controlador = c

    def obterControlador(self):
        return self.controlador

    def definirBanco(self, b):
        self.banco = b

    def obterBanco(self):
        return self.banco

    def definirRegra(self, r):
        self.regra = r

    def obterRegra(self):
        return self.regra

    def configurarGif(self):
        gif = os.path.join(os.path.dirname(__file__), 'loading.gif')
        self.movie = QtGui.QMovie(gif)
        self.gifLabel.setMovie(self.movie)
        self.movie.start()

    def abrirGif(self):
        self.interfaceFrame.hide()
        self.gifLabel.setVisible(True)

    def fecharGif(self):
        self.interfaceFrame.show()
        self.gifLabel.setVisible(False)

    def mostrarFrame(self):
        self.carregarBancosEmCombo()
        self.carregarTiposDeRegrasEmCombo()
        self.show()

    def carregarBancosEmCombo(self):
       bancos = self.obterControlador().rodarComando('obter bancos de dados')
       self.carregarCombo(self.bancosCombo, bancos)

    def carregarTiposDeRegrasEmCombo(self):
        regras = self.obterControlador().rodarComando('obter tipos de regras')
        self.carregarCombo(self.regrasCombo, regras)

    def carregarCombo(self, combo, dados=None):
        combo.clear()
        combo.addItem(u'<Opções>')
        if dados:
            combo.addItems(dados)

    def haSelecao(self, s):
        if s != u'<Opções>':
            return True
        return False

    @QtCore.pyqtSlot(str)
    def on_bancosCombo_currentIndexChanged(self, texto):
        self.definirBanco(None)
        if self.haSelecao(texto):
            self.obterControlador().rodarComando('definir conexao', (texto,))
            self.definirBanco(texto)
            self.carregarTiposDeRegrasEmCombo()

    @QtCore.pyqtSlot(str)
    def on_regrasCombo_currentIndexChanged(self, texto):
        self.definirRegra(None)
        if self.haSelecao(texto):
            self.definirRegra(texto)

    @QtCore.pyqtSlot(bool)
    def on_carregarButton_clicked(self):
        if self.obterBanco() and self.obterRegra():
            self.abrirGif()
            self.obterControlador().rodarComando('gerar regras', (self.obterRegra(),))
            self.fecharGif()
            self.close()






