import flet as ft

def main(page: ft.Page):
    page.title = "MIDIKeymap"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("Asignaciones de Teclas:"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Column(
                    [
                        ft.Text("Asignaciones de slider:"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Column(
                    [
                        ft.Text("Asignaciones de Pads:"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    )
ft.app(target=main)
