#! -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSettings
import psycopg2

class BancoDeDados(QtCore.QObject):
    def __init__(self):
        'Construtor'
        QtCore.QObject.__init__(self)
        self.inicializarVariaveis()
        self.definirSettings(QSettings())

    def inicializarVariaveis(self):
        'Metodo para inicializar variaveis'
        self.settings = None
        self.conexao = None

    def definirSettings(self, s):
        'Metodo para registrar objeto de configuracoes'
        self.settings = s
        self.settings.beginGroup("PostgreSQL/connections")

    def obterSettings(self):
        'Metodo para obter objeto de configuracoes'
        return self.settings

    def definirConexaoPostgres(self, b):
        'Metodo para registrar conexao com o postgres'
        self.obterConexaoPostgres().close() if self.obterConexaoPostgres() else ''
        db = b[0]
        if db:
            host = self.obterSettings().value(db+"/host")
            port = self.obterSettings().value(db+"/port")
            database = self.obterSettings().value(db+"/database")
            username = self.obterSettings().value(db+'/username')
            password = self.obterSettings().value(db+'/password')
            conn_string = "host="+host+" dbname="+database+" user="+username+" password="+password+" port="+port
            conn = psycopg2.connect(conn_string)
            self.conexao = conn.cursor()

    def obterConexaoPostgres(self):
        'Metodo para obter conexao com o postgres'
        return self.conexao

    def obterNomesDeBancosLogados(self):
        'Metodo para obter o nome de todos os bancos que o usuario esta logado'
        bancos = []
        for info in self.obterSettings().allKeys():
            if info[-9:] == "/username":
                bancos.append(info[:-9])
        return tuple(bancos)

    def obterTiposDeRegras(self):
        try:
            self.obterConexaoPostgres().execute("""select tipo_estilo from public.layer_rules;""")
        except:
            return
        else:
            resultado = self.obterConexaoPostgres().fetchall()
            tiposDeRegras = list(set([x[0] for x in resultado]))
            return tiposDeRegras

    def obterTabelaDeRegras(self, tipo):
        try:
            if (tipo[0].lower() == u'aquisicao') or (tipo[0].lower() == u'aquisição'):
                self.obterConexaoPostgres().execute("""select * from public.layer_rules where tipo_estilo = 'aquisicao';""")
            elif (tipo[0].lower() == u'reambulacao') or (tipo[0].lower() == u'reambulação'):
                self.obterConexaoPostgres().execute("""select * from public.layer_rules ;""")
        except:
            return
        else:
            resultado = self.obterConexaoPostgres().fetchall()
            return resultado





