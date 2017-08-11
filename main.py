# -*- coding: utf-8 -*- 

from controladores.eventos import Eventos
from modelos.configurador import Configurador
from visualizacoes.action import Action
from visualizacoes.frame import Frame

class Main:
    def __init__(self, iface):
        '''construtor'''
        self.configurador = Configurador(iface)
        self.action = Action(iface)
        self.frame = Frame(iface)
        self.eventos = Eventos(self.configurador, self.action, self.frame)
        self.definirControlador(self.eventos)

    def definirControlador(self, c):
        'Metodo para definir controlador'
        self.controlador = c

    def obterControlador(self):
        'Metodo para obter controlador'
        return self.controlador

    def initGui(self):
        '''Metodo chamado na inicializacao do Qgis'''
        self.obterControlador().rodarComando('configurar qgis')
        self.obterControlador().rodarComando('adicionar action')


    def unload(self):
        '''Metodo chamado quando desinstala/desliga'''
        self.obterControlador().rodarComando('remover action')

