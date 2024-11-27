class RecursoBiblioteca:
    """Clase base para los recursos de la biblioteca."""
    def __init__(self, nombre, cantidad):
        self.nombre = nombre  # Título del recurso
        self.cantidad = cantidad  # Número de ejemplares disponibles

    def prestar(self):
        """Permite prestar un ejemplar del recurso."""
        if self.cantidad > 0:
            self.cantidad -= 1  # Reduce la cantidad de ejemplares
            return True
        return False  # No hay ejemplares disponibles

    def retornar(self):
        """Devuelve un ejemplar del recurso."""
        self.cantidad += 1  # Aumenta la cantidad de ejemplares

    def __str__(self):
        """Representa el recurso como una cadena."""
        return f"{self.nombre} - Ejemplares disponibles: {self.cantidad}"


class Libro(RecursoBiblioteca):
    """Clase que representa un libro."""
    def __init__(self, nombre, autor, cantidad):
        super().__init__(nombre, cantidad)
        self.autor = autor  # Autor del libro

    def __str__(self):
        """Representa el libro como una cadena."""
        return f"Libro: {self.nombre}, Autor: {self.autor}, {super().__str__()}"


class Revista(RecursoBiblioteca):
    """Clase que representa una revista."""
    def __init__(self, nombre, fecha_publicacion, cantidad):
        super().__init__(nombre, cantidad)
        self.fecha_publicacion = fecha_publicacion  # Fecha de publicación

    def __str__(self):
        """Representa la revista como una cadena."""
        return f"Revista: {self.nombre}, Fecha de publicación: {self.fecha_publicacion}, {super().__str__()}"


class Pelicula(RecursoBiblioteca):
    """Clase que representa una película."""
    def __init__(self, nombre, director, genero, cantidad):
        super().__init__(nombre, cantidad)
        self.director = director  # Director de la película
        self.genero = genero  # Género de la película

    def __str__(self):
        """Representa la película como una cadena."""
        return f"Pelicula: {self.nombre}, Director: {self.director}, Género: {self.genero}, {super().__str__()}"


class Usuario:
    """Clase que representa a un socio de la biblioteca."""
    def __init__(self, nombre, dni):
        self.nombre = nombre  # Nombre del socio
        self.dni = dni  # DNI del socio
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, libro):
        """Permite al socio prestar un libro."""
        if len(self.libros_prestados) < 3 and libro.prestar():
            self.libros_prestados.append(libro)  # Agrega el libro a la lista de prestados
            return True
        return False  # No se puede prestar el libro

    def retornar_libro(self, libro):
        """Permite al socio retornar un libro prestado."""
        if libro in self.libros_prestados:
            libro.retornar()  # Devuelve el libro
            self.libros_prestados.remove(libro)  # Lo quita de la lista de prestados
            return True
        return False  # El libro no está prestado

    def __str__(self):
        """Representa al socio como una cadena."""
        return f"Usuario: {self.nombre}, DNI: {self.dni}, Libros prestados: {[libro.nombre for libro in self.libros_prestados]}"


class AdministradorBiblioteca:
    """Clase que representa a un administrador de la biblioteca."""
    def __init__(self, nombre, dni, cargo):
        self.nombre = nombre  # Nombre del administrador
        self.dni = dni  # DNI del administrador
        self.cargo = cargo  # Cargo del administrador

    def __str__(self):
        """Representa al administrador como una cadena."""
        return f"Administrador: {self.nombre}, DNI: {self.dni}, Cargo: {self.cargo}"


