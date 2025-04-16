class NumeroDebeSerPositivo(Exception):
    pass
def ingrese_numero():
    entrada = input("Ingrese un número: ").strip()

    if not entrada:
        raise ValueError("La entrada no puede estar vacía")

    try:
        numero = int(entrada)
        if numero < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")