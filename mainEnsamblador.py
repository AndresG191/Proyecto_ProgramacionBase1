import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from EnsambladorLexer import EnsambladorLexer
from EnsambladorParser import EnsambladorParser
from AnalizadorSemantico import AnalizadorSemantico

def main(argv):
    if len(argv) < 2:
        print("Uso: python mainEnsamblador.py <archivo.txt>")
        return

    archivo = argv[1]
    print(f"Analizando archivo: {archivo}")

    input_stream = FileStream(archivo, encoding='utf-8')
    lexer = EnsambladorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = EnsambladorParser(stream)

    parser.removeErrorListeners()
    error_listener = SyntaxErrorListener()
    parser.addErrorListener(error_listener)

    tree = parser.programa()

    if error_listener.has_errors():
        print("--- Error de Sintaxis ---")
        for error in error_listener.errores:
            print(error)
        return

    print("DIAGNÓSTICO: Análisis Sintáctico Correcto.")
    walker = ParseTreeWalker()
    semantico = AnalizadorSemantico()

    #Primera pasada; recolectar etiquetas
    walker.walk(semantico, tree)
    if not semantico.reportar_errores():
        print("--- SEGUNDA PASADA: Validando saltos y operaciones ---")
        walker.walk(semantico, tree)#aqui la segunda pasada
        semantico.reportar_errores()

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"   Error en línea {line}, columna {column}: {msg}"
        self.errores.append(error_msg)

    def has_errors(self):
        return len(self.errores) > 0

if __name__ == '__main__':
    main(sys.argv)