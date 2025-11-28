# Generated from Ensamblador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EnsambladorParser import EnsambladorParser
else:
    from EnsambladorParser import EnsambladorParser

# This class defines a complete generic visitor for a parse tree produced by EnsambladorParser.

class EnsambladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EnsambladorParser#programa.
    def visitPrograma(self, ctx:EnsambladorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnsambladorParser#linea.
    def visitLinea(self, ctx:EnsambladorParser.LineaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnsambladorParser#ultima_linea.
    def visitUltima_linea(self, ctx:EnsambladorParser.Ultima_lineaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnsambladorParser#etiqueta.
    def visitEtiqueta(self, ctx:EnsambladorParser.EtiquetaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnsambladorParser#instruccion.
    def visitInstruccion(self, ctx:EnsambladorParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnsambladorParser#operacionAritmetica.
    def visitOperacionAritmetica(self, ctx:EnsambladorParser.OperacionAritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnsambladorParser#mover.
    def visitMover(self, ctx:EnsambladorParser.MoverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnsambladorParser#comparar.
    def visitComparar(self, ctx:EnsambladorParser.CompararContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnsambladorParser#condicional.
    def visitCondicional(self, ctx:EnsambladorParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnsambladorParser#salto.
    def visitSalto(self, ctx:EnsambladorParser.SaltoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnsambladorParser#guardar_inst.
    def visitGuardar_inst(self, ctx:EnsambladorParser.Guardar_instContext):
        return self.visitChildren(ctx)



del EnsambladorParser