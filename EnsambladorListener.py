# Generated from Ensamblador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EnsambladorParser import EnsambladorParser
else:
    from EnsambladorParser import EnsambladorParser

# This class defines a complete listener for a parse tree produced by EnsambladorParser.
class EnsambladorListener(ParseTreeListener):

    # Enter a parse tree produced by EnsambladorParser#programa.
    def enterPrograma(self, ctx:EnsambladorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#programa.
    def exitPrograma(self, ctx:EnsambladorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#instruccion.
    def enterInstruccion(self, ctx:EnsambladorParser.InstruccionContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#instruccion.
    def exitInstruccion(self, ctx:EnsambladorParser.InstruccionContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#operacionAritmetica.
    def enterOperacionAritmetica(self, ctx:EnsambladorParser.OperacionAritmeticaContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#operacionAritmetica.
    def exitOperacionAritmetica(self, ctx:EnsambladorParser.OperacionAritmeticaContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#mover.
    def enterMover(self, ctx:EnsambladorParser.MoverContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#mover.
    def exitMover(self, ctx:EnsambladorParser.MoverContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#comparar.
    def enterComparar(self, ctx:EnsambladorParser.CompararContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#comparar.
    def exitComparar(self, ctx:EnsambladorParser.CompararContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#condicional.
    def enterCondicional(self, ctx:EnsambladorParser.CondicionalContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#condicional.
    def exitCondicional(self, ctx:EnsambladorParser.CondicionalContext):
        pass


    # Enter a parse tree produced by EnsambladorParser#salto.
    def enterSalto(self, ctx:EnsambladorParser.SaltoContext):
        pass

    # Exit a parse tree produced by EnsambladorParser#salto.
    def exitSalto(self, ctx:EnsambladorParser.SaltoContext):
        pass



del EnsambladorParser