import flet as ft

def dashboardView(page, tarea_controller):
    user = page.session.get("user")

    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    def refresh():
        lista_tareas.controls.clear()

        tareas = tarea_controller.obtener_lista(user['id_usuario'])

        if not tareas:
            lista_tareas.controls.append(
                ft.Text("No hay tareas")
            )
        else:
            for t in tareas:
                lista_tareas.controls.append(
                    ft.Text(f"{t['titulo']} - {t['estado']}")
                )

        page.update()

    txt_titulo = ft.TextField(label="Nueva tarea", expand=True)

    def add_task(e):
        success, msg = tarea_controller.guardar_nueva(
            user['id_usuario'], 
            txt_titulo.value, 
            "", 
            "media", 
            "trabajo"
        )
        if success:
            txt_titulo.value = ""
            refresh()

    refresh()

    return ft.View(
        "/dashboard",
        [
            ft.AppBar(
                title=ft.Text(f"Bienvenido {user['nombre']}"),
                actions=[
                    ft.TextButton("Salir", on_click=lambda _: page.go("/"))
                ],
            ),
            ft.Column(
                [
                    ft.Row([
                        txt_titulo,
                        ft.ElevatedButton("Agregar", on_click=add_task),
                    ]),
                    ft.Divider(),
                    ft.Text("Tareas:"),
                    lista_tareas
                ],
                expand=True,
                padding=20
            )
        ]
    )