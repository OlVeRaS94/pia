class Recurso:
    def __init__(self, titulo, ejemplares):
        # Inicializa un recurso con un título y un número de ejemplares.
        self.titulo = titulo
        self.ejemplares = ejemplares

    def prestar(self):
        # Permite prestar un ejemplar si hay disponibles.
        if self.ejemplares > 0:
            self.ejemplares -= 1  # Reduce el número de ejemplares disponibles.
            return True  # El préstamo fue exitoso.
        return False  # No hay ejemplares disponibles.

    def retornar(self):
        # Devuelve un ejemplar al recurso.
        self.ejemplares += 1

    def __str__(self):
        # Representa el recurso como una cadena.
        return f"{self.titulo} - Ejemplares disponibles: {self.ejemplares}"


class Libro(Recurso):
    def __init__(self, titulo, autor, ejemplares):
        # Inicializa un libro con título, autor y ejemplares.
        super().__init__(titulo, ejemplares)
        self.autor = autor

    def __str__(self):
        # Representa el libro como una cadena con información adicional.
        return f"Libro: '{self.titulo}', Autor: {self.autor}, {super().__str__()}"


class Revista(Recurso):
    def __init__(self, titulo, fecha_publicacion, ejemplares):
        # Inicializa una revista con título, fecha de publicación y ejemplares.
        super().__init__(titulo, ejemplares)
        self.fecha_publicacion = fecha_publicacion

    def __str__(self):
        # Representa la revista como una cadena con información adicional.
        return f"Revista: '{self.titulo}', Fecha de publicación: {self.fecha_publicacion}, {super().__str__()}"


class Pelicula(Recurso):
    def __init__(self, titulo, director, genero, ejemplares):
        # Inicializa una película con título, director, género y ejemplares.
        super().__init__(titulo, ejemplares)
        self.director = director
        self.genero = genero

    def __str__(self):
        # Representa la película como una cadena con información adicional.
        return f"Pelicula: '{self.titulo}', Director: {self.director}, Género: {self.genero}, {super().__str__()}"


class Socio:
    def __init__(self, nombre, dni):
        # Inicializa un socio con nombre, DNI y una lista de libros prestados.
        self.nombre = nombre
        self.dni = dni
        self.libros_prestados = []

    def prestar_libro(self, libro):
        # Permite al socio prestar un libro si no ha superado el límite.
        if len(self.libros_prestados) < 3 and libro.prestar():
            self.libros_prestados.append(libro)  # Agrega el libro a los prestados.
            return True  # El préstamo fue exitoso.
        return False  # No se pudo prestar el libro.

    def retornar_libro(self, libro):
        # Permite al socio retornar un libro prestado.
        if libro in self.libros_prestados:
            libro.retornar()  # Retorna el ejemplar al recurso.
            self.libros_prestados.remove(libro)  # Lo elimina de la lista de prestados.
            return True  # El retorno fue exitoso.
        return False  # El libro no estaba prestado.

    def __str__(self):
        # Representa al socio como una cadena con información de los libros prestados.
        titulos = ', '.join(libro.titulo for libro in self.libros_prestados)
        return f"Socio: {self.nombre}, DNI: {self.dni}, Libros prestados: [{titulos}]" if titulos else f"Socio: {self.nombre}, DNI: {self.dni}, Sin libros prestados."


class Administrador:
    def __init__(self, nombre, dni, cargo):
        # Inicializa un administrador con nombre, DNI y cargo.
        self.nombre = nombre
        self.dni = dni
        self.cargo = cargo

    def __str__(self):
        # Representa al administrador como una cadena.
        return f"Administrador: {self.nombre}, DNI: {self.dni}, Cargo: {self.cargo}"


