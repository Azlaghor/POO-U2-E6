class frequentFlyer:
    numTraveler = 0
    dni = 0
    name = ""
    lastname = ""
    miles = 0
    def __init__(self, vNumTrav, vDni, vName, vLastname, vMile):
        self.numTraveler = vNumTrav
        self.dni = vDni
        self.name = vName
        self.lastname = vLastname
        self.miles = vMile

    def returnMiles(self):
        return self.miles

    def accMiles(self, vAdd):
        self.miles += vAdd
        return self.miles

    def reedemMiles(self, vReedem):
        if vReedem <= self.miles:
            self.miles -= vReedem
        else:
            print("No tienes millas suficientes")
        
        return self.miles


    