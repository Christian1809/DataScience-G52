# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# Las clases son plantillas para crear objetos (instancias)
# Una clase puede tener atributos (características) y métodos (funciones)

class Automovil:
    #creamos constructor de la clase
    def __init__(self, aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar
        
    #creamos un método
    def encender(self):
        print(f'Encender el automóvil {self.marca} {self.placa}')
        
    def avanzar(self):
        print(f'El automóvil {self.marca} {self.placa} está avanzando')
        
    def acelerar(self):
        print(f'El automóvil {self.marca} {self.placa} está acelerando')
        
    def frenar(self):
        print(f'El automóvil {self.marca} {self.placa} está frenando')
        
#creamos un objeto (instancia) de la clase Automovil
vw = Automovil(1970,'ch-1234','Amarillo','Volkswagen')
vw.encender()

tico = Automovil(2000,'ch-5678','rojo','Daewoo')
tico.encender()