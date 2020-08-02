import random
from models.Bateria import Bateria
from models.Camara import Camara
from models.Motor import Motor
from models.Comportamiento import Comportamiento


class Robot:
    comportamiento = []
    recorrido = []
    padres = []
    camara = 0
    motor = 0
    bateria = 0
    costo = 0
    ultimaAccion = -1
    posicionActual = [19,0]
    direccion = 'N'

    def __init__(self):
        self.comportamiento = Comportamiento()
        self.camara = Camara(random.randint(1,3))
        self.motor = Motor(random.randint(1,3))
        self.bateria = Bateria(random.randint(1,3))

    def accion(self, tipoTerreno):
        accionRealizar =  self.comportamiento.decidirAccion()
    def moverAdelante(self):
        if(self.direccion=='N' and (self.posicionActual[0]!=0)):
            self.posicionActual[0] = self.posicionActual[0] - 1
        elif((self.direccion=='S') and (self.posicionActual[0]!=19)):
            self.posicionActual[0] = self.posicionActual[0] + 1
        elif ((self.direccion == 'E') and (self.posicionActual[1] != 19)):
            self.posicionActual[1] = self.posicionActual[1] + 1
        elif ((self.direccion == 'O') and (self.posicionActual[1] != 0)):
            self.posicionActual[1] = self.posicionActual[1] - 1
    def girarDerecha(self):
        if (self.direccion == 'N' ):
            self.direccion = 'E'
        elif (self.direccion == 'S'):
            self.direccion = 'O'
        elif (self.direccion == 'E'):
            self.direccion = 'S'
        elif (self.direccion == 'O'):
            self.direccion = 'N'
    def girarIzquierda(self):
        if (self.direccion == 'N'):
            self.direccion = 'O'
        elif (self.direccion == 'S'):
            self.direccion = 'E'
        elif (self.direccion == 'E'):
            self.direccion = 'N'
        elif (self.direccion == 'O'):
            self.direccion = 'S'
    def revisarFrente(self):
        if (self.camara.numero_espacios==1):
            return [[self.posicionActual[0]+1][self.posicionActual[1]+1][self.posicionActual[0]-1][self.posicionActual[1]-1]]
        elif(self.camara.numero_espacios==2):
            return [[[self.posicionActual[0] + 1][self.posicionActual[1] + 1][self.posicionActual[0] - 1][self.posicionActual[1] - 1]],
                    [[self.posicionActual[0] + 2][self.posicionActual[1] + 2][self.posicionActual[0] - 2][self.posicionActual[1] - 2]]]
        elif(self.camara.numero_espacios==3):
            return [[[self.posicionActual[0] + 1][self.posicionActual[1] + 1][self.posicionActual[0] - 1][self.posicionActual[1] - 1]],
            [[self.posicionActual[0] + 2][self.posicionActual[1] + 2][self.posicionActual[0] - 2][self.posicionActual[1] - 2]],
            [[self.posicionActual[0] + 3][self.posicionActual[1] + 3][self.posicionActual[0] - 3][self.posicionActual[1] - 3]]]










