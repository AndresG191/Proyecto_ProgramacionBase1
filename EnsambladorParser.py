# Generated from Ensamblador.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing import TextIO

def serializedATN():
    return [
        4,1,19,95,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,3,0,30,8,0,1,0,1,0,1,1,3,1,35,8,1,1,1,3,1,38,8,1,1,1,1,1,
        3,1,42,8,1,1,2,3,2,45,8,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,59,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,
        16,18,20,0,0,95,0,25,1,0,0,0,2,41,1,0,0,0,4,44,1,0,0,0,6,49,1,0,
        0,0,8,58,1,0,0,0,10,60,1,0,0,0,12,69,1,0,0,0,14,74,1,0,0,0,16,79,
        1,0,0,0,18,86,1,0,0,0,20,89,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,
        24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,29,1,0,0,0,27,25,1,
        0,0,0,28,30,3,4,2,0,29,28,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,
        32,5,0,0,1,32,1,1,0,0,0,33,35,3,6,3,0,34,33,1,0,0,0,34,35,1,0,0,
        0,35,37,1,0,0,0,36,38,3,8,4,0,37,36,1,0,0,0,37,38,1,0,0,0,38,39,
        1,0,0,0,39,42,5,17,0,0,40,42,5,17,0,0,41,34,1,0,0,0,41,40,1,0,0,
        0,42,3,1,0,0,0,43,45,3,6,3,0,44,43,1,0,0,0,44,45,1,0,0,0,45,47,1,
        0,0,0,46,48,3,8,4,0,47,46,1,0,0,0,47,48,1,0,0,0,48,5,1,0,0,0,49,
        50,5,15,0,0,50,51,5,16,0,0,51,7,1,0,0,0,52,59,3,10,5,0,53,59,3,12,
        6,0,54,59,3,14,7,0,55,59,3,16,8,0,56,59,3,18,9,0,57,59,3,20,10,0,
        58,52,1,0,0,0,58,53,1,0,0,0,58,54,1,0,0,0,58,55,1,0,0,0,58,56,1,
        0,0,0,58,57,1,0,0,0,59,9,1,0,0,0,60,61,5,1,0,0,61,62,5,13,0,0,62,
        63,5,11,0,0,63,64,5,13,0,0,64,65,5,9,0,0,65,66,5,3,0,0,66,67,5,7,
        0,0,67,68,5,14,0,0,68,11,1,0,0,0,69,70,5,2,0,0,70,71,5,13,0,0,71,
        72,5,10,0,0,72,73,5,14,0,0,73,13,1,0,0,0,74,75,5,4,0,0,75,76,5,14,
        0,0,76,77,5,8,0,0,77,78,5,13,0,0,78,15,1,0,0,0,79,80,5,5,0,0,80,
        81,5,14,0,0,81,82,5,12,0,0,82,83,5,13,0,0,83,84,5,6,0,0,84,85,5,
        15,0,0,85,17,1,0,0,0,86,87,5,6,0,0,87,88,5,15,0,0,88,19,1,0,0,0,
        89,90,5,3,0,0,90,91,5,13,0,0,91,92,5,7,0,0,92,93,5,14,0,0,93,21,
        1,0,0,0,8,25,29,34,37,41,44,47,58
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
                     "':'" ]

    symbolicNames = [ "<INVALID>", "OPERACION_ARITMETICA", "MOVER", "GUARDAR", 
                      "COMPARAR", "SI", "IR_A", "EN", "CON", "Y", "A", "OPERADOR", 
                      "COMPARADOR", "NUMERO", "REGISTRO", "ID", "DOS_PUNTOS", 
                      "NEWLINE", "WS", "COMENTARIO" ]

    RULE_programa = 0
    RULE_linea = 1
    RULE_ultima_linea = 2
    RULE_etiqueta = 3
    RULE_instruccion = 4
    RULE_operacionAritmetica = 5
    RULE_mover = 6
    RULE_comparar = 7
    RULE_condicional = 8
    RULE_salto = 9
    RULE_guardar_inst = 10

    ruleNames =  [ "programa", "linea", "ultima_linea", "etiqueta", "instruccion", 
                   "operacionAritmetica", "mover", "comparar", "condicional", 
                   "salto", "guardar_inst" ]

    EOF = Token.EOF
    OPERACION_ARITMETICA=1
    MOVER=2
    GUARDAR=3
    COMPARAR=4
    SI=5
    IR_A=6
    EN=7
    CON=8
    Y=9
    A=10
    OPERADOR=11
    COMPARADOR=12
    NUMERO=13
    REGISTRO=14
    ID=15
    DOS_PUNTOS=16
    NEWLINE=17
    WS=18
    COMENTARIO=19

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

        def EOF(self):
            return self.getToken(EnsambladorParser.EOF, 0)

        def linea(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EnsambladorParser.LineaContext)
            else:
                return self.getTypedRuleContext(EnsambladorParser.LineaContext,i)


        def ultima_linea(self):
            return self.getTypedRuleContext(EnsambladorParser.Ultima_lineaContext,0)


        def getRuleIndex(self):
            return EnsambladorParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = EnsambladorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 22
                    self.linea() 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 28
                self.ultima_linea()


            self.state = 31
            self.match(EnsambladorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(EnsambladorParser.NEWLINE, 0)

        def etiqueta(self):
            return self.getTypedRuleContext(EnsambladorParser.EtiquetaContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(EnsambladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return EnsambladorParser.RULE_linea

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinea" ):
                listener.enterLinea(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinea" ):
                listener.exitLinea(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinea" ):
                return visitor.visitLinea(self)
            else:
                return visitor.visitChildren(self)




    def linea(self):

        localctx = EnsambladorParser.LineaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_linea)
        self._la = 0 # Token type
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 33
                    self.etiqueta()


                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0):
                    self.state = 36
                    self.instruccion()


                self.state = 39
                self.match(EnsambladorParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(EnsambladorParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ultima_lineaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def etiqueta(self):
            return self.getTypedRuleContext(EnsambladorParser.EtiquetaContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(EnsambladorParser.InstruccionContext,0)


        def getRuleIndex(self):
            return EnsambladorParser.RULE_ultima_linea

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUltima_linea" ):
                listener.enterUltima_linea(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUltima_linea" ):
                listener.exitUltima_linea(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUltima_linea" ):
                return visitor.visitUltima_linea(self)
            else:
                return visitor.visitChildren(self)




    def ultima_linea(self):

        localctx = EnsambladorParser.Ultima_lineaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ultima_linea)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 43
                self.etiqueta()


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0):
                self.state = 46
                self.instruccion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EtiquetaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(EnsambladorParser.ID, 0)

        def DOS_PUNTOS(self):
            return self.getToken(EnsambladorParser.DOS_PUNTOS, 0)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_etiqueta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEtiqueta" ):
                listener.enterEtiqueta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEtiqueta" ):
                listener.exitEtiqueta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEtiqueta" ):
                return visitor.visitEtiqueta(self)
            else:
                return visitor.visitChildren(self)




    def etiqueta(self):

        localctx = EnsambladorParser.EtiquetaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_etiqueta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(EnsambladorParser.ID)
            self.state = 50
            self.match(EnsambladorParser.DOS_PUNTOS)
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


        def guardar_inst(self):
            return self.getTypedRuleContext(EnsambladorParser.Guardar_instContext,0)


        def getRuleIndex(self):
            return EnsambladorParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = EnsambladorParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instruccion)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.operacionAritmetica()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.mover()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.comparar()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.condicional()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.salto()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.guardar_inst()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionAritmetica" ):
                return visitor.visitOperacionAritmetica(self)
            else:
                return visitor.visitChildren(self)




    def operacionAritmetica(self):

        localctx = EnsambladorParser.OperacionAritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operacionAritmetica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(EnsambladorParser.OPERACION_ARITMETICA)
            self.state = 61
            self.match(EnsambladorParser.NUMERO)
            self.state = 62
            self.match(EnsambladorParser.OPERADOR)
            self.state = 63
            self.match(EnsambladorParser.NUMERO)
            self.state = 64
            self.match(EnsambladorParser.Y)
            self.state = 65
            self.match(EnsambladorParser.GUARDAR)
            self.state = 66
            self.match(EnsambladorParser.EN)
            self.state = 67
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMover" ):
                return visitor.visitMover(self)
            else:
                return visitor.visitChildren(self)




    def mover(self):

        localctx = EnsambladorParser.MoverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mover)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(EnsambladorParser.MOVER)
            self.state = 70
            self.match(EnsambladorParser.NUMERO)
            self.state = 71
            self.match(EnsambladorParser.A)
            self.state = 72
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparar" ):
                return visitor.visitComparar(self)
            else:
                return visitor.visitChildren(self)




    def comparar(self):

        localctx = EnsambladorParser.CompararContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(EnsambladorParser.COMPARAR)
            self.state = 75
            self.match(EnsambladorParser.REGISTRO)
            self.state = 76
            self.match(EnsambladorParser.CON)
            self.state = 77
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = EnsambladorParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(EnsambladorParser.SI)
            self.state = 80
            self.match(EnsambladorParser.REGISTRO)
            self.state = 81
            self.match(EnsambladorParser.COMPARADOR)
            self.state = 82
            self.match(EnsambladorParser.NUMERO)
            self.state = 83
            self.match(EnsambladorParser.IR_A)
            self.state = 84
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSalto" ):
                return visitor.visitSalto(self)
            else:
                return visitor.visitChildren(self)




    def salto(self):

        localctx = EnsambladorParser.SaltoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_salto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(EnsambladorParser.IR_A)
            self.state = 87
            self.match(EnsambladorParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Guardar_instContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GUARDAR(self):
            return self.getToken(EnsambladorParser.GUARDAR, 0)

        def NUMERO(self):
            return self.getToken(EnsambladorParser.NUMERO, 0)

        def EN(self):
            return self.getToken(EnsambladorParser.EN, 0)

        def REGISTRO(self):
            return self.getToken(EnsambladorParser.REGISTRO, 0)

        def getRuleIndex(self):
            return EnsambladorParser.RULE_guardar_inst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGuardar_inst" ):
                listener.enterGuardar_inst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGuardar_inst" ):
                listener.exitGuardar_inst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGuardar_inst" ):
                return visitor.visitGuardar_inst(self)
            else:
                return visitor.visitChildren(self)




    def guardar_inst(self):

        localctx = EnsambladorParser.Guardar_instContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_guardar_inst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(EnsambladorParser.GUARDAR)
            self.state = 90
            self.match(EnsambladorParser.NUMERO)
            self.state = 91
            self.match(EnsambladorParser.EN)
            self.state = 92
            self.match(EnsambladorParser.REGISTRO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





