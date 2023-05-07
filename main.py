# ================IMPORT================ #
from classes import frequentFlyer

# ================FUNCTIONS================ #
def findTraveller(vNum, vList):
    i = 0
    findTrav = None
    while i < len(vList) and not findTrav:
        if vList[i].numTraveler == vNum:
            findTrav = vList[i]
        i += 1
    
    return findTrav


# ================MAIN================ #
if __name__ == "__main__":
    travellerList = []
    with open("data.txt", "r") as archive:
        for line in archive:
            data = line.split(",")
            traveller = frequentFlyer(int(data[0]), data[1], data[2], data[3], int(data[4]))
            travellerList.append(traveller)

    while True:
        numTrav = input("Ingrese su numero de viajero frecuente: ")
        if numTrav.isdigit() == True:
            tempObj = findTraveller(int(numTrav), travellerList)
            if tempObj == None:
                print("El Numero de viajero no existe")
            else:
                break
        else:
            print("No se ingreso un numero valido.")

    print("""¿Que desea realizar?:
    a: Consultar cantidad de millas.
    b: Acumular millas.
    c: Canjear Millas.
    d: Salir.""")
    

    while True:
        option = input("Ingrese la opcion deseada (a-b-c-d): ")
        # option.lower()
        if option == "a":
            print("Su cantidad de millas", tempObj.returnMiles())
        elif option == "b":
            print(tempObj.accMiles(int(input("Ingrese la cantidad de millas que desea sumar: "))))
        elif option == "c":
            print(tempObj.reedemMiles(int(input("Ingrese la cantidad de millas a canjear: "))))
        elif option == "d":
            print("Espero haber sido util. By Lucifer")
            break
        else:

            print("Opcion incorrecta.")