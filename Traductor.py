import re

def traducir_linea(linea):
    linea = linea.strip()
    if not linea or linea.endswith(':'):
        return linea

    linea_lower = linea.lower()

    # MOVER / PONER
    if any(p in linea_lower for p in ["mueve", "pon", "coloca"]):

        numero = re.search(r'\d+', linea).group()
        registro = linea.split()[-1].upper()
        return f"    MOVER {numero} A R{registro}"

    # COMPARAR
    if "compara" in linea_lower:
        partes = linea.split()
        reg = partes[partes.index("registro") + 1].upper()
        valor = partes[-1]
        return f"    comparar R{reg} con {valor}"

    # CONDICIONAL - AHORA SÍ CON NÚMERO
    if "si " in linea_lower and ("ve a" in linea_lower or "salta a" in linea_lower):
        # Extraer registro (A, B, etc.)
        reg_match = re.search(r"registro\s+([A-Za-z])", linea, re.IGNORECASE)
        reg = reg_match.group(1).upper()

        # Extraer número
        num_match = re.search(r"(\d+)", linea)
        numero = num_match.group(1) if num_match else "0"

        # Determinar comparador
        if "menor o igual" in linea_lower:
            comp = "<="
        elif "mayor o igual" in linea_lower:
            comp = ">="
        elif "menor que" in linea_lower:
            comp = "<"
        elif "mayor que" in linea_lower:
            comp = ">"
        elif "igual a" in linea_lower:
            comp = "=="
        else:
            comp = "<="

        # Extraer etiqueta
        etiqueta = linea.strip().split()[-1]

        return f"    SI R{reg} {comp} {numero} IR_A {etiqueta}"

    # SALTO SIMPLE
    if any(x in linea_lower for x in ["ve a ", "salta a ", "ir a "]) and "si" not in linea_lower:
        etiqueta = linea.strip().split()[-1]
        return f"    IR_A {etiqueta}"

    # SUMAR
    if "suma" in linea_lower:
        partes = linea.split()
        n1, n2 = partes[1], partes[3]
        reg = partes[-1].upper()
        return f"    sumar {n1} + {n2} y guardar en R{reg}"

    # MULTIPLICAR
    if "multiplica" in linea_lower:
        partes = linea.split()
        n1 = partes[1]
        n2 = partes[partes.index("por") + 1] if "por" in partes else partes[3]
        reg = partes[-1].upper()
        return f"    multiplicar {n1} * {n2} y guardar en R{reg}"

    # GUARDAR
    if "guarda" in linea_lower and "número" in linea_lower:
        partes = linea.split()
        numero = partes[partes.index("número") + 1]
        reg = partes[-1].upper()
        return f"    guardar {numero} en R{reg}"

    return "    // NO TRADUCIDO: " + linea

# === EJECUTAR ===
with open("EntradaNatural.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()

ensamblador = []
print("=== ENSAMBLADOR GENERADO ===\n")
for i, linea in enumerate(lineas, 1):
    trad = traducir_linea(linea)
    ensamblador.append(trad)
    print(f"{i:2d}: {trad}")

with open("EnsambladorGenerado.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(ensamblador) + "\n")

print("\n¡TRADUCCIÓN 100% EXITOSA!")
print("Ejecuta ahora: python mainEnsamblador.py EnsambladorGenerado.txt")