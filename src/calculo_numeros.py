from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    try:
        num = int(input("Ingrese un numero: "))

        if num < 0:
            raise NumeroDebeSerPositivo()
        
        return num
    except ValueError:
        raise ValueError("La entrada debe ser un numero valido.")

def main():
    while True:
        try:
            num = ingrese_numero()
            print(f"Número valido: {num}")
        except NumeroDebeSerPositivo as error1:
            print(f"Error: {error1}")
        except ValueError as error2:
            print(f"Error: {error2}")

        continuar = input("Desea seguir? (s/n): ")
        if continuar.lower() != "s":
            break

if __name__ == "__main__":
    main()