class Biblioteca:
    """Clase que representa la biblioteca y gestiona los recursos y usuarios."""
    def __init__(self):
        self.recursos = []  # Lista de recursos
        self.usuarios = []  # Lista de socios
        self.administradores = []  # Lista de administradores

    def agregar_libro(self, nombre, autor, cantidad):
        """Agrega un libro a la biblioteca."""
        libro = Libro(nombre, autor, cantidad)
        self.recursos.append(libro)

    def agregar_revista(self, nombre, fecha_publicacion, cantidad):
        """Agrega una revista a la biblioteca."""
        revista = Revista(nombre, fecha_publicacion, cantidad)
        self.recursos.append(revista)

    def agregar_pelicula(self, nombre, director, genero, cantidad):
        """Agrega una película a la biblioteca."""
        pelicula = Pelicula(nombre, director, genero, cantidad)
        self.recursos.append(pelicula)

    def agregar_usuario(self, nombre, dni):
        """Agrega un nuevo socio a la biblioteca."""
        usuario = Usuario(nombre, dni)
        self.usuarios.append(usuario)

    def agregar_administrador(self, nombre, dni, cargo):
        """Agrega un administrador a la biblioteca."""
        admin = AdministradorBiblioteca(nombre, dni, cargo)
        self.administradores.append(admin)

    def prestar_recurso(self, dni_usuario, nombre_recurso):
        """Gestiona el préstamo de un recurso a un socio."""
        usuario = next((u for u in self.usuarios if u.dni == dni_usuario), None)
        recurso = next((r for r in self.recursos if r.nombre == nombre_recurso), None)
        if usuario and recurso:
            return usuario.prestar_libro(recurso)
        return False  # No se pudo realizar el préstamo

    def retornar_recurso(self, dni_usuario, nombre_recurso):
        """Gestiona el retorno de un recurso prestado."""
        usuario = next((u for u in self.usuarios if u.dni == dni_usuario), None)
        recurso = next((r for r in self.recursos if r.nombre == nombre_recurso), None)
        if usuario and recurso:
            return usuario.retornar_libro(recurso)
        return False  # No se pudo realizar el retorno

    def mostrar_recursos(self, tipo=None):
        """Muestra los recursos de la biblioteca según su tipo."""
        for recurso in self.recursos:
            if not tipo or (tipo == 'libro' and isinstance(recurso, Libro)) or \
               (tipo == 'revista' and isinstance(recurso, Revista)) or \
               (tipo == 'pelicula' and isinstance(recurso, Pelicula)):
                print(recurso)

    def mostrar_usuarios(self):
        """Muestra todos los socios de la biblioteca."""
        for usuario in self.usuarios:
            print(usuario)

    def mostrar_administradores(self):
        """Muestra todos los administradores de la biblioteca."""
        for admin in self.administradores:
            print(admin)

    def mostrar_libros_prestados(self):
        """Muestra todos los libros prestados."""
        for usuario in self.usuarios:
            print(usuario)


# Programa de prueba
if __name__ == "__main__":
    mi_biblioteca = Biblioteca()
    
    while True:
        print("\nA. Agregar libro")
        print("B. Agregar revista")
        print("C. Agregar película")
        print("D. Agregar socio")
        print("E. Agregar administrador")
        print("F. Prestar recurso")
        print("G. Retornar recurso")
        print("H. Mostrar recursos")
        print("I. Mostrar socios")
        print("J. Mostrar administradores")
        print("K. Mostrar libros prestados")
        print("L. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "A":
            nombre = input("Título del libro: ")
            autor = input("Autor del libro: ")
            cantidad = int(input("Número de ejemplares: "))
            mi_biblioteca.agregar_libro(nombre, autor, cantidad)

        elif opcion == "B":
            nombre = input("Título de la revista: ")
            fecha_publicacion = input("Fecha de publicación (AAAA-MM-DD): ")
            cantidad = int(input("Número de ejemplares: "))
            mi_biblioteca.agregar_revista(nombre, fecha_publicacion, cantidad)

        elif opcion == "C":
            nombre = input("Título de la película: ")
            director = input("Director de la película: ")
            genero = input("Género de la película: ")
            cantidad = int(input("Número de ejemplares: "))
            mi_biblioteca.agregar_pelicula(nombre, director, genero, cantidad)

        elif opcion == "D":
            nombre = input("Nombre del socio: ")
            dni = input("DNI del socio: ")
            mi_biblioteca.agregar_usuario(nombre, dni)

        elif opcion == "E":
            nombre = input("Nombre del administrador: ")
            dni = input("DNI del administrador: ")
            cargo = input("Cargo del administrador: ")
            mi_biblioteca.agregar_administrador(nombre, dni, cargo)

        elif opcion == "F":
            dni_usuario = input("DNI del socio: ")
            nombre_recurso = input("Título del recurso: ")
            if mi_biblioteca.prestar_recurso(dni_usuario, nombre_recurso):
                print("Préstamo realizado con éxito.")
            else:
                print("No se pudo realizar el préstamo.")

        elif opcion == "G":
            dni_usuario = input("DNI del socio: ")
            nombre_recurso = input("Título del recurso: ")
            if mi_biblioteca.retornar_recurso(dni_usuario, nombre_recurso):
                print("Retorno realizado con éxito.")
            else:
                print("No se pudo realizar el retorno.")

        elif opcion == "H":
            tipo = input("¿Qué tipo de recurso deseas ver? (libro/revista/pelicula/todos): ").lower()
            if tipo == 'todos':
                mi_biblioteca.mostrar_recursos()
            else:
                mi_biblioteca.mostrar_recursos(tipo)

        elif opcion == "I":
            mi_biblioteca.mostrar_usuarios()

        elif opcion == "J":
            mi_biblioteca.mostrar_administradores()

        elif opcion == "K":
            mi_biblioteca.mostrar_libros_prestados()

        elif opcion == "L":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")
