import math
import json

# Dibuix global
Dibuix = {
    "ample": 800,
    "alt": 600,
    "figures": []
}

# Clase Punt
class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def dist_x(self, other):
        return abs(self.x - other.x)

    def dist_y(self, other):
        return abs(self.y - other.y)

# Clase Figura
class Figura:
    def __init__(self, punt, color):
        self.punt = punt
        self.color = color

    def __str__(self):
        return f"Figura en {self.punt} de color {self.color}"

    def area(self):
        raise NotImplementedError("El método area() debe ser implementado en las subclases")

    def perimetre(self):
        raise NotImplementedError("El método perimetre() debe ser implementado en las subclases")

# Clase Rectangle
class Rectangle(Figura):
    def __init__(self, punt1, punt2, color):
        super().__init__(punt1, color)
        self.punt2 = punt2

    def area(self):
        return self.punt.dist_x(self.punt2) * self.punt.dist_y(self.punt2)

    def perimetre(self):
        return 2 * (self.punt.dist_x(self.punt2) + self.punt.dist_y(self.punt2))

    def __str__(self):
        return f"Rectangle de color {self.color}, des de {self.punt} fins a {self.punt2}"

# Clase Cercle
class Cercle(Figura):
    def __init__(self, punt, radi, color):
        super().__init__(punt, color)
        self.radi = radi

    def area(self):
        return math.pi * (self.radi**2)

    def perimetre(self):
        return 2 * math.pi * self.radi

    def __str__(self):
        return f"Cercle de color {self.color} amb centre a {self.punt} i radi {self.radi}"

# Clase Linia
class Linia(Figura):
    def __init__(self, punt1, punt2, color):
        super().__init__(punt1, color)
        self.punt2 = punt2

    def area(self):
        return 0  # Las líneas no tienen área

    def perimetre(self):
        return self.punt.dist(self.punt2)  # La longitud de la línea

    def __str__(self):
        return f"Linia de color {self.color}, des de {self.punt} fins a {self.punt2}"

# Función para mostrar el menú principal
def mostrar_menu():
    print("\nIndica el que vols fer:")
    print("  1 - Afegir figura al dibuix")
    print("  2 - Carregar dibuix des de fitxer")
    print("  3 - Exportar dibuix a SVG")
    print("  4 - Dibuixar i eixir")

# Función para mostrar el submenú de figuras
def mostrar_submenu_figures():
    print("\nIndica la figura que vols afegir:")
    print("  1 - Linia")
    print("  2 - Rectangle")
    print("  3 - Cercle")

# Función para añadir una figura
def afegir_figura():
    mostrar_submenu_figures()
    opcio = input("Introdueix l'opció: ")

    if opcio == '1':  # Linia
        dades = input("Introdueix les dades de la linia (x1 y1 x2 y2 #color): ")
        x1, y1, x2, y2, color = dades.split()
        l = Linia(Punt(int(x1), int(y1)), Punt(int(x2), int(y2)), color)
        Dibuix["figures"].append(l)
    elif opcio == '2':  # Rectangle
        dades = input("Introdueix les dades de la Rectangle (x1 y1 x2 y2 #color): ")
        x1, y1, x2, y2, color = dades.split()
        r = Rectangle(Punt(int(x1), int(y1)), Punt(int(x2), int(y2)), color)
        Dibuix["figures"].append(r)
    elif opcio == '3':  # Cercle
        dades = input("Introdueix les dades de la Cercle (x1 y1 r #color): ")
        x, y, r, color = dades.split()
        c = Cercle(Punt(int(x), int(y)), int(r), color)
        Dibuix["figures"].append(c)
    else:
        print("Figura no reconeguda.")

# Función para cargar el dibujo desde un archivo
def carregar_dibuix():
    fitxer = input("Indica el nom del fitxer a carregar: ")
    try:
        with open(fitxer, 'r') as f:
            global Dibuix
            Dibuix = json.load(f)
            print(f"Dibuix carregat correctament des de {fitxer}.")
            for figura in Dibuix["figures"]:
                print(figura)
    except FileNotFoundError:
        print(f"El fitxer {fitxer} no existeix.")
    except json.JSONDecodeError:
        print("Error en carregar el fitxer. El format del JSON no és vàlid.")

# Función para exportar el dibujo a un archivo SVG
def exportar_svg():
    fitxer = input("Indica el nom del fitxer SVG a guardar: ")
    try:
        with open(fitxer, 'w') as f:
            f.write('<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">\n')
            
            for figura in Dibuix["figures"]:
                if isinstance(figura, Rectangle):
                    f.write(f'<rect x="{figura.punt.get_x()}" y="{figura.punt.get_y()}" '
                            f'width="{figura.punt.dist_x(figura.punt2)}" '
                            f'height="{figura.punt.dist_y(figura.punt2)}" '
                            f'fill="{figura.color}"/>\n')
                elif isinstance(figura, Cercle):
                    f.write(f'<circle cx="{figura.punt.get_x()}" cy="{figura.punt.get_y()}" '
                            f'r="{figura.radi}" fill="{figura.color}"/>\n')
                elif isinstance(figura, Linia):
                    f.write(f'<line x1="{figura.punt.get_x()}" y1="{figura.punt.get_y()}" '
                            f'x2="{figura.punt2.get_x()}" y2="{figura.punt2.get_y()}" '
                            f'stroke="{figura.color}"/>\n')

            f.write('</svg>\n')
        
        print(f"Dibuix exportat a {fitxer} correctament.")
    except Exception as e:
        print(f"Ha ocurrido un error al exportar el dibujo: {e}")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcio = input("Introdueix l'opció: ")

        if opcio == '1':
            afegir_figura()
            print("Figura afegida amb èxit!")
        elif opcio == '2':
            carregar_dibuix()  # Cargar dibujo desde archivo
        elif opcio == '3':
            exportar_svg()  # Exportar dibujo a SVG
        elif opcio == '4':
            print("Dibuixant...")
            for figura in Dibuix["figures"]:
                print(figura)
            break
        else:
            print("Opció no vàlida. Torna a intentar-ho.")

# Prueba del código
if __name__ == "__main__":
    main()
