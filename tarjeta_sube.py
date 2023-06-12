class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

PRECIO_TICKET = 70
PRIMARIO = 50
SECUNDARIO = 40
UNIVERSITARIO = 30
JUBILADO = 25
ACTIVADO = "activado"
DESACTIVADO = "desactivado"

class Sube():
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO
        
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario != None:
            return PRECIO_TICKET - (PRECIO_TICKET * (self.grupo_beneficiario / 100))
        
        else:
            return PRECIO_TICKET
        
    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException("Usuario desactivado.")
        
        if self.grupo_beneficiario != None:
            if PRECIO_TICKET - (PRECIO_TICKET * (self.grupo_beneficiario / 100)) > self.saldo:
                raise NoHaySaldoException("Saldo insuficiente.")
            
            else:
                self.saldo -= PRECIO_TICKET - (PRECIO_TICKET * (self.grupo_beneficiario / 100))
        
        else:
            if PRECIO_TICKET > self.saldo:
                raise NoHaySaldoException("Saldo insuficiente.")
            
            else:
                self.saldo -= PRECIO_TICKET
                
    def cambiar_estado(self, estado):
        if estado != ACTIVADO and estado != DESACTIVADO:
            raise EstadoNoExistenteException("Estado no existente.")
        
        else:
            self.estado = estado
        
if __name__ == '__main__':
    pass
