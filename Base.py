import random

bombos =[["Rusia", "Alemania", "Brasil", "Portugal", "Argentina", "Bélgica", "Polonia", "Francia"],
        ["España", "Perú", "Suiza", "Inglaterra", "Colombia", "México", "Uruguay", "Croacia"],
        ["Dinamarca", "Islandia", "Costa Rica", "Suecia", "Túnez", "Egipto", "Senegal", "Irán"],
        ["Serbia", "Nigeria", "Australia", "Japón", "Marruecos", "Panamá", "Corea del Sur", "Saudita"]]


for i in range (8):
  grupo = []
  lista_grupos = []
  for j in bombos:
    aux= random.randint(0,len(j)-1)
    grupo.append(j[aux])
    j.pop(aux)
  lista_grupos.append(grupo)

  print(lista_grupos)