class Biblioteca:
    def __init__(self):
        # Inicializa la biblioteca con listas vacías para recursos, socios y administradores.
        self.recursos = []
        self.socios = []
        self.administradores = []

    def agregar_recurso(self, tipo, *args):
        # Agrega un recurso (libro, revista o película) a la biblioteca.
        tipos = {'libro': Libro, 'revista': Revista, 'pelicula': Pelicula}
        if tipo in tipos:
            self.recursos.append(tipos[tipo](*args))  # Crea el recurso y lo agrega a la lista.

    def agregar_socio(self, nombre, dni):
        # Agrega un nuevo socio a la biblioteca.
        self.socios.append(Socio(nombre, dni))

    def agregar_administrador(self, nombre, dni, cargo):
        # Agrega un nuevo administrador a la biblioteca.
        self.administradores.append(Administrador(nombre, dni, cargo))

    def prestar_recurso(self, dni_socio, titulo_recurso):
        # Procesa la solicitud de préstamo de un recurso por un socio.
        socio = next((s for s in self.socios if s.dni == dni_socio), None)  # Busca el socio por DNI.
        recurso = next((r for r in self.recursos if r.titulo == titulo_recurso), None)  # Busca el recurso por título.
        return socio.prestar_libro(recurso) if socio and recurso else False  # Intenta prestar el recurso.

    def retornar_recurso(self, dni_socio, titulo_recurso):
        # Procesa la solicitud de retorno de un recurso por un socio.
        socio = next((s for s in self.socios if s.dni == dni_socio), None)  # Busca el socio por DNI.
        recurso = next((r for r in self.recursos if r.titulo == titulo_recurso), None)  # Busca el recurso por título.
        return socio.retornar_libro(recurso) if socio and recurso else False  # Intenta retornar el recurso.

    def mostrar_recursos(self, tipo=None):
        # Muestra los recursos disponibles en la biblioteca.
        for recurso in self.recursos:
            if tipo is None or (tipo == 'todos' or isinstance(recurso, {'libro': Libro, 'revista': Revista, 'pelicula': Pelicula}[tipo])):
                print(recurso)  # Imprime la información del recurso.

    def mostrar_socios(self):
        # Muestra todos los socios registrados en la biblioteca.
        for socio in self.socios:
            print(socio)

    def mostrar_administradores(self):
        # Muestra todos los administradores registrados en la biblioteca.
        for admin in self.administradores:
            print(admin)

    def mostrar_recursos_prestados(self):
        # Muestra la información sobre qué recursos están prestados a cada socio.
        for socio in self.socios:
            if socio.libros_prestados:
                print(socio)  # Imprime la información del socio y sus libros prestados.


# Programa de prueba
if __name__ == "__main__":
    biblioteca = Biblioteca()  # Crea una instancia de la biblioteca.

    while True:
        # Muestra las opciones del menú.
        opciones = {
            "1": "Agregar libro",
            "2": "Agregar revista",
            "3": "Agregar película",
            "4": "Agregar socio",
            "5": "Agregar administrador",
            "6": "Prestar recurso",
            "7": "Retornar recurso",
            "8": "Mostrar recursos",
            "9": "Mostrar socios",
            "10": "Mostrar administradores",
            "11": "Mostrar recursos prestados",
            "12": "Salir"
        }

        for key, value in opciones.items():
            print(f"{key}. {value}")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            ejemplares = int(input("Número de ejemplares: "))
            biblioteca.agregar_recurso('libro', titulo, autor, ejemplares)  # Agrega un libro.

        elif opcion == "2":
            titulo = input("Título de la revista: ")
            fecha_publicacion = input("Fecha de publicación (DD-MM-AAAA): ")
            ejemplares = int(input("Número de ejemplares: "))
            biblioteca.agregar_recurso('revista', titulo, fecha_publicacion, ejemplares)  # Agrega una revista.

        elif opcion == "3":
            titulo = input("Título de la película: ")
            director = input("Director de la película: ")
            genero = input("Género de la película: ")
            ejemplares = int(input("Número de ejemplares: "))
            biblioteca.agregar_recurso('pelicula', titulo, director, genero, ejemplares)  # Agrega una película.

        elif opcion == "4":
            nombre = input("Nombre del socio: ")
            dni = input("DNI del socio: ")
            biblioteca.agregar_socio(nombre, dni)  # Agrega un socio.

        elif opcion == "5":
            nombre = input("Nombre del administrador: ")
            dni = input("DNI del administrador: ")
            cargo = input("Cargo del administrador: ")
            biblioteca.agregar_administrador(nombre, dni, cargo)  # Agrega un administrador.

        elif opcion == "6":
            dni_socio = input("DNI del socio: ")
            titulo_recurso = input("Título del recurso: ")
            if biblioteca.prestar_recurso(dni_socio, titulo_recurso):
                print("Préstamo realizado con éxito.")  # Mensaje de éxito en préstamo.
            else:
                print("No se pudo realizar el préstamo.")  # Mensaje de error.

        elif opcion == "7":
            dni_socio = input("DNI del socio: ")
            titulo_recurso = input("Título del recurso: ")
            if biblioteca.retornar_recurso(dni_socio, titulo_recurso):
                print("Retorno realizado con éxito.")  # Mensaje de éxito en retorno.
            else:
                print("No se pudo realizar el retorno.")  # Mensaje de error.

        elif opcion == "8":
            tipo = input("¿Qué tipo de recurso deseas ver? (libro/revista/pelicula/todos): ").lower()
            biblioteca.mostrar_recursos('todos' if tipo == 'todos' else tipo)  # Muestra los recursos.

        elif opcion == "9":
            biblioteca.mostrar_socios()  # Muestra los socios.

        elif opcion == "10":
            biblioteca.mostrar_administradores()  # Muestra los administradores.

        elif opcion == "11":
            biblioteca.mostrar_recursos_prestados()  # Muestra los recursos prestados a cada socio.

        elif opcion == "12":
            print("Saliendo del programa.")  # Mensaje de salida.
            break  # Termina el bucle.

        else:
            print("Opción no válida. Inténtalo de nuevo.")  # Mensaje de opción no válida.
