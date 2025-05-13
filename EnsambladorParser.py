# Generated from Ensamblador.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,0,0,7,0,2,4,
        6,8,10,12,0,0,53,0,15,1,0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,35,1,0,
        0,0,8,40,1,0,0,0,10,45,1,0,0,0,12,52,1,0,0,0,14,16,3,2,1,0,15,14,
        1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,
        25,3,4,2,0,20,25,3,6,3,0,21,25,3,8,4,0,22,25,3,10,5,0,23,25,3,12,
        6,0,24,19,1,0,0,0,24,20,1,0,0,0,24,21,1,0,0,0,24,22,1,0,0,0,24,23,
        1,0,0,0,25,3,1,0,0,0,26,27,5,1,0,0,27,28,5,18,0,0,28,29,5,16,0,0,
        29,30,5,18,0,0,30,31,5,14,0,0,31,32,5,7,0,0,32,33,5,11,0,0,33,34,
        5,19,0,0,34,5,1,0,0,0,35,36,5,6,0,0,36,37,5,18,0,0,37,38,5,15,0,
        0,38,39,5,19,0,0,39,7,1,0,0,0,40,41,5,8,0,0,41,42,5,19,0,0,42,43,
        5,12,0,0,43,44,5,18,0,0,44,9,1,0,0,0,45,46,5,9,0,0,46,47,5,19,0,
        0,47,48,5,17,0,0,48,49,5,18,0,0,49,50,5,10,0,0,50,51,5,20,0,0,51,
        11,1,0,0,0,52,53,5,10,0,0,53,54,5,20,0,0,54,13,1,0,0,0,2,17,24
    ]

