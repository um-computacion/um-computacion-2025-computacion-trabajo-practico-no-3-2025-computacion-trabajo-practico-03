class NumeroDebeSerPositivo(Exception): #Excepcion cuando un num es negativo
    def __init__(self, mensaje="El número debe ser positivo." ):
        self.mensaje = mensaje
        super().__init__(self.mensaje)