opcion,p = "",""
coordenadas = []
jugador1, jugador2 = [],[]
player = 0

def cordenadas(path):

    archivo = open(path, encoding="utf16", errors="ignore")
    cont3 = 0
    lector = ""
    final=[]

    lector = archivo.read()
    final = lector.split()
    
    barco, barco2, barco3, barco4 = [],[],[],[]

    for cont3 in range(len(final)):

        y = 0
        x = 0

        y = int(cont3/10)
        x = int(round(((cont3/10)-y)*10))

        if final[cont3]=="1":
            barco.append([x+1,y+1])
        elif final[cont3]=="2":
            barco2.append([x+1,y+1])
        elif final[cont3]=="3":
            barco3.append([x+1,y+1])
        if final[cont3]=="4":
            barco4.append([x+1,y+1])

    return barco, barco2,barco3,barco4

def cargar():

    entrada = ""
    posciciones = [[],[]]
    cont2 = 0

    #loop para subir los archivos
    while True:
        print("por favor suba el archivo del jugador #",cont2+1)
        entrada = input()
        #use el try para 
        try:
            posciciones[cont2]=cordenadas(entrada)
            print("se ha subido de manera exitosa el archivo")
            cont2 += 1
            if cont2 == 2: break
        except FileNotFoundError:
            print("por favor vuelvalo a subir")

    print("gracias por subir los archivos, regresandolo al menu")
    return posciciones

def jugador(koordinaten):
    print(koordinaten)

    p = input("ingrese donde quiere atacar: ")
    player = p.split(",")
    cont2,cont3 = 0,0

    for cont2 in range(len(koordinaten)):
        for cont3 in range(len(koordinaten[cont2])):
            print(cont3)
            if player == koordinaten[cont2][cont3]:
                print("acertaste")
                break
            if cont3 == len(koordinaten[cont2])-1:
                print("fallaste")

def jugar(coordinates):

    jugador1 = coordinates[0]
    jugador2 = coordinates[1]
    print(jugador1,jugador2)

    jugador(jugador2)
    jugador(jugador1)

while True:
    #menu de opciones
    print("Escoga una opcion")
    print("a)carga de archivos")
    print("b)jugar")
    print("c)terminar")
    
    opcion = input()

    if opcion == "a":
        coordenadas = cargar()

    elif opcion == "b":
        jugar(coordenadas)

    elif opcion == "c":
        break
    else:
        print("por favor ingrese una opcion valida")
