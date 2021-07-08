""" 
    Modulo tipocliente -
    Classe TipoCliente - Enumeration de Tipos de Cliente
"""

import enum
 
class TipoCliente(enum.Enum):
    PESSOA_FISICA = 1
    PESSOA_JURIDICA = 2

    def retonar_enum(numero : int):
        for tipo in (TipoCliente):
            if tipo.value == numero:
                return tipo
        return None

if __name__ == '__main__':
    print ("Os numeros enum sao: ")
    for tipo in (TipoCliente):
        print(type(tipo))
        print(tipo)