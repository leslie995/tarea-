class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f" Bienvenidos, soy {self.nombre}, artista de {self.genero} "
              f"(popularidad: {self.popularidad}/100).")

    def actuar(self):
        print(f"{self.nombre} está actuando...")

    def despedirse(self):
        print(f" {self.nombre} se despide. ¡Gracias por venir!")


class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f" {self.nombre} canta su éxito {self.cancion_mas_popular} con gran energía.")


class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f" El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")


class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f" La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")


def iniciar_festival(lista_artistas):
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print(" Fin de la actuación ")
        print("-" * 50)


def pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
        except ValueError:
            pass
        print(f"Introduce un número entre {minimo} y {maximo}.")


def main():
    lista_artistas = []
    cantidad = pedir_entero("¿Cuántos artistas se presentarán? ", 1, 100)

    for i in range(1, cantidad + 1):
        print(f"\n--- Artista {i} ---")
        tipo = ""
        while tipo not in ("cantante", "dj", "banda"):
            tipo = input("Tipo (Cantante, DJ o Banda): ").strip().lower()
        nombre = input("Nombre: ")
        genero = input("Género musical: ")
        popularidad = pedir_entero("Popularidad (1-100): ", 1, 100)

        if tipo == "cantante":
            cancion = input("Canción más popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)
        elif tipo == "dj":
            estilo = input("Estilo: ")
            artista = DJ(nombre, genero, popularidad, estilo)
        else:
            integrantes = pedir_entero("Número de integrantes: ", 1, 50)
            artista = Banda(nombre, genero, popularidad, integrantes)

        lista_artistas.append(artista)

    print("\n🎉 ¡COMIENZA EL FESTIVAL! 🎉\n")
    iniciar_festival(lista_artistas)


if __name__ == "__main__":
    main()