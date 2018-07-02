import random
#Inicio del programa
bombos = []
for i in range(1,5):
        archivo = "bombo"+str(i)+".txt"
        leer_archivo = open(archivo)
        bombo = leer_archivo.readline()
        lista = bombo.split(", ")
        bombos.append(lista)
grupo = []
lista_grupos = []
for i in range(8):
        for i in bombos:
                posicion = random.randint(0,len(i)-1)
                grupo.append(i[posicion])
                i.remove(i[posicion])
        lista_grupos.append(grupo[:])
        grupo.clear()
print(" ")
letra=["A", "B", "C", "D", "E", "F", "G", "H"]
for i in range(8):
        print("Grupo",letra[i],":",", ".join(lista_grupos[i]))
#Grupos
dicc = {"Alemania":0,"Arabia Saudita":1, "Argentina":2, "Australia":3, "Belgica":4, "Brasil":5, "Colombia":6, "Corea del Sur":7,
        "Costa Rica":8, "Croacia":9, "Dinamarca":10, "Egipto":11, "España":12,"Francia":13,"Inglaterra":14,"Iran":15,"Islandia":16,
        "Japon":17, "Marruecos":18,"Mexico":19, "Nigeria":20,"Panama":21,"Peru":22,"Polonia":23,"Portugal":24,"Rusia":25,"Senegal":26,
        "Serbia":27,"Suecia":28,"Suiza":29,"Tunez":30,"Uruguay":31}
#Este es el diccionario para el nombre de cada equipo
tab = [[0,0.27,0.60,0.10,0.50,0.04,0.34,0.12,0.26,0.24,0.22,0.23,0.99,0.44,0.02,0.43,0.60,0.19,0.54,0.25,0.35,0.35,0.00,0.35,0.62,0.17,0.69,0.62,0.88,0.52,0.49,0.46],
        [0,0,0.66,0.29,0.93,0.19,0.91,0.36,0.59,0.45,0.88,0.25,0.18,0.01,0.19,0.73,0.65,0.01,0.82,0.70,0.77,0.54,0.05,0.68,0.87,0.77,0.16,0.47,0.34,0.73,0.53,0.60],
        [0,0,0,0.99,0.01,0.35,0.54,0.40,0.51,0.39,0.13,0.02,0.02,0.05,0.62,0.50,0.53,0.94,0.07,0.02,0.62,0.85,0.33,0.16,0.21,0.66,0.81,0.93,0.20,0.21,0.67,0.67],
        [0,0,0,0,0.16,0.44,0.02,0.84,0.41,0.86,0.37,0.85,0.13,0.97,0.42,0.87,0.58,0.78,0.86,0.50,0.01,0.86,0.39,0.66,0.61,0.60,0.22,0.10,0.35,0.46,0.10,0.09],
        [0,0,0,0,0,0.34,1.00,0.39,0.48,0.23,0.38,0.17,0.93,0.71,0.40,0.56,0.05,0.17,0.27,0.77,0.63,0.30,0.48,0.79,0.94,0.91,0.63,0.31,0.93,0.75,0.17,0.47],
        [0,0,0,0,0,0,0.44,0.56,0.33,0.64,0.39,0.63,0.60,0.70,0.83,0.99,0.96,0.73,0.21,0.13,0.32,0.56,0.98,0.01,0.42,0.65,0.59,0.52,0.65,0.62,0.41,0.35],
        [0,0,0,0,0,0,0,0.30,0.85,0.80,0.01,0.22,0.68,0.61,0.52,0.42,0.37,0.47,0.25,0.34,0.72,0.91,0.07,0.63,0.24,0.63,0.59,0.28,0.19,0.07,0.27,0.05],
        [0,0,0,0,0,0,0,0,0.66,0.68,0.77,0.38,0.53,0.55,0.24,0.86,0.47,0.68,0.74,0.04,0.55,0.96,0.64,0.49,0.07,0.86,0.41,0.43,0.30,0.52,0.85,0.76],
        [0,0,0,0,0,0,0,0,0,0.81,0.71,0.32,0.66,0.19,0.71,0.97,0.69,0.64,0.50,0.47,0.84,0.95,0.41,0.96,0.56,0.44,0.30,0.65,0.53,0.77,0.83,0.25],
        [0,0,0,0,0,0,0,0,0,0,0.90,0.14,0.17,0.52,0.27,0.22,0.84,0.60,0.72,0.16,0.50,0.40,0.73,0.88,0.77,0.21,0.39,0.89,0.17,0.34,0.43,0.73],
        [0,0,0,0,0,0,0,0,0,0,0,0.34,0.12,0.03,0.40,0.13,0.34,0.71,1.00,0.41,0.80,0.64,0.50,0.58,0.75,0.52,0.84,0.83,0.25,0.47,0.84,0.89],
        [0,0,0,0,0,0,0,0,0,0,0,0,0.47,0.52,0.15,0.29,0.13,0.76,0.64,0.11,0.30,0.45,0.16,0.07,0.22,0.05,0.46,0.61,0.35,0.44,0.32,0.96],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0.72,0.13,0.24,0.11,0.74,0.20,0.47,0.62,0.79,0.21,0.27,0.20,0.04,0.39,0.73,0.10,0.94,0.59,0.04],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.24,0.12,0.58,0.06,0.27,0.64,0.88,0.67,0.24,0.71,0.76,0.63,0.47,0.27,0.67,0.04,0.13,0.69],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.83,0.00,0.66,0.65,0.24,0.62,0.80,0.04,0.57,0.97,0.53,0.79,0.77,0.74,0.07,0.66,0.70],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.72,0.04,0.15,0.91,0.70,0.90,0.89,0.07,0.95,0.68,0.37,0.70,0.72,0.51,0.85,0.41],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.83,0.74,0.60,0.54,0.19,0.84,0.76,0.28,0.21,0.16,0.55,0.33,0.93,0.36,0.98],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.41,0.23,0.45,0.89,0.84,0.96,0.84,0.90,0.84,0.04,0.75,0.26,0.40,0.31],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.19,0.08,0.53,0.67,0.46,0.04,0.11,0.32,0.80,0.82,0.06,0.96,0.43],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.13,0.82,0.66,0.87,0.30,0.59,0.50,0.03,0.77,1.00,0.83,0.46],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.57,0.67,0.34,0.24,0.92,0.48,0.35,0.55,0.72,0.20,0.50],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.14,0.08,0.71,0.94,0.64,0.49,0.11,0.46,0.42,0.08],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.10,0.87,0.76,0.37,0.51,0.68,0.33,0.20,0.08],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.13,0.96,0.78,0.10,0.74,0.35,0.24,0.35],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.72,0.26,0.83,0.85,0.81,0.33,0.10],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.23,0.79,0.71,0.00,0.63,0.51],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.45,0.60,0.10,0.29,0.77],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.25,0.20,0.35,0.00],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.39,0.65,0.18],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.98,0.11],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.43]]
