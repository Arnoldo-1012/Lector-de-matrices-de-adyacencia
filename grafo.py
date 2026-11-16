import sys


def leer_matriz(ruta):
    nombres = []
    matriz = []
    with open(ruta, encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            if linea.startswith("#"):
                nombres = linea[1:].split()
            else:
                matriz.append([int(x) for x in linea.split()])
    return nombres, matriz


def validar_matriz(matriz):
    n = len(matriz)
    for i in range(n):
        if len(matriz[i]) != n:
            raise ValueError("La matriz no es cuadrada (fila %d)" % (i + 1))
        if matriz[i][i] != 0:
            raise ValueError("Hay un lazo en el vertice %d" % (i + 1))
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                raise ValueError("La matriz no es simetrica en (%d, %d)" % (i + 1, j + 1))


def contar_vertices(matriz):
    return len(matriz)


def contar_aristas(matriz):
    n = len(matriz)
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            total += matriz[i][j]
    return total


def calcular_grados(matriz):
    return [sum(fila) for fila in matriz]


def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 else "matriz_amigos.txt"
    nombres, matriz = leer_matriz(ruta)
    validar_matriz(matriz)

    n = contar_vertices(matriz)
    m = contar_aristas(matriz)
    grados = calcular_grados(matriz)
    if not nombres:
        nombres = ["v%d" % (i + 1) for i in range(n)]

    print("Archivo leido:", ruta)
    print("n (vertices) =", n)
    print("m (aristas)  =", m)
    print()
    print("Grado de cada vertice:")
    for nombre, g in zip(nombres, grados):
        print("  %-10s %d" % (nombre, g))
    print()
    print("Suma de grados =", sum(grados), "(debe ser 2m =", 2 * m, ")")
    print("Grado maximo   =", max(grados), "->", ", ".join(nombres[i] for i in range(n) if grados[i] == max(grados)))
    print("Grado minimo   =", min(grados), "->", ", ".join(nombres[i] for i in range(n) if grados[i] == min(grados)))


main()
