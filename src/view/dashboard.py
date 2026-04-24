import flet as ft

def DashboardView(page, tarea_controller):

    user = page.session.get("user")

    if not user:
        page.go("/")
        return ft.View("/", [ft.Text("Redirigiendo...")])

    lista = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def load():
        lista.controls.clear()

        tareas = tarea_controller.obtener_lista(user["id_usuario"])

        for t in tareas:
            lista.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(t["titulo"]),
                            subtitle=ft.Text(t.get("descripcion", "")),
                            trailing=ft.Text(t["estado"])
                        ),
                        padding=10
                    )
                )
            )

        page.update()

    txt = ft.TextField(label="Nueva tarea", expand=True)

    def add(e):
        tarea_controller.guardar_nueva(
            user["id_usuario"],
            txt.value,
            "",
            "media",
            "trabajo"
        )
        txt.value = ""
        load()

    def logout(e):
        page.session.clear()
        page.go("/")

    load()

    return ft.View(
        route="/dashboard",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Bienvenido {user['nombre']}"),
                actions=[ft.IconButton(ft.Icons.LOGOUT, on_click=logout)]
            ),
            ft.Column(
                [
                    ft.Row([
                        txt,
                        ft.FloatingActionButton(ft.Icons.ADD, on_click=add)
                    ]),
                    ft.Divider(),
                    lista
                ],
                expand=True
            )
        ]
    )