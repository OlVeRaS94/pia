import flet as ft

def main(page: ft.Page):
    # Componentes
    nombre = ft.TextField(label="Ingresa tu nombre")
    saludo = ft.Text()

    def saludar(e):
        saludo.value = f"¡Hola, {nombre.value}!"
        page.update()

    page.add(
        nombre,
        ft.ElevatedButton("Saludar", on_click=saludar),
        saludo
    )

ft.app(target=main)