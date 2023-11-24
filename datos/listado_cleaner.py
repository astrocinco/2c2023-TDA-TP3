def lista_listado_completo():
    set_jugadores = set()
    lista_jugadores = list()

    with open("datos\listado_completo.txt") as archivo:
        for linea in archivo:
            set_jugadores.add(linea[:-1])
            lista_jugadores.append(linea[:-1])
            #print(linea[:-1])

    return set_jugadores, lista_jugadores


def write_clear_listado_completo(set_jugadores):
    file = open("listado_completo_31.txt", "a")

    for player in set_jugadores:
        file.write(player + "\n")
    file.close()


if __name__ == "__main__":
    set_jugadores, lista_jugadores = lista_listado_completo()
    print(set_jugadores)
    #print(lista_jugadores)
    #print("Largos:", len(set_jugadores), len(lista_jugadores))
    write_clear_listado_completo(set_jugadores)