class EnsambladorParser ( Parser ):

    grammarFileName = "Ensamblador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "OPERACION_ARITMETICA", "SUMAR", "RESTAR", 
                      "MULTIPLICAR", "DIVIDIR", "MOVER", "GUARDAR", "COMPARAR", 
                      "SI", "IR_A", "EN", "CON", "DE", "Y", "A", "OPERADOR", 
                      "COMPARADOR", "NUMERO", "REGISTRO", "ID", "ETIQUETA", 
                      "COMA", "NEWLINE", "WS", "COMENTARIO" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_operacionAritmetica = 2
    RULE_mover = 3
    RULE_comparar = 4
    RULE_condicional = 5
    RULE_salto = 6

    ruleNames =  [ "programa", "instruccion", "operacionAritmetica", "mover", 
                   "comparar", "condicional", "salto" ]

    EOF = Token.EOF
    OPERACION_ARITMETICA=1
    SUMAR=2
    RESTAR=3
    MULTIPLICAR=4
    DIVIDIR=5
    MOVER=6
    GUARDAR=7
    COMPARAR=8
    SI=9
    IR_A=10
    EN=11
    CON=12
    DE=13
    Y=14
    A=15
    OPERADOR=16
    COMPARADOR=17
    NUMERO=18
    REGISTRO=19
    ID=20
    ETIQUETA=21
    COMA=22
    NEWLINE=23
    WS=24
    COMENTARIO=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnsambladorParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(EnsambladorParser.InstruccionContext,i)


        def getRuleIndex(self):
            return EnsambladorParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = EnsambladorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.instruccion()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1858) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operacionAritmetica(self):
            return self.getTypedRuleContext(EnsambladorParser.OperacionAritmeticaContext,0)


        def mover(self):
            return self.getTypedRuleContext(EnsambladorParser.MoverContext,0)


        def comparar(self):
            return self.getTypedRuleContext(EnsambladorParser.CompararContext,0)


        def condicional(self):
            return self.getTypedRuleContext(EnsambladorParser.CondicionalContext,0)


        def salto(self):
            return self.getTypedRuleContext(EnsambladorParser.SaltoContext,0)


        def getRuleIndex(self):
            return EnsambladorParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)




    def instruccion(self):

        localctx = EnsambladorParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.operacionAritmetica()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.mover()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.comparar()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 22
                self.condicional()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 23
                self.salto()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionAritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERACION_ARITMETICA(self):
            return self.getToken(EnsambladorParser.OPERACION_ARITMETICA, 0)

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(EnsambladorParser.NUMERO)
            else:
                return self.getToken(EnsambladorParser.NUMERO, i)

        def OPERADOR(self):
            return self.getToken(EnsambladorParser.OPERADOR, 0)

        def Y(self):
            return self.getToken(EnsambladorParser.Y, 0)

        def GUARDAR(self):
            return self.getToken(EnsambladorParser.GUARDAR, 0)

        def EN(self):
            return self.getToken(EnsambladorParser.EN, 0)

        def REGISTRO(self):
            return self.getToken(EnsambladorParser.REGISTRO, 0)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_operacionAritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionAritmetica" ):
                listener.enterOperacionAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionAritmetica" ):
                listener.exitOperacionAritmetica(self)




    def operacionAritmetica(self):

        localctx = EnsambladorParser.OperacionAritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operacionAritmetica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(EnsambladorParser.OPERACION_ARITMETICA)
            self.state = 27
            self.match(EnsambladorParser.NUMERO)
            self.state = 28
            self.match(EnsambladorParser.OPERADOR)
            self.state = 29
            self.match(EnsambladorParser.NUMERO)
            self.state = 30
            self.match(EnsambladorParser.Y)
            self.state = 31
            self.match(EnsambladorParser.GUARDAR)
            self.state = 32
            self.match(EnsambladorParser.EN)
            self.state = 33
            self.match(EnsambladorParser.REGISTRO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVER(self):
            return self.getToken(EnsambladorParser.MOVER, 0)

        def NUMERO(self):
            return self.getToken(EnsambladorParser.NUMERO, 0)

        def A(self):
            return self.getToken(EnsambladorParser.A, 0)

        def REGISTRO(self):
            return self.getToken(EnsambladorParser.REGISTRO, 0)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_mover

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMover" ):
                listener.enterMover(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMover" ):
                listener.exitMover(self)




    def mover(self):

        localctx = EnsambladorParser.MoverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mover)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(EnsambladorParser.MOVER)
            self.state = 36
            self.match(EnsambladorParser.NUMERO)
            self.state = 37
            self.match(EnsambladorParser.A)
            self.state = 38
            self.match(EnsambladorParser.REGISTRO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompararContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPARAR(self):
            return self.getToken(EnsambladorParser.COMPARAR, 0)

        def REGISTRO(self):
            return self.getToken(EnsambladorParser.REGISTRO, 0)

        def CON(self):
            return self.getToken(EnsambladorParser.CON, 0)

        def NUMERO(self):
            return self.getToken(EnsambladorParser.NUMERO, 0)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_comparar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparar" ):
                listener.enterComparar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparar" ):
                listener.exitComparar(self)




    def comparar(self):

        localctx = EnsambladorParser.CompararContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comparar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(EnsambladorParser.COMPARAR)
            self.state = 41
            self.match(EnsambladorParser.REGISTRO)
            self.state = 42
            self.match(EnsambladorParser.CON)
            self.state = 43
            self.match(EnsambladorParser.NUMERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(EnsambladorParser.SI, 0)

        def REGISTRO(self):
            return self.getToken(EnsambladorParser.REGISTRO, 0)

        def COMPARADOR(self):
            return self.getToken(EnsambladorParser.COMPARADOR, 0)

        def NUMERO(self):
            return self.getToken(EnsambladorParser.NUMERO, 0)

        def IR_A(self):
            return self.getToken(EnsambladorParser.IR_A, 0)

        def ID(self):
            return self.getToken(EnsambladorParser.ID, 0)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)




    def condicional(self):

        localctx = EnsambladorParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(EnsambladorParser.SI)
            self.state = 46
            self.match(EnsambladorParser.REGISTRO)
            self.state = 47
            self.match(EnsambladorParser.COMPARADOR)
            self.state = 48
            self.match(EnsambladorParser.NUMERO)
            self.state = 49
            self.match(EnsambladorParser.IR_A)
            self.state = 50
            self.match(EnsambladorParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaltoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IR_A(self):
            return self.getToken(EnsambladorParser.IR_A, 0)

        def ID(self):
            return self.getToken(EnsambladorParser.ID, 0)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_salto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSalto" ):
                listener.enterSalto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSalto" ):
                listener.exitSalto(self)




    def salto(self):

        localctx = EnsambladorParser.SaltoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_salto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(EnsambladorParser.IR_A)
            self.state = 53
            self.match(EnsambladorParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