#tabla de probabiliddes
def probabilidad(pais1,pais2):
        prob = 0
        if pais2 > pais1:
                prob = tab[pais1][pais2]
        elif pais1 > pais2:
                prob = 1 - tab[pais2][pais1]
        return prob
def puntaje(probabilidad):
    contador = 0
    if probabilidad > 0.5:
        return (contador+3)
    elif probabilidad < 0.5:
        return (contador)
    elif probabilidad== 0.5:
        return (contador+1)
#puntaje

a = 0
lista_octavos = []
for k in range(8):
        print(" ")
        print("GRUPO",letra[k])
        lista_grupo = []

        for j in range(4):
                for i in range(4):
                        a +=puntaje(probabilidad(dicc[lista_grupos[k][j]],dicc[lista_grupos[k][i]]))
                lista_grupo.append([a,lista_grupos[k][j]])
                lista_grupo.sort(reverse=True)
                #lista de grupo ordenado por puntos
                a = 0
        for i in range(4):
                print(lista_grupo[i])
        lista_octavos.append([lista_grupo[0],lista_grupo[1]])
# Clasificación a octavos
def partido(pais1,pais2):
        if probabilidad(dicc[pais1],dicc[pais2]) > 0.5:
                return pais1
        elif probabilidad(dicc[pais1],dicc[pais2])<0.5:
                return pais2
        else:
                return pais1
#Fase de print
print("")
print("OCTAVOS")
print("_________")
lista_cuartos = []
lista_numeros= [1,3,5,7]
for i in range(4):
        print("")
        print("PARTIDO",lista_numeros[i])
        print(lista_octavos[2*i][0][1],"vs.",lista_octavos[lista_numeros[i]][1][1])
        print("Ganador:",partido(lista_octavos[2*i][0][1],lista_octavos[lista_numeros[i]][1][1]))
        print("")
        print("PARTIDO",lista_numeros[i]+1)
        print(lista_octavos[2*i][1][1],"vs.",lista_octavos[lista_numeros[i]][0][1])
        print("Ganador:",partido(lista_octavos[2*i][1][1],lista_octavos[lista_numeros[i]][0][1]))

        lista_cuartos.append(partido(lista_octavos[2*i][0][1],lista_octavos[lista_numeros[i]][1][1]))
        lista_cuartos.append(partido(lista_octavos[2*i][1][1],lista_octavos[lista_numeros[i]][0][1]))
#Clasificacion a cuartos
lista_semi = []
print("")
print("CUARTOS")
print("_________")
for i in range(4):
        b = partido(lista_cuartos[2*i],lista_cuartos[lista_numeros[i]])
        print("")
        print("PARTIDO",i+1)
        print(lista_cuartos[2*i],"vs.",lista_cuartos[lista_numeros[i]])
        print("GANADOR:",b)
        lista_semi.append(b)
#Clasificación a semifinales
lista_final = []
print("")
print("SEMIFINALES")
print("____________")

for i in range(2):
        c = partido(lista_semi[2*i],lista_semi[lista_numeros[i]])
        print("")
        print("PARTIDO",i+1)
        print(lista_semi[2*i],"vs.",lista_semi[lista_numeros[i]])
        print("GANADOR:",c)
        lista_final.append(c)
#Clasificación a finales
print("")
print("FINAL")
print("_______")

print("")
print(lista_final[0],"vs.",lista_final[1])
print("CAMPEÓN:",partido(lista_final[0],lista_final[1]))

#Fin del programa
