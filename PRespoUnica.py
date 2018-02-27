class Vehiculo(object):
    def __init__(self, nombre, motor):
        self._nombre = nombre
        self._motor = motor

    def getNombre(self):
        return self._nombre()

    def getMotorRPM(self):
        return self._motor.getRPM()

    def getVelocidad(self):
        return self._velocidad

"""Manejo de persistencia"""
class ConstruirVehiculo(object):
    def __init__(self, vehiculo, db)
        self._persistence = db
        self._vehiculo = vehiculo

"""Capa de presentacion"""
class MostrarVehiculo(object):
    def __init__(self, vehiculo, db)
        self._persistence = db
        self._vehiculo = vehiculo

    def print(self):
        return print ‘Vehicle: {}, Velocidad: {}, RMP: {}’.format(self._vehiculo.getNombre(), self._vehiculo.getVelocidad(), self._vehiculo.getRPM())
