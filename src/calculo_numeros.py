from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    try:
        num = int(input("Ingrese un numero:"))

        if num < 0:
            raise NumeroDebeSerPositivo()
        
        return num
    except ValueError:
        raise ValueError("La entrada debe ser un numero valido.")

