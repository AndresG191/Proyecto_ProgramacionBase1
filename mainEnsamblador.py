from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from EnsambladorLexer import EnsambladorLexer
from EnsambladorParser import EnsambladorParser


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        offending = offendingSymbol.text if offendingSymbol else "<EOF>"

        try:
            expected_tokens = recognizer.getExpectedTokens()
            symbolic_names = recognizer.symbolicNames

            expected = []
            token_types = list(expected_tokens)  # ← CORREGIDO AQUÍ

            for token_type in token_types:
                if 0 <= token_type < len(symbolic_names):
                    name = symbolic_names[token_type]
                    if name:
                        expected.append(name)

            expected_str = ', '.join(expected) if expected else "desconocido"

        except Exception as ex:
            expected_str = f"(error obteniendo tokens esperados: {ex})"

        print(f"   Error de sintaxis en línea {line}, columna {column}:")
        print(f"   Token inesperado: '{offending}'")
        print(f"   Se esperaba alguno de: {expected_str}")


def print_tokens(lexer):
    lexer.reset()
    token = lexer.nextToken()
    while token.type != Token.EOF:
        token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else f"UNKNOWN({token.type})"
        print(f"  {token_name:<20} → '{token.text}'")
        token = lexer.nextToken()


def run_test(input_text, label="Prueba"):
    print(f"\n {label}")
    print(f"Entrada: {repr(input_text)}")

    input_stream = InputStream(input_text)

    lexer = EnsambladorLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())

    print(" Tokens:")
    print_tokens(lexer)

    # Reconstruir el lexer y parser para análisis sintáctico
    input_stream = InputStream(input_text)
    lexer = EnsambladorLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = EnsambladorParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    try:
        tree = parser.programa()
        if tree is not None and tree.children:
            print("\n Árbol de análisis:")
            print(tree.toStringTree(recog=parser))
        else:
            print(" No se pudo generar el árbol de análisis (entrada inválida).")
    except Exception as e:
        print(f"[Parser Error] {type(e).__name__}: {e}")


def main():
    run_test("Sumar 5 + 3 y guardar en RA", "Prueba 1: Operación aritmética válida")
    run_test("mover 8 a RB", "Prueba 2: Movimiento válido")
    run_test("comparar RA con 10", "Prueba 3: Comparación válida")
    run_test("si RA >= 5 ir_a Inicio", "Prueba 4: Condicional válida")
    run_test("ir_a Fin", "Prueba 5: Salto válido")
    run_test("Sumar 5 de 3 y guardar en RA", "Prueba 6: Instrucción mal formada")  # negativa a propósito


if __name__ == '__main__':
    main()
