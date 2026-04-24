import flet as ft

def LoginView(page, auth_controller):

    email = ft.TextField(label="Correo", width=320)
    password = ft.TextField(label="Contraseña", password=True, width=320)

    msg = ft.Text()

    def login(e):
        try:
            user = auth_controller.login(email.value, password.value)

            if user:
                page.session.set("user", user)
                page.go("/dashboard")
            else:
                msg.value = "Usuario o contraseña incorrectos"
                msg.color = "red"
                page.update()

        except Exception as ex:
            msg.value = f"Error: {ex}"
            msg.color = "red"
            page.update()

    return ft.View(
        route="/",
        controls=[
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.LOCK_PERSON, size=70),
                        ft.Text("SIGE - Login", size=26, weight="bold"),
                        email,
                        password,
                        ft.ElevatedButton("Entrar", on_click=login),
                        msg
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15
                )
            )
        ]
    )