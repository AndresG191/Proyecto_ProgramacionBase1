from EnsambladorListener import EnsambladorListener
from EnsambladorParser import EnsambladorParser

class AnalizadorSemantico(EnsambladorListener):
    def __init__(self):
        print("DIAGNÓSTICO: Analizador Semántico Inicializado.")
        self.etiquetas_definidas = {}
        self.saltos_pendientes = []  # Guardamos saltos para validar después
        self.errores = []
        self.registros_usados = set()
        self.pasada = 1  # 1 = recolectar etiquetas, 2 = validar saltos

    # PRIMERA PASADA: solo recolectamos etiquetas
    def enterEtiqueta(self, ctx: EnsambladorParser.EtiquetaContext):
        if self.pasada == 1:
            etiqueta = ctx.ID().getText()
            linea = ctx.ID().getSymbol().line
            if etiqueta in self.etiquetas_definidas:
                self.errores.append(f"Error Semántico (Línea {linea}): Etiqueta duplicada '{etiqueta}'")
            else:
                self.etiquetas_definidas[etiqueta] = linea
                print(f"OK: Etiqueta '{etiqueta}' definida en línea {linea}")
    #Código muerto
    # def enterSalto(self, ctx: EnsambladorParser.SaltoContext):
    #     if self.pasada == 1:
    #         etiqueta = ctx.ID().getText()
    #         linea = ctx.start.line
    #         self.saltos_pendientes.append((etiqueta, linea, "salto"))
    #     else:
    #         self.validar_salto(ctx.ID().getText(), ctx.start.line, "salto")
    #
    # def enterCondicional(self, ctx: EnsambladorParser.CondicionalContext):
    #     if self.pasada == 1:
    #         etiqueta = ctx.ID().getText()
    #         linea = ctx.start.line
    #         self.saltos_pendientes.append((etiqueta, linea, "condicional"))
    #     else:
    #         self.validar_salto(ctx.ID().getText(), ctx.start.line, "condicional")

    def validar_salto(self, etiqueta, linea, tipo):
        if etiqueta not in self.etiquetas_definidas:
            self.errores.append(f"Error Semántico (Línea {linea}): {tipo.capitalize()} a etiqueta inexistente '{etiqueta}'")

    # Operaciones (se ejecutan en ambas pasadas)
    def enterOperacionAritmetica(self, ctx: EnsambladorParser.OperacionAritmeticaContext):
        if self.pasada == 2:
            comando = ctx.OPERACION_ARITMETICA().getText().lower()
            operador = ctx.OPERADOR().getText()
            linea = ctx.start.line

            esperado = {'sumar': '+', 'restar': '-', 'multiplicar': '*', 'dividir': '/'}
            if comando in esperado and operador != esperado[comando]:
                self.errores.append(f"Error Semántico (Línea {linea}): '{comando.capitalize()}' debe usar '{esperado[comando]}'")

            if comando == 'dividir':
                try:
                    if float(ctx.NUMERO(1).getText()) == 0:
                        self.errores.append(f"Error Semántico (Línea {linea}): División por cero")
                except:
                    pass

            reg = ctx.REGISTRO().getText()
            self.validar_registro(reg, linea)

    def enterMover(self, ctx: EnsambladorParser.MoverContext):
        if self.pasada == 2:
            self.validar_registro(ctx.REGISTRO().getText(), ctx.start.line)

    def enterGuardar_inst(self, ctx: EnsambladorParser.Guardar_instContext):
        if self.pasada == 2:
            self.validar_registro(ctx.REGISTRO().getText(), ctx.start.line)

    def validar_registro(self, reg, linea):
        if not reg.upper().startswith('R'):
            self.errores.append(f"Error Semántico (Línea {linea}): Registro inválido '{reg}'")
        else:
            self.registros_usados.add(reg.upper())

    def reportar_errores(self):
        if self.pasada == 1:
            print(f"\n--- PRIMERA PASADA COMPLETADA: {len(self.etiquetas_definidas)} etiquetas recolectadas ---")
            self.pasada = 2
            return False  # No terminado aún
        else:
            # Validar saltos pendientes
            for etiqueta, linea, tipo in self.saltos_pendientes:
                self.validar_salto(etiqueta, linea, tipo)

            if self.errores:
                print("\nERRORES SEMÁNTICOS DETECTADOS:")
                for e in self.errores:
                    print(f"   {e}")
            else:
                print("\nANÁLISIS SEMÁNTICO COMPLETADO: ¡CÓDIGO 100% VÁLIDO!")
            print(f"Etiquetas definidas: {list(self.etiquetas_definidas.keys())}")
            print(f"Registros usados: {sorted(self.registros_usados)}")
            return True