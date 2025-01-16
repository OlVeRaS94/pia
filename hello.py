import flet as ft

def main(page):
    def add_clicked(e):
        if new_task.value.strip() != "":
            page.add(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            send_button.disabled = True
        new_task.focus()
        page.update()

    def text_changed(e):
        send_button.disabled = new_task.value.strip() == ""
        page.update()

    new_task = ft.TextField(hint_text="Tasca pendent", width=300, on_change=text_changed, on_submit=add_clicked)

    send_button = ft.ElevatedButton("Afegeix", on_click=add_clicked, disabled=True)



    page.window.width = 700
    page.window.height = 300
    page.add(ft.Row([new_task, send_button]))
    new_task.focus()

ft.app(target=main)
