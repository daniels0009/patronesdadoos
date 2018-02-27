class Motor(object):
    def __init__(self):
        pass

    def acelerar(self):
        pass

    def getRPM(self):
        currentRPM = 0
        #...
        return currentRPM

"""Para desacoplar motor de vehiculo:
class Vehiculo(object):
    def __init__(self, motor)"""

class Vehiculo(object):
    def __init__(self):
        self._motor = Motor()

    def getMotorRPM(self)
        return self._motor.getRPM();
