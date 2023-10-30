# Biblioteca de funciones para trabajar con cadenas


def longitud(cadena: str) -> int:
    """
    Calcula la longitud de una cadena.

    :param cadena: Cadena a evaluar.

    :return: Longitud de la cadena.
    """

    return len(cadena)


def invertir(cadena: str) -> str:
    """
    Invierte una cadena.

    :param cadena: Cadena a evaluar.

    :return: Cadena invertida.
    """

    return cadena[::-1]

print(invertir('hola'))
