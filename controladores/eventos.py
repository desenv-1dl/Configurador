# -*- coding: utf-8 -*-

class Eventos:
    def __init__(self, configurador, action, frame):
        'construtor'
        self.configuradorModelo = configurador
        self.actionInterface = action
        self.actionInterface.definirControlador(self)
        self.frameInterface = frame
        self.frameInterface.definirControlador(self)
        self.inicializarComandos()

    def inicializarComandos(self):
        'Metodo para inicializar as alias dos eventos gerado entre camadas'
        self.comandos = {
        'configurar qgis' : self.configuradorModelo.configurar,
        'adicionar action' : self.actionInterface.adicionarAction,
        'remover action' : self.actionInterface.removerAction,
        'abrir frame' : self.frameInterface.mostrarFrame,
        'obter bancos de dados' : self.configuradorModelo.obterBancoDeDados().obterNomesDeBancosLogados,
        'obter tipos de regras' : self.configuradorModelo.obterBancoDeDados().obterTiposDeRegras,
        'definir conexao' : self.configuradorModelo.obterBancoDeDados().definirConexaoPostgres,
        'gerar regras' : self.configuradorModelo.obterGeradorDeRegras().gerarRegras,
                        }

    def rodarComando(self, cmd, params=None):
        'Metodo para filtrar os eventos'
        if params:
            r = self.comandos[cmd](params)
        else:
            r = self.comandos[cmd]()
        return (r if r else '')

