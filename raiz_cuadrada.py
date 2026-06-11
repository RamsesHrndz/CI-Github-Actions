def raiz_cuadrada(numero):
    if not isinstance(numero, (int, float)):
        raise TypeError("El argumento debe ser un número")
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    if numero == 0:
        return 0
    return numero ** 0.